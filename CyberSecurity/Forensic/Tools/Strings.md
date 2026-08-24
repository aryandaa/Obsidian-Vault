#tool 

Kalau `file` menjawab pertanyaan "ini benda apa?", maka `strings` menjawab pertanyaan **"di dalam benda ini ada kata-kata apa saja?"**. Tool ini terlihat sederhana, tetapi dalam dunia forensic ia adalah salah satu senjata pertama yang paling sering menghasilkan flag.

`strings` bekerja dengan cara membaca sebuah file binary dan mengekstrak rangkaian karakter yang bisa dibaca (printable). Secara konsep:

```text
Binary file
    ↓
Baca byte per byte
    ↓
Kumpulkan rangkaian karakter printable
    ↓
Tampilkan sebagai string
```

Kenapa ini berguna untuk forensic? Karena banyak informasi penting disimpan dalam bentuk teks di dalam file binary. URL, alamat IP, nama file, command, password, token, nama pengguna, domain, dan bahkan flag CTF sering kali masih bisa dibaca langsung.

```
Jangan menganggap flag selalu berbentuk file. Flag bisa berada di dalam metadata,
di dalam gambar, di dalam memory dump, di dalam log, atau bahkan di dalam
unallocated space. `strings` adalah tool pertama untuk mencarinya.
```

---
## 1. Instalasi

Pada distro berbasis Debian, `strings` berasal dari package `binutils` dan biasanya sudah tersedia.

Cek:

```bash
strings --version
```

atau:

```bash
which strings
```

Kalau belum ada:

```bash
sudo apt update
sudo apt install binutils
```

---
# 2. Penggunaan Paling Dasar

```bash
strings file.bin
```

Outputnya adalah daftar string yang ditemukan.

Misalnya:

```bash
strings suspicious.bin
```

bisa menghasilkan sesuatu seperti:

```text
powershell.exe
-enc
http://malicious.example.com/update
flag{ini_bukan_flag_asli}
```

Perhatikan: tanpa filtering, output `strings` bisa sangat panjang, apalagi untuk file besar. Biasanya kita langsung menggabungkannya dengan `grep`.

---
# 3. `strings` dan `grep`: Kombinasi Paling Sakti

Ini pola yang paling sering dipakai di CTF:

```bash
strings file.bin | grep -i flag
```

```bash
strings file.bin | grep -iE "http|https"
```

```bash
strings memory.raw | grep -i password
```

Karena `strings` menghasilkan teks per baris, outputnya sangat ramah untuk diproses oleh `grep`, `head`, `tail`, `sort`, `uniq`, dan `awk`.

Contoh untuk melihat potongan string yang menarik dengan konteks:

```bash
strings file.bin | grep -A 5 -B 5 "secret"
```

---
# 4. Flag `-n` (Minimum Length)

Secara default, `strings` hanya menampilkan string dengan panjang minimal 4 karakter.

Dengan:

```bash
-n <angka>
```

kamu bisa mengubah ambang tersebut.

Contoh, menampilkan string minimal 8 karakter:

```bash
strings -n 8 file.bin
```

Kenapa ini penting? Karena flag CTF atau string penting biasanya lebih panjang dari 4 karakter. Menggunakan `-n 8` atau `-n 12` membuat output lebih bersih dan mengurangi noise.

Kebalikannya, untuk mencari string pendek seperti `flag{`:

```bash
strings -n 3 file.bin
```

---
# 5. Flag `-t` (Tampilkan Offset)

```bash
-t <format>
```

menampilkan offset (posisi) string di dalam file.

Format yang tersedia:

```text
-d  → decimal
-o  → octal
-x  → hexadecimal
```

Contoh:

```bash
strings -t x file.bin
```

Output:

```text
2a3f4 secret_string
```

Offset ini sangat berguna dalam forensic karena memberitahu **di mana** sebuah string berada. Kalau string berada di offset yang tidak wajar, itu bisa menjadi clue bahwa ada data tersembunyi atau file yang disisipkan.

Offset juga membantu ketika kamu ingin memeriksa daerah tertentu:

```bash
dd if=file.bin bs=1 skip=$((0x2a3f4)) count=64 | xxd
```

---
# 6. Flag `-e` (Encoding)

Ini flag yang sering dilupakan, padahal sangat penting.

```bash
-e <encoding>
```

`strings` secara default hanya membaca karakter 8-bit (ASCII). Masalahnya, banyak file Windows menyimpan string dalam format UTF-16 (wide string), di mana setiap karakter direpresentasikan oleh 2 byte.

Contoh penggunaannya:

```bash
strings -e l file.bin
```

```text
l  → 16-bit little-endian (UTF-16LE, default untuk Windows)
b  → 16-bit big-endian
S  → 8-bit (default)
```

Kenapa ini penting? Karena executable Windows sering menyimpan pesan dan URL dalam UTF-16LE. Kalau kamu hanya menjalankan `strings` biasa, string penting bisa tidak terlihat sama sekali.

Kombinasi yang sering dipakai untuk file Windows:

```bash
strings -e l malware.exe | grep -i "http"
```

---
# 7. Flag `-a` dan `-f`

```bash
-a
```

atau:

```bash
--all
```

membuat `strings` memindai seluruh file. Secara default, `strings` hanya memindai bagian tertentu dari file objek/binary (section data). Dengan `-a`, seluruh file diperiksa, termasuk bagian yang biasanya dilewati.

```bash
-f
```

atau:

```bash
--print-file-name
```

menampilkan nama file sebelum setiap string. Ini berguna ketika kamu memeriksa banyak file sekaligus:

```bash
strings -f evidence/*.bin
```

Output:

```text
evidence/a.bin: flag_pertama
evidence/b.bin: flag_kedua
```

---
# 8. Flag `-d` dan `-o`

```bash
-d
```

hanya menampilkan string yang berada di bagian data file (bukan bagian kode instruksi). Ini berguna untuk mempersempit hasil.

```bash
-o
```

sama seperti `-t o`, menampilkan offset dalam format octal.

---
# 9. `strings` pada Memory Dump dan Disk Image

Ini bagian yang membuat `strings` menjadi hidden gem di forensic.

Pada memory dump:

```bash
strings -n 8 memory.raw | grep -iE "password|secret|flag"
```

Pada disk image, kamu bisa memindai seluruh image tanpa harus mount:

```bash
strings -n 10 disk.img | grep -iE "http|@|flag"
```

Keuntungan utama `strings` adalah ia **tidak memerlukan filesystem yang sehat**. Selama datanya masih ada di dalam file, string tetap bisa diekstrak, termasuk dari unallocated space dan file yang sudah dihapus.

Inilah mengapa `strings` sering menjadi tool pertama sebelum masuk ke analisis yang lebih dalam.

---
# 10. Keterbatasan `strings`

Penting untuk memahami batasannya:

- String yang di-encode (base64, hex, XOR) tidak akan terbaca langsung.
- Data yang dikompresi atau dienkripsi tidak terlihat.
- File dengan banyak teks (misalnya HTML) menghasilkan banyak noise.
- `strings` tidak bisa membedakan string penting dan tidak penting.

Ketika string tidak terbaca, kita lanjut ke tool lain seperti `xxd`, `binwalk`, atau `bulk_extractor`.

---
# 11. Command yang Perlu Kamu Kuasai

```bash
strings <file>
```

```bash
strings <file> | grep -i flag
```

```bash
strings -n 8 <file>
```

```bash
strings -t x <file>
```

```bash
strings -e l <file> | grep -i http
```

```bash
strings -a -n 8 <file>
```

```bash
strings -f <directory>/*
```
