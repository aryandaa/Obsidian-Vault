#cybersecurity

`checksec` menampilkan proteksi yang aktif di binary. Ini wajib dijalankan di awal setiap challenge - strategi exploit kamu ditentukan oleh hasilnya.

## Menjalankan

```bash
# Dari pwntools
checksec --file=./chall

# Dari dalam python
python3 -c "from pwn import *; print(ELF('./chall').checksec())"
```

## Contoh output

```
Arch:     amd64-64-little
RELRO:    Partial RELRO
Stack:    Canary found
NX:       NX enabled
PIE:      PIE enabled
```

## Arti tiap baris

| Baris | Arti | Kalau aktif |
|---|---|---|
| `Arch` | Arsitektur (i386/amd64) | Tentukan p32/p64 |
| `RELRO` | Proteksi GOT | Full → GOT read-only; Partial → GOT overwrite mungkin |
| `Stack: Canary found` | Ada canary | Perlu leak canary atau brute force |
| `NX enabled` | Stack tidak executable | Tidak bisa ret2shellcode langsung; pakai ROP |
| `PIE enabled` | Alamat binary acak | Perlu leak base address |

## Kombinasi umum & strategi

| NX | PIE | Canary | Strategi awal |
|---|---|---|---|
| off | off | no | ret2shellcode (paling mudah) |
| on | off | no | ret2win / ret2libc |
| on | off | yes | leak canary → ret2libc |
| on | on | no | leak PIE → ret2libc |
| on | on | yes | leak canary + PIE (paling sulit) |

## Tabel proteksi

| Proteksi | Detail materi |
|---|---|
| NX | [[NX]] |
| ASLR (system-level) | [[ASLR dan PIE]] |
| PIE | [[ASLR dan PIE]] |
| Stack Canary | [[Stack Canary]] |
| RELRO | [[RELRO]] |

## Catatan

- ASLR **tidak terlihat di checksec** - itu proteksi level OS. Cek dengan:

```bash
cat /proc/sys/kernel/randomize_va_space
# 2 = ASLR aktif (default Linux)
# 0 = mati
```

- `checksec` juga bisa cek binary dari remote? Tidak langsung - tapi banyak CTF menyertakan binary & libc-nya, jadi cek di file lokal.
- FORTIFY (baris lain di checksec) menandakan compiler menambahkan pemeriksaan ekstra - jarang jadi penghalang utama di CTF.
