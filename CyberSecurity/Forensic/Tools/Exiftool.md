#tool 

`exiftool` adalah salah satu hidden gem terbaik dalam forensic. Ia mampu membaca **metadata** dari hampir semua jenis file: gambar, dokumen, PDF, video, audio, bahkan file yang tidak biasa. Metadata sering kali menyimpan informasi yang tidak terlihat di permukaan: kapan file dibuat, aplikasi apa yang membuatnya, perangkat apa yang digunakan, siapa author-nya, bahkan koordinat GPS.

Secara konsep:

```text
File
 ↓
Baca struktur internal
 ↓
Parse tag metadata
 ↓
Tampilkan pasangan key=value
```

Bedanya dengan `file`, `exiftool` jauh lebih dalam. `file` hanya memberi tahu tipe file, sedangkan `exiftool` membedah seluruh metadata yang tersimpan di dalamnya.

---
## 1. Instalasi

```bash
sudo apt update
sudo apt install libimage-exiftool-perl
```

Verifikasi:

```bash
exiftool -ver
```

atau:

```bash
exiftool -v
```

---
# 2. Penggunaan Dasar

```bash
exiftool photo.jpg
```

Output menampilkan banyak tag:

```text
ExifTool Version Number         : 12.40
File Name                       : photo.jpg
File Size                       : 2.4 MB
File Modification Date/Time     : 2026:08:12 01:30:00+07:00
File Access Date/Time           : 2026:08:12 02:15:00+07:00
File Inode Change Date/Time     : 2026:08:12 01:30:00+07:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
Image Width                     : 4032
Image Height                    : 3024
Make                            : Apple
Camera Model Name               : iPhone 14 Pro
Software                        : 16.1
Date/Time Original              : 2026:08:11 22:47:12
GPS Latitude                    : 6 deg 11' 30.00" S
GPS Longitude                   : 106 deg 49' 0.00" E
```

Perhatikan baris-baris menarik: kamera, waktu pengambilan, software, dan koordinat GPS. Semua ini bisa menjadi evidence.

```
Jangan pernah meremehkan metadata. Satu foto bisa menjawab pertanyaan
"di mana", "kapan", "dengan apa", dan "siapa" hanya dari tag yang tersimpan
di dalamnya.
```

---
# 3. Metadata pada Dokumen dan PDF

`exiftool` tidak hanya untuk gambar.

```bash
exiftool document.pdf
```

bisa menampilkan:

```text
Author          : Alice
Creator         : Microsoft Word
Producer        : Microsoft: Word
Create Date     : 2026:07:01 09:12:00
Modify Date     : 2026:07:05 14:30:00
```

Informasi seperti `Author` dan `Producer` sangat berguna untuk menentukan aplikasi dan user yang terlibat dalam pembuatan dokumen.

Untuk dokumen Office:

```bash
exiftool report.docx
```

Untuk file lain, `exiftool` tetap bisa mencoba membaca strukturnya. Coba saja pada berbagai file di evidence directory.

---
# 4. Flag `-a` dan `-u`

Secara default, `exiftool` menyembunyikan beberapa tag yang dianggap tidak penting.

```bash
-a
```

menampilkan semua tag, termasuk tag duplikat atau tag dari semua kelompok.

```bash
-u
```

menampilkan tag yang tidak diketahui (unknown), termasuk tag yang tidak terdaftar dalam database exiftool.

Kombinasi yang paling lengkap:

```bash
exiftool -a -u -g1 file.bin
```

Ini menampilkan semua metadata dengan pengelompokan berdasarkan group. Sangat berguna untuk mencari sesuatu yang tidak biasa.

---
# 5. Flag `-g` (Group)

```bash
-g
```

mengelompokkan output berdasarkan asal metadata:

```text
[ExifTool]      ExifTool Version Number : 12.40
[File]          File Name               : photo.jpg
[EXIF]          Date/Time Original      : 2026:08:11 22:47:12
[GPS]           GPS Latitude            : 6 deg 11' 30.00" S
[Composite]     GPS Position            : 6 deg 11' 30.00" S, 106 deg 49' 0.00" E
```

```
[System]        File Modification Date/Time : ...
```

Dengan `-g`, kamu bisa memahami metadata berasal dari bagian file mana. Dalam forensic, membedakan metadata filesystem dan metadata internal file itu penting.

---
# 6. Flag `-j` dan `-csv` (Output Terstruktur)

Ketika jumlah file banyak, output biasa sulit dibaca.

```bash
exiftool -j directory/
```

menghasilkan output JSON, yang bisa diproses dengan `jq` atau Python.

```bash
exiftool -csv directory/ > metadata.csv
```

menghasilkan tabel CSV yang bisa dibuka di spreadsheet.

Ini sangat berguna ketika kamu ingin membandingkan metadata dari banyak file sekaligus.

---
# 7. Flag `-r` dan `-ext`

```bash
-r
```

membaca secara rekursif ke dalam subdirectory.

```bash
-exif
```

hanya menampilkan tag tertentu.

Contoh kombinasi:

```bash
exiftool -r -csv evidence/ > all_metadata.csv
```

```bash
exiftool -r -ext jpg -ext png evidence/
```

hanya memproses file dengan ekstensi tertentu.

---
# 8. Mencari Tag Tertentu

Kamu bisa langsung menampilkan tag spesifik:

```bash
exiftool -CreateDate -GPSPosition photo.jpg
```

```bash
exiftool -Author document.pdf
```

Untuk mencari semua file dengan tag tertentu di dalam directory:

```bash
exiftool -if '$GPSPosition' -r evidence/
```

Hanya file yang memiliki GPS yang akan muncul. Ini pola yang sangat berguna untuk triage.

---
# 9. Flag `-T` (Terse)

```bash
-T
```

menghasilkan output ringkas tanpa nama tag:

```bash
exiftool -T -CreateDate -GPSPosition photo.jpg
```

```text
2026:08:11 22:47:12  6 deg 11' 30.00" S, 106 deg 49' 0.00" E
```

Ini bagus untuk pipeline automation.

---
# 10. Metadata sebagai Artefak Investigasi

Sekarang kita hubungkan dengan konsep evidence, artifact, dan finding.

Kamu menemukan `invoice.pdf`. Sendirian, file itu belum berarti apa-apa. Tetapi `exiftool` menunjukkan:

```text
Author      : bobby
Create Date : 2026:08:12 02:14:00
Producer    : Microsoft: Macintosh
```

Sekarang kamu punya artifact: file dibuat oleh user `bobby` menggunakan aplikasi Mac pada pukul 02:14.

Kemudian kamu korelasikan dengan evidence lain: Prefetch menunjukkan aplikasi tertentu dijalankan pukul 02:15, dan browser history menunjukkan download pada pukul 02:13. Semua mulai membentuk timeline.

```
Metadata adalah clue, bukan vonis. Tetapi tanpa metadata, banyak investigasi
harus dimulai dari nol.
```

---
# 11. Peringatan: `exiftool` Bisa Mengubah File

Hati-hati. `exiftool` juga bisa menulis metadata.

```bash
exiftool -Comment="isi baru" file.jpg
```

mengubah metadata, dan:

```bash
exiftool -all= file.jpg
```

menghapus semua metadata.

Dalam forensic, **jangan pernah menjalankan perintah penulisan terhadap evidence asli**. Kalau kamu benar-benar perlu menguji, gunakan salinan kerja.

Untuk analisis read-only, cukup gunakan perintah pembacaan seperti yang sudah kita bahas.

---
# 12. Posisi `exiftool` dalam Workflow

```text
file evidence.jpg
    ↓
exiftool evidence.jpg
    ↓
Metadata: author, waktu, GPS, aplikasi
    ↓
Korelasi dengan artifact lain
    ↓
Timeline dan finding
```

`exiftool` berada di tahap setelah identifikasi tipe file, sebelum analisis isi. Ia menjawab pertanyaan tentang **asal-usul file**, bukan isinya.

---
# 13. Command yang Perlu Kamu Kuasai

```bash
exiftool <file>
```

```bash
exiftool -a -u -g1 <file>
```

```bash
exiftool -CreateDate -GPSPosition <file>
```

```bash
exiftool -r -csv <directory>/ > metadata.csv
```

```bash
exiftool -j <directory>/
```

```bash
exiftool -T -CreateDate <file>
```

```bash
exiftool -if '$GPSPosition' -r <directory>/
```
