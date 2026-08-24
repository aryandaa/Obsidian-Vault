#tool 

Jangan tertipu karena command-nya cuma lima karakter. Dalam digital forensics, `file` adalah salah satu tool yang sangat berguna untuk melakukan **initial triage** terhadap sebuah file. Sebelum investigator membuka, mengeksekusi, mengekstrak, atau menganalisis sebuah file lebih jauh, kita perlu tahu dulu sebenarnya file tersebut apa.

Hal penting yang perlu kamu pahami sejak awal adalah bahwa `file` **tidak percaya begitu saja kepada ekstensi file**. Kalau sebuah file bernama `photo.jpg`, manusia biasanya menganggap itu JPEG. `file` justru memeriksa karakteristik internal file dan mencoba menentukan **file type** berdasarkan data yang ada di dalamnya. Ini penting karena ekstensi dapat dengan mudah diubah.

Misalnya sebuah file sebenarnya adalah executable tetapi diberi nama `document.pdf`. Sistem operasi atau pengguna bisa saja tertipu oleh nama tersebut. Dalam forensic investigation, kita lebih mempercayai struktur internal file daripada sekadar nama yang diberikan kepadanya.

Secara konsep, proses sederhananya seperti ini:
```text
File
 ↓
Baca byte / signature
 ↓
Bandingkan dengan database magic
 ↓
Identifikasi tipe file
 ↓
Tampilkan hasil
```

Di Linux, `file` menggunakan konsep **magic number** atau **file signature** untuk mengenali banyak jenis file. Misalnya JPEG biasanya memiliki signature tertentu pada bagian awal file, begitu juga PNG, PDF, ELF executable, ZIP archive, filesystem image, dan berbagai format lainnya.

---
# 1. Instalasi

Pada Debian, Ubuntu, Kali Linux, dan distro berbasis Debian lainnya, `file` biasanya sudah terinstall secara default.

Coba:
```bash
file --version
```

atau:
```bash
file -v
```

Kalau berhasil, kamu akan mendapatkan informasi versi `file`.

Untuk memastikan binary-nya memang tersedia:
```bash
which file
```

Biasanya akan menghasilkan:
```text
/usr/bin/file
```

Kamu juga bisa menggunakan:
```bash
command -v file
```

Kalau ternyata belum tersedia:
```bash
sudo apt update
sudo apt install file
```

Kemudian verifikasi lagi:
```bash
file --version
```

Untuk pembelajaran kita, jangan cuma memastikan command bisa dijalankan. Biasakan melakukan **verification step** setelah instalasi. Ini kebiasaan kecil yang nanti sangat berguna ketika mulai menggunakan puluhan tool cybersecurity.

---
# 2. Penggunaan Paling Dasar

Syntax paling sederhana adalah:
```bash
file <filename>
```

Contohnya:
```bash
file image.jpg
```

Output bisa terlihat seperti:
```text
image.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), ...
```

Artinya `file` membaca isi file dan menyimpulkan bahwa file tersebut merupakan JPEG.

Sekarang coba file lain:
```bash
file document.pdf
```

Contohnya:
```text
document.pdf: PDF document, version 1.7
```

Atau executable Linux:

```bash
file program
```

Misalnya:
```text
program: ELF 64-bit LSB pie executable, x86-64, ...
```

Perhatikan bahwa `file` tidak sekadar mengatakan:
```text
program: executable
```

Ia dapat memberikan informasi tambahan mengenai struktur binary tersebut.

---
# 3. Mengapa Ekstensi Tidak Bisa Dipercaya?

Sekarang kita masuk ke bagian yang lebih penting untuk forensic.

Misalnya ada file:
```text
evidence.jpg
```

Tetapi ternyata seseorang mengubah nama sebuah PDF menjadi:
```text
evidence.jpg
```

Kalau kamu hanya melihat:
```bash
ls
```

kamu mungkin menganggap itu gambar.

Tetapi:
```bash
file evidence.jpg
```

bisa menghasilkan:
```text
evidence.jpg: PDF document, version 1.7
```

Nah, ini menarik.

Nama file mengatakan:
```text
.jpg
```

Tetapi content mengatakan:
```text
PDF
```

Perbedaan seperti ini disebut sebagai **extension mismatch**.

Dalam forensic investigation, mismatch seperti ini bisa menjadi artifact yang menarik. Bukan berarti otomatis malicious. Bisa saja pengguna hanya salah mengganti nama file. Forensic investigator tidak boleh langsung meloncat dari “aneh” menjadi “tersangka bersalah”, karena manusia memang punya bakat luar biasa untuk menarik kesimpulan dari bukti yang belum cukup.

---
# 4. Melihat Banyak File Sekaligus

Kamu bisa memberikan beberapa file:
```bash
file image.jpg document.pdf archive.zip
```

Output akan menunjukkan informasi masing-masing file.

Kamu juga bisa menggunakan wildcard:
```bash
file *
```

Ini sangat berguna ketika melakukan **initial triage** terhadap satu directory.

Misalnya:
```text
evidence/
├── image.jpg
├── document.pdf
├── payload.exe
├── archive.zip
└── suspicious.txt
```

Kemudian:
```bash
file evidence/*
```

Kamu bisa mendapatkan gambaran awal mengenai isi directory tanpa harus membuka satu per satu.

---
# 5. Flag `-b`

Sekarang kita mulai masuk ke CLI flags.

Flag pertama yang perlu kamu kuasai adalah:
```bash
-b
```

atau:
```bash
--brief
```

Flag ini membuat `file` hanya menampilkan hasil identifikasi tanpa nama file.

Tanpa `-b`:
```bash
file image.jpg
```

hasilnya kira-kira:
```text
image.jpg: JPEG image data, JFIF standard 1.01
```

Dengan:
```bash
file -b image.jpg
```

hasilnya:
```text
JPEG image data, JFIF standard 1.01
```

Ini sangat berguna ketika output `file` akan diproses oleh command lain atau script.

Misalnya:
```bash
type=$(file -b image.jpg)
echo "$type"
```

Sekarang `file` bukan hanya digunakan secara manual, tetapi sudah mulai menjadi bagian dari **automation pipeline**.

---
# 6. Flag `-i`

Flag berikutnya:
```bash
-i
```

atau:
```bash
--mime
```

digunakan untuk menampilkan **MIME type**.

Contohnya:
```bash
file -i image.jpg
```

Output:
```text
image.jpg: image/jpeg; charset=binary
```

Untuk PDF:
```bash
file -i document.pdf
```

bisa menghasilkan:
```text
document.pdf: application/pdf; charset=binary
```

MIME type sering digunakan oleh aplikasi web, HTTP, upload handler, dan sistem operasi untuk mengidentifikasi jenis data.

Dalam web security, konsep ini juga penting karena aplikasi kadang melakukan validasi upload hanya berdasarkan MIME type atau extension. Dan seperti yang mungkin sudah bisa kamu tebak, mempercayai satu indikator saja adalah tradisi manusia yang sering berakhir menjadi vulnerability.

---
# 7. Flag `--mime-type`

Kalau kamu hanya ingin MIME type tanpa charset:
```bash
file --mime-type image.jpg
```

Contohnya:
```text
image.jpg: image/jpeg
```

Ini lebih praktis ketika kita hanya membutuhkan jenis MIME.

---
# 8. Flag `-L`

Sekarang kita masuk ke symbolic link.

Misalnya:
```bash
ln -s image.jpg shortcut
```

Kemudian:
```bash
file shortcut
```

`file` dapat memberikan informasi bahwa `shortcut` adalah symbolic link menuju file tertentu.

Dengan:
```bash
file -L shortcut
```

`file` akan mengikuti symbolic link dan memeriksa **target file**.

Jadi konsepnya:
```text
shortcut
   ↓
symbolic link
   ↓
image.jpg
```

`-L` membuat `file` mengikuti link tersebut.

Dalam forensic analysis, ini relevan karena filesystem memiliki berbagai jenis link dan reference. Investigator perlu mengetahui apakah yang sedang dianalisis adalah file sebenarnya atau hanya reference menuju file lain.

---
# 9. Flag `-h`

Flag:
```bash
-h
```

berkaitan dengan symbolic links dan membuat `file` tidak mengikuti symbolic link.

Ini merupakan behavior yang berlawanan dengan `-L`.

Secara sederhana:
```bash
file -L target
```

berarti:
> Ikuti symbolic link.

Sedangkan:

```bash
file -h target
```

berarti:

> Analisis symbolic link itu sendiri.

---
# 10. Flag `-s` (Block Device)

Salah satu flag yang paling penting dalam forensic tetapi sering terlewat:

```bash
-s
```

atau:

```bash
--special-files
```

Secara default, `file` hanya mau membaca file biasa. Kalau kamu mencoba membaca block device langsung tanpa flag ini, hasilnya sering tidak berguna.

Dengan:

```bash
file -s /dev/sdb
```

`file` membaca block device tersebut secara langsung tanpa harus di-mount terlebih dahulu.

Contoh hasil:

```text
/dev/sdb: DOS/MBR boot sector
```

Ini sangat berguna ketika kamu mendapatkan evidence berupa USB drive atau hard disk fisik. Sebelum melakukan imaging, kamu bisa melakukan triage cepat terhadap device tersebut tanpa menyentuh isinya.

Kombinasi dengan `lsblk`:

```text
lsblk
 ↓
Identifikasi device
 ↓
file -s /dev/sdb
 ↓
Identifikasi awal evidence
```

---
# 11. Flag `-p` (Preserve Date)

Flag ini terlihat sepele, tetapi dalam forensic ia menyimpan konsep penting:

```bash
-p
```

atau:

```bash
--preserve-date
```

Secara default, setiap kali sebuah file dibaca, sistem dapat memperbarui access time (atime) file tersebut. Dalam forensic, kita tidak ingin analisis kita sendiri mengubah metadata evidence.

Dengan:

```bash
file -p evidence.txt
```

`file` berusaha menjaga access time file tetap seperti semula setelah pembacaan.

Ini bagian dari kebiasaan yang lebih besar: **setiap command yang kamu jalankan terhadap evidence harus diminimalkan dampaknya terhadap evidence itu sendiri.**

---
# 12. Flag `-e` (Exclude Test)

Flag:

```bash
-e
```

atau:

```bash
--exclude
```

digunakan untuk menonaktifkan jenis pengujian tertentu.

Misalnya:

```bash
file -e ascii file.bin
```

membuat `file` tidak menjalankan pengujian teks ASCII, sehingga hasilnya lebih fokus pada identifikasi berdasarkan magic/signature.

Contoh penggunaan lain:

```bash
file -e compress file.bin
```

Jenis test yang bisa di-exclude antara lain:

```text
ascii
apptype
compress
elf
soft
text
tokens
```

Flag ini berguna ketika `file` memberikan hasil yang terlalu "ramah" terhadap data yang sebenarnya binary.

---
# 13. Flag `-0` dan `-N` (Automation)

Ketika output `file` akan diproses oleh script, dua flag ini sangat membantu.

```bash
-0
```

atau:

```bash
--print0
```

membuat `file` menambahkan null character setelah nama file, bukan newline. Ini membuat output aman diproses ketika nama file mengandung spasi atau karakter aneh.

```bash
-N
```

atau:

```bash
--no-pad
```

membuat `file` tidak menambahkan padding agar kolom nama file sejajar.

Contohnya:

```bash
file -0 -N evidence/*
```

Output menjadi lebih ramah untuk diproses oleh script atau tool lain.

---

# 14. Flag `-z`

Sekarang masuk ke archive/compression.

Flag:

```bash
-z
```

memungkinkan `file` mencoba melihat ke dalam file compressed.

Contohnya sebuah file:

```text
archive.gz
```

Tanpa `-z`:

```bash
file archive.gz
```

kamu akan mendapatkan informasi bahwa itu gzip compressed data.

Dengan:

```bash
file -z archive.gz
```

`file` dapat mencoba memberikan informasi lebih lanjut mengenai data yang terkompresi tersebut.

Ini berguna ketika melakukan triage terhadap evidence yang dikompresi.

---

# 15. Flag `-k`

Salah satu flag yang menarik untuk forensic adalah:

```bash
-k
```

atau:

```bash
--keep-going
```

Biasanya `file` berhenti setelah menemukan satu kecocokan yang dianggap cukup.

Dengan:

```bash
file -k suspicious.bin
```

`file` mencoba melanjutkan pemeriksaan dan menampilkan beberapa hasil identifikasi jika tersedia.

Ini bisa berguna ketika sebuah file memiliki struktur yang tidak biasa atau terdapat beberapa layer data.

---

# 16. Flag `-f`

Flag:

```bash
-f <file>
```

digunakan untuk membaca daftar filename dari sebuah file.

Misalnya kita punya:

```text
targets.txt
```

isinya:

```text
image.jpg
document.pdf
archive.zip
program
```

Kemudian:

```bash
file -f targets.txt
```

`file` akan melakukan pemeriksaan terhadap file-file tersebut.

Ini mulai menarik ketika kita melakukan forensic triage terhadap banyak evidence.

---

# 17. Flag `-F`

Flag:

```bash
-F <separator>
```

digunakan untuk menentukan separator antara nama file dan hasil identifikasi.

Default-nya biasanya:

```text
filename: result
```

Kamu bisa mengubahnya:

```bash
file -F " => " image.jpg
```

Output:

```text
image.jpg => JPEG image data, ...
```

Flag ini bukan flag yang akan paling sering kamu gunakan dalam forensic sehari-hari, tetapi bagus untuk dipahami karena output formatting akan berguna ketika membuat pipeline automation.

---

# 18. File Signature

Sekarang kita masuk ke bagian yang lebih penting daripada sekadar hafalan flag.

`file` bekerja menggunakan database **magic**.

Kamu bisa melihat lokasi magic database dengan:

```bash
file --version
```

Informasinya dapat menunjukkan lokasi magic file/database yang digunakan.

Kamu juga bisa melihat manual:

```bash
man file
```

dan:

```bash
man 5 magic
```

Magic database berisi pola byte yang digunakan untuk mengidentifikasi tipe file.

Konsep sederhananya:

```text
File
 ↓
Byte awal
 ↓
Magic signature
 ↓
Magic database
 ↓
File type
```

Misalnya secara konseptual:

```text
FF D8 FF ...
```

dapat mengindikasikan JPEG.

PDF biasanya dimulai dengan signature:

```text
25 50 44 46
```

yang jika diterjemahkan ke ASCII menjadi:

```text
%PDF
```

Berikut beberapa magic signature yang paling sering muncul di forensic:

```text
JPEG      FF D8 FF
PNG       89 50 4E 47
GIF       47 49 46 38
PDF       25 50 44 46 (%PDF)
ZIP       50 4B 03 04 (PK)
RAR       52 61 72 21 (Rar!)
ELF       7F 45 4C 46
PE/EXE    4D 5A (MZ)
SQLite    53 51 4C 69 74 65
7Z        37 7A BC AF 27 1C
Boot sig  55 AA (akhir boot sector)
```

Hafalkan beberapa yang paling umum: `FF D8 FF` untuk JPEG, `50 4B` untuk ZIP, `25 50 44 46` untuk PDF, dan `7F 45 4C 46` untuk ELF. Ketika nanti kita masuk file carving, magic signature ini akan menjadi dasar dari tool seperti `foremost`, `scalpel`, dan `binwalk`.

Jadi kamu bisa melihat byte awal sebuah file menggunakan:

```bash
xxd -l 32 image.jpg
```

atau:

```bash
hexdump -C image.jpg | head
```

Di sinilah `file`, `xxd`, dan `hexdump` mulai saling terhubung.

---

# 19. Hubungan `file` dengan Forensic Workflow

Dalam forensic investigation, `file` biasanya bukan tool terakhir.

Ia berada di tahap **initial triage**.

Misalnya kita mendapatkan evidence directory:

```text
evidence/
├── file1.jpg
├── file2.pdf
├── file3.exe
├── file4.bin
└── file5.dat
```

Kita mulai:

```bash
file evidence/*
```

Kemudian menemukan:

```text
file1.jpg: JPEG image data
file2.pdf: PDF document
file3.exe: PE32 executable
file4.bin: Zip archive data
file5.dat: JPEG image data
```

Nah.

`file5.dat` menarik.

Ekstensinya `.dat`, tetapi content-nya ternyata JPEG.

Sekarang investigation bisa dilanjutkan:

```bash
file file5.dat
```

kemudian:

```bash
exiftool file5.dat
```

kemudian:

```bash
xxd file5.dat | head
```

kemudian:

```bash
strings file5.dat
```

Tool-tool tersebut akan kita pelajari setelah `file`, sehingga nanti kamu bisa melihat bagaimana satu tool menghasilkan informasi yang menjadi dasar penggunaan tool berikutnya.

---

# 20. `file` pada Disk Image

Nah, ini penting karena kita sedang belajar **Storage & File System Forensic**.

Misalnya kamu mempunyai:

```text
evidence.img
```

Jangan langsung menganggap:

```text
.img = disk image
```

Gunakan:

```bash
file evidence.img
```

Hasilnya bisa menunjukkan sesuatu seperti:

```text
evidence.img: DOS/MBR boot sector
```

atau informasi filesystem tertentu.

Ini adalah langkah awal untuk mengetahui apa yang sebenarnya ada di dalam file image.

Kalau evidence berupa block device (USB, hard disk fisik), gunakan `-s`:

```bash
file -s /dev/sdb
```

hasilnya bisa menunjukkan boot sector atau filesystem dari device tersebut secara langsung.

Tetapi ingat:

**`file` bukan tool untuk melakukan filesystem analysis secara penuh.**

Kalau hasilnya menunjukkan:

```text
DOS/MBR boot sector
```

itu belum berarti kita sudah mengetahui partition layout.

Untuk itu nanti kita menggunakan:

```bash
mmls
```

Dan setelah mengetahui partition, kita bisa lanjut:

```bash
fsstat
```

kemudian:

```bash
fls
```

dan seterusnya.

Jadi workflow kita mulai terbentuk:

```text
file
 ↓
Identifikasi evidence
 ↓
mmls
 ↓
Partition layout
 ↓
fsstat
 ↓
Filesystem
 ↓
fls
 ↓
Files & directories
```

---

# 21. Command yang Perlu Kamu Kuasai

Untuk tahap Basic, jangan menghafalkan semua option sekaligus. Yang penting kamu benar-benar memahami command berikut:

```bash
file <file>
```

```bash
file -b <file>
```

```bash
file -i <file>
```

```bash
file --mime-type <file>
```

```bash
file -L <file>
```

```bash
file -h <file>
```

```bash
file -z <file>
```

```bash
file -k <file>
```

```bash
file -f <list>
```

```bash
file <directory>/*
```

```bash
file -s /dev/sdb
```

```bash
file -p <file>
```

```bash
file -0 -N <directory>/*
```

Dan untuk forensic triage terhadap disk image:

```bash
file evidence.img
```

Itu jauh lebih penting daripada menghafalkan dua puluh flag lalu lima menit kemudian otak melakukan `rm -rf`.