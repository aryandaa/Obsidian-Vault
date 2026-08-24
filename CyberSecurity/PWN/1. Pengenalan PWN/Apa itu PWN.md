#cybersecurity

PWN (dari kata "own") adalah kategori CTF yang berfokus pada **binary exploitation**: menemukan bug di program yang sudah dikompilasi, lalu memanfaatkannya untuk mengubah alur program - biasanya sampai menjalankan shell atau membaca flag.

## Contoh challenge PWN

Kamu diberi file binary:

```bash
$ file chall
chall: ELF 64-bit LSB executable, x86-64
$ ./chall
Masukkan nama: AAAAAAAAAAAAAAAAAAAAAAAA
Halo AAAAAAAAAAAAAAAAAAAAAAAA
Segmentation fault (core dumped)
```

Program crash karena input terlalu panjang → ada **buffer overflow**. Tugasmu: kontrol crash itu, ubah alur program, dapatkan shell → `cat flag.txt`.

## Kenapa disebut "exploitation"?

Bug di binary seperti:
- **Buffer overflow** - menulis melebihi batas buffer di stack
- **Format string** - input user dipakai sebagai format string `printf(user_input)`
- **Use after free** - memakai memori yang sudah dibebaskan
- **Integer overflow** - angka melebihi batas tipe data

Exploit = menyusun input khusus (payload) yang mengubah bug menjadi kontrol penuh.

## Konsep yang wajib dikuasai

| Konsep | Kenapa penting |
|---|---|
| Stack & heap | Tempat data & alur program disimpan |
| Register & calling convention | Cara fungsi dipanggil & argumen dikirim |
| Assembly x86/x64 | Bahasa mesin yang dieksekusi CPU |
| Endianness | Cara byte disimpan di memory |
| ELF format | Struktur binary Linux |
| Proteksi (NX, ASLR, PIE, Canary, RELRO) | Penghalang yang harus di-bypass |
| GOT/PLT | Cara program memanggil fungsi library |

## Alur umum menyelesaikan challenge

```
1. Analisis binary (file, checksec, strings, decompile)
2. Pahami bug-nya (baca source code kalau ada, atau reverse engineer)
3. Hitung offset / posisi kontrol
4. Susun payload (pakai pwntools)
5. Jalankan exploit lokal -> remote (nc host port)
6. Dapatkan shell -> cat flag
```

## Bedanya dengan Reverse Engineering

| | Reverse Engineering | PWN |
|---|---|---|
| Fokus | Memahami cara kerja program | Mengeksploitasi program |
| Tujuan | Baca flag dari logika (serial, crackme) | Kontrol eksekusi (shell) |
| Butuh | Disassembler, debugger | Semua itu + payload & mitigasi |

Keduanya saling melengkapi: untuk PWN kamu harus bisa membaca assembly (RE skill), dan untuk RE yang baik kamu paham cara program dieksekusi (PWN skill).

## Etika

Sama seperti kategori lain: hanya exploit binary yang memang diperbolehkan (CTF, lab sendiri, atau binary yang kamu punya izin). Jangan menyerang sistem orang lain.
