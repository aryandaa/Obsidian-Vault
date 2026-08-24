#tools

`objdump` dan `readelf` adalah tools binutils untuk membaca struktur binary dan disassembly. Penting untuk analisis statis (tanpa menjalankan program).

## objdump - disassembly

```bash
# Disassembly semua section text
objdump -d chall

# Disassembly fungsi tertentu
objdump -d chall | grep -A50 "<vuln>:"

# Disassembly dengan source (kalau ada debug info)
objdump -d -S chall

# Lihat PLT
objdump -d chall | grep -A5 "<puts@plt>"

# Cari instruksi tertentu
objdump -d chall | grep "pop.*rdi"
```

Contoh output:

```asm
0000000000401236 <vuln>:
  401236:       55                      push   rbp
  401237:       48 89 e5                mov    rbp,rsp
  40123a:       48 83 ec 40             sub    rsp,0x40
  40123e:       48 8d 45 c0             lea    rax,[rbp-0x40]
  401242:       48 89 c7                mov    rdi,rax
  401245:       e8 06 ff ff ff          call   401150 <gets@plt>
```

Dari sini: buffer di `rbp-0x40` (64 byte) → offset ke return address = 0x40 + 8 = 72.

## readelf - struktur ELF

```bash
# Header
readelf -h chall

# Section
readelf -S chall

# Symbol (fungsi & variabel)
readelf -s chall | grep FUNC

# Dynamic imports
readelf -d chall | grep NEEDED
#   Shared library: [libc.so.6]

# Relokasi (GOT)
readelf -r chall

# Segmen (NX, flags)
readelf -l chall | grep GNU_STACK
```

## Membaca ukuran buffer dari disassembly

```asm
sub rsp, 0x40       ; 64 byte untuk local variables
lea rax, [rbp-0x40] ; buffer mulai di rbp-0x40
```

Offset ke return address = `0x40 + 8 (saved rbp)` = 72 (64-bit).

## Tools alternatif

```bash
# radare2 / rizin
r2 ./chall

# objdump versi canggih
rizin -qc "aaa; s sym.vuln; pdf" chall

# Capstone (python)
from capstone import *
md = Cs(CS_ARCH_X86, CS_MODE_64)
```

## Tips

1. `objdump -d` + `grep` untuk cari gadget & alamat fungsi cepat.
2. `readelf -s` memberi alamat symbol - cocokkan dengan `elf.sym` pwntools.
3. Binary stripped → nama fungsi hilang; cari lewat pola (prolog `push rbp; mov rbp,rsp`) atau Ghidra.
4. `file chall` dulu untuk tahu arsitektur, baru pilih `objdump` yang sesuai.
