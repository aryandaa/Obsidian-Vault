#tool 

Setelah `strings` menunjukkan kata-kata yang bisa dibaca, muncul pertanyaan berikutnya: **bagaimana kalau informasi penting justru berada di byte yang tidak bisa dibaca?** Di sinilah `xxd` dan `hexdump` masuk. Keduanya adalah tool untuk melihat file dalam bentuk **hexadecimal**, sehingga kamu bisa membaca byte, offset, dan struktur file secara langsung.

Secara konsep:

```text
File
 ↓
Baca byte
 ↓
Tampilkan sebagai hex + ASCII
 ↓
Kamu melihat struktur sebenarnya
```

Kemampuan ini sangat penting dalam forensic karena banyak struktur data (file signature, partition table, boot sector, header file) hanya bisa dipahami dalam bentuk byte.

---
## 1. Instalasi

`xxd` berasal dari package `xxd` (atau `vim-common` di beberapa distro):

```bash
sudo apt update
sudo apt install xxd
```

`hexdump` berasal dari package `bsdmainutils`:

```bash
sudo apt install bsdmainutils
```

Verifikasi:

```bash
xxd --version
```

```bash
hexdump --version
```

---
# 2. Penggunaan Dasar `xxd`

```bash
xxd file.bin
```

Output default menampilkan tiga bagian:

```text
00000000: 2550 4446 2d31 2e37 0a25 e2e3 cfd3 0a25  %PDF-1.7.%....%
00000010: 3530 204f 626a 0a3c 3c2f 4c65 6e67 7468  50 Obj.<<Length
```

Bagian kiri adalah offset dalam hex, bagian tengah adalah byte dalam hex, dan bagian kanan adalah representasi ASCII.

Untuk melihat byte awal sebuah file:

```bash
xxd -l 64 file.bin
```

`-l` membatasi jumlah byte yang ditampilkan.

Untuk melihat dari offset tertentu:

```bash
xxd -s 0x200 file.bin
```

`-s` (skip) mulai membaca dari offset yang ditentukan.

---
# 3. Penggunaan Dasar `hexdump`

Bentuk yang paling sering dipakai adalah:

```bash
hexdump -C file.bin
```

`-C` adalah mode **canonical**, format yang mirip dengan `xxd`:

```text
00000000  25 50 44 46 2d 31 2e 37  0a 25 e2 e3 cf d3 0a 25  |%PDF-1.7.%....%|
00000010  35 30 20 4f 62 6a 0a 3c  3c 2f 4c 65 6e 67 74 68  |50 Obj.<<Length|
```

Kombinasi yang sering dipakai:

```bash
hexdump -C -n 64 file.bin
```

```bash
hexdump -C -s 512 file.bin
```

---
# 4. Memeriksa Magic Bytes

Sekarang kita hubungkan dengan materi `file`. `file` mengenali tipe file berdasarkan magic signature. Dengan `xxd` atau `hexdump`, kamu bisa melihat magic bytes tersebut secara langsung.

```bash
xxd -l 16 evidence.jpg
```

```text
00000000: ffd8 ffe0 0010 4a46 4946 0001 0100 0001  ......JFIF.....
```

Perhatikan `ffd8 ffe0` di awal. Itu adalah signature JPEG.

Beberapa signature yang harus kamu kenali:

```text
FF D8 FF        JPEG
89 50 4E 47     PNG
25 50 44 46     PDF (%PDF)
50 4B 03 04     ZIP (PK)
7F 45 4C 46     ELF
4D 5A           EXE (MZ)
55 AA           Boot signature MBR
```

Kebiasaan yang baik: setelah `file` memberi tahu tipe file, verifikasi dengan `xxd` untuk melihat signature-nya sendiri.

---
# 5. Mencari Data di Antara Header dan Footer

File carving (yang nanti kita pelajari lewat `foremost` dan `scalpel`) bekerja berdasarkan header dan footer. Dengan `xxd` kamu bisa melihat langsung di mana sebuah file dimulai dan berakhir.

Misalnya kita menemukan data ZIP di tengah file:

```bash
xxd -s 0x4F00 -l 64 file.bin
```

Jika terlihat `50 4B 03 04`, itu adalah awal ZIP. Dari offset tersebut kamu bisa mengekstraknya:

```bash
dd if=file.bin bs=1 skip=$((0x4F00)) of=extracted.zip
```

Ini contoh sederhana manual carving.

---
# 6. Flag `-g` dan `-c` pada `xxd`

```bash
-g <ukuran>
```

mengelompokkan byte. Default `xxd` adalah 2 byte per group. Untuk melihat per byte:

```bash
xxd -g 1 file.bin
```

```bash
-c <jumlah>
```

mengatur jumlah byte per baris. Default 16:

```bash
xxd -c 32 file.bin
```

```
Perhatikan bahwa `hexdump -C` menggunakan group 4 byte, sedangkan `xxd`
default menggunakan group 2 byte. Kebiasaan melihat keduanya akan membuatmu
nyaman membaca byte dalam format apa pun.
```

---
# 7. Flag `-p` dan `-r` (Plain dan Reverse)

Ini kombinasi yang sangat berguna, bahkan termasuk hidden gem.

```bash
-p
```

atau:

```bash
--plain
```

menghasilkan output hex tanpa offset dan tanpa ASCII:

```bash
xxd -p file.bin
```

```text
255044462d312e370a25...
```

Kebalikannya:

```bash
-r
```

atau:

```bash
--revert
```

mengubah hex kembali menjadi binary:

```bash
xxd -r -p hex.txt > file.bin
```

Ini sangat berguna ketika kamu menemukan data hex di dalam teks (misalnya di log atau di file lain) dan ingin mengubahnya menjadi file asli. Contoh:

```bash
xxd -r -p extracted_hex.txt > recovered.bin
```

---
# 8. Flag `-b` (Binary)

```bash
xxd -b file.bin
```

menampilkan byte dalam bentuk biner, bukan hex. Ini jarang dipakai untuk analisis cepat, tetapi berguna untuk memahami struktur bit, misalnya pada flag filesystem atau atribut NTFS.

---
# 9. `hexdump` dan Format Kustom

`hexdump` memiliki kemampuan format yang sangat fleksibel:

```bash
hexdump -e '16/1 "%02x " "\n"' file.bin
```

Ini menampilkan 16 byte per baris dalam hex. Untuk menampilkan dengan offset:

```bash
hexdump -e '"%08_ax: " 16/1 "%02x " "\n"' file.bin
```

Kemampuan format kustom ini berguna ketika kamu membuat pipeline automation untuk membaca struktur binary tertentu.

---
# 10. `xxd` untuk Editing

`xxd` juga bisa digunakan untuk mengedit byte. Pertama ubah file menjadi hex:

```bash
xxd file.bin > file.hex
```

Edit file.hex dengan text editor, lalu ubah kembali:

```bash
xxd -r file.hex > file_new.bin
```

```
Dalam forensic, mengedit evidence asli adalah hal yang dilarang. Gunakan
teknik ini hanya pada salinan kerja (working copy), bukan pada evidence.
```

---
# 11. Posisi `xxd` dan `hexdump` dalam Workflow

```text
file evidence.bin
    ↓
Identifikasi tipe (file)
    ↓
xxd -l 64 evidence.bin
    ↓
Verifikasi signature
    ↓
strings evidence.bin
    ↓
Cari string yang bisa dibaca
    ↓
xxd -s <offset> evidence.bin
    ↓
Periksa daerah menarik
```

`xxd` dan `hexdump` bukan tool untuk mencari flag secara langsung, tetapi mereka adalah **jembatan antara data mentah dan analisis**. Ketika `strings` tidak menemukan apa-apa, biasanya kita kembali ke `xxd` untuk memahami apa yang sebenarnya ada di dalam file.

---
# 12. Command yang Perlu Kamu Kuasai

```bash
xxd <file>
```

```bash
xxd -l 64 <file>
```

```bash
xxd -s 0x200 <file>
```

```bash
xxd -g 1 <file>
```

```bash
xxd -p <file>
```

```bash
xxd -r -p hex.txt > recovered.bin
```

```bash
hexdump -C <file>
```

```bash
hexdump -C -s 512 <file>
```
