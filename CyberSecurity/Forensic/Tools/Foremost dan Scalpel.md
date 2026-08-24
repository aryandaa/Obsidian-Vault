#tool 

Sekarang kita masuk ke **file carving**: teknik memulihkan file dari data mentah tanpa menggunakan filesystem sama sekali. `foremost` dan `scalpel` adalah tool carving yang bekerja berdasarkan **signature**: mereka mencari pola byte di awal file (header), lalu menyalin data sampai menemukan footer atau batas tertentu.

Kenapa carving penting? Karena file yang dihapus tidak selalu bisa dipulihkan lewat filesystem. Jika entry metadata sudah ditimpa, satu-satunya cara adalah mencari data mentahnya di unallocated space berdasarkan signature.

```text
Data mentah (image / unallocated space)
    ↓
Cari header (magic bytes)
    ↓
Salin sampai footer
    ↓
File berhasil di-carve
```

---
## 1. Instalasi

```bash
sudo apt update
sudo apt install foremost scalpel
```

Verifikasi:

```bash
foremost -V
```

```bash
scalpel --version
```

---
# 2. Penggunaan Dasar `foremost`

```bash
mkdir output
```

```bash
foremost -i evidence.img -o output/
```

`foremost` akan memindai image dan menaruh hasilnya di directory `output/`, diorganisasi berdasarkan tipe file:

```text
output/
├── jpg/
├── png/
├── pdf/
├── zip/
└── audit.txt
```

`audit.txt` berisi catatan file apa saja yang ditemukan, offsetnya, dan tipe filenya.

Untuk memilih tipe file tertentu:

```bash
foremost -t jpg,pdf -i evidence.img -o output/
```

Untuk mode verbose (melihat prosesnya):

```bash
foremost -v -i evidence.img -o output/
```

---
# 3. Flag Penting `foremost`

```bash
-t <tipe>
```

membatasi tipe file yang dicari: `jpg`, `png`, `gif`, `pdf`, `zip`, `doc`, `avi`, `exe`, dan lainnya.

```bash
-q
```

mode quiet (hanya hasil akhir).

```bash
-v
```

mode verbose.

```bash
-b <ukuran>
```

block size, default 512. Berguna jika data berada pada media dengan sector size berbeda.

```bash
-d
```

mengaktifkan indirect block detection (untuk ext filesystem).

```bash
-c <file>
```

menggunakan file konfigurasi khusus.

```bash
-s <file>
```

menggunakan file seed yang berisi data yang diketahui untuk membantu carving.

---
# 4. File Konfigurasi `foremost`

`foremost` membaca definisi signature dari file konfigurasi `/etc/foremost.conf`. Isinya seperti:

```text
png     y       200     \x89\x50\x4e\x47\x0d\x0a\x1a\x0a
jpg     y       200000  \xff\xd8\xff\xe0
pdf     y       5000000 \x25\x50\x44\x46
zip     y       5000000 \x50\x4b\x03\x04
```

Formatnya:

```text
<ekstensi> <y/n> <ukuran_max> <signature>
```

- `y` berarti carving aktif, `n` nonaktif.
- Ukuran maksimal dalam byte.
- Signature dalam hex escape.

Kamu bisa menambahkan signature kustom:

```text
txt     y       100000  \x46\x4c\x41\x47
```

lalu jalankan:

```bash
foremost -c myforemost.conf -i evidence.img -o output/
```

```
Kemampuan menulis signature sendiri adalah hidden gem foremost.
Kalau ada format file khusus, kamu yang menentukan polanya.
```

---
# 5. Penggunaan Dasar `scalpel`

`scalpel` bekerja dengan prinsip yang sama tetapi implementasinya berbeda. Ia lebih cepat tetapi kurang toleran terhadap file yang terfragmentasi.

Pertama, aktifkan tipe file di file konfigurasi. File konfigurasi `scalpel` berada di `/etc/scalpel/scalpel.conf`. Semua baris di-comment secara default. Uncomment baris yang kamu butuhkan, misalnya:

```text
jpg     y       20000000      \xff\xd8\xff\xe0      \xff\xd9
```

Formatnya:

```text
<ekstensi> <y/n> <ukuran_max> <header> <footer>
```

Perhatikan: `scalpel` bisa mendefinisikan **footer secara eksplisit**, berbeda dengan `foremost` yang mengandalkan struktur file.

Setelah konfigurasi siap:

```bash
scalpel -o output/ evidence.img
```

Untuk menggunakan konfigurasi kustom:

```bash
scalpel -c myscalpel.conf -o output/ evidence.img
```

---
# 6. Carving dari Unallocated Space

Teknik yang lebih tajam: isolasi dulu unallocated space, baru carve di dalamnya.

```bash
blkls -o 2048 evidence.img > unallocated.bin
```

```bash
foremost -i unallocated.bin -o carved/
```

Dengan cara ini, carving fokus pada daerah yang paling mungkin berisi data yang dihapus, tanpa noise dari file yang masih aktif.

---
# 7. Verifikasi Hasil Carving

Hasil carving tidak selalu sempurna. File yang terfragmentasi bisa menghasilkan output yang rusak.

Selalu verifikasi:

```bash
file carved/jpg/*
```

```bash
exiftool carved/jpg/*.jpg
```

Buang file yang rusak atau tidak relevan.

```
Carving menghasilkan kandidat, bukan vonis. Setiap hasil harus
diverifikasi sebelum dijadikan evidence.
```

---
# 8. Kelebihan dan Keterbatasan

Kelebihan carving:

- Tidak membutuhkan filesystem yang sehat.
- Bisa memulihkan file yang metadata-nya sudah hilang.
- Bekerja pada unallocated space, slack space, dan memory dump.

Keterbatasan:

- File terfragmentasi sering gagal di-carve.
- Hasilnya banyak file rusak atau false positive.
- File tanpa signature yang jelas sulit dipulihkan.

Untuk data yang tidak punya signature jelas, kita lanjut ke `binwalk` atau analisis manual dengan `xxd`.

---
# 9. Posisi Carving dalam Workflow

```text
mmls → offset partition
    ↓
fls -d → temukan file yang dihapus
    ↓
icat → coba recovery via metadata
    ↓
blkls → isolasi unallocated space
    ↓
foremost / scalpel → carving
    ↓
file + exiftool → verifikasi hasil
```

Carving adalah pilihan terakhir setelah metode berbasis metadata tidak bisa memulihkan data.

---
# 10. Command yang Perlu Kamu Kuasai

```bash
foremost -i evidence.img -o output/
```

```bash
foremost -t jpg,pdf -i evidence.img -o output/
```

```bash
foremost -c myforemost.conf -i evidence.img -o output/
```

```bash
scalpel -o output/ evidence.img
```

```bash
blkls -o 2048 evidence.img > unallocated.bin
```

```bash
foremost -i unallocated.bin -o carved/
```
