# Script untuk membaca informasi binary ELF dengan pwntools - langkah awal analisis PWN.
# Jalankan: python3 baca_elf.py <binary>

import sys
from pwn import *

context.log_level = "error"

path = sys.argv[1] if len(sys.argv) > 1 else "./chall"
elf = ELF(path)

print("=" * 50)
print("[*] Informasi binary:", elf.path)
print("[*] Arch            :", elf.arch)
print("[*] Bit             :", elf.bits)
print("[*] Endian          :", elf.endian)
print("[*] PIE             :", elf.pie)
print("[*] NX              :", elf.nx)
print("[*] Canary          :", elf.canary)
print("[*] RELRO           :", elf.relro)
print("=" * 50)

print("\n[*] Fungsi yang ada (symbol):")
for name, addr in sorted(elf.symbols.items()):
    if name in ("main", "win", "vuln", "system", "puts", "gets"):
        print(f"    {hex(addr)} {name}")

print("\n[*] Import (PLT):")
for name in elf.plt:
    print(f"    {name} @ {hex(elf.plt[name])}")

print("\n[*] GOT:")
for name in elf.got:
    print(f"    {name} @ {hex(elf.got[name])}")

print("\n[*] String /bin/sh:")
for addr in elf.search(b"/bin/sh"):
    print(f"    {hex(addr)}")

print("\n[*] String flag:")
for addr in elf.search(b"flag"):
    print(f"    {hex(addr)}")
