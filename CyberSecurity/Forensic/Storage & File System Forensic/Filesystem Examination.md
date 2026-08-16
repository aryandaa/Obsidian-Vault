#cybersecurity 

Filesystem examination adalah proses memeriksa struktur dan metadata filesystem yang terdapat di dalam forensic image untuk menemukan informasi yang relevan terhadap investigation.

Sebelumnya kita sudah belajar bahwa sebuah storage secara konseptual memiliki struktur:
```text
Disk Image
    ↓
Partition
    ↓
Volume
    ↓
Filesystem
    ↓
Directories
    ↓
Files
    ↓
Artifacts
```

Sampai materi partition table, kita baru berada di bagian:
```text
Disk Image
    ↓
Partition Table
    ↓
Partition
```

Sekarang kita akan turun satu tingkat lebih dalam:
```text
Partition
    ↓
Filesystem
    ↓
Filesystem Structures
    ↓
Files
    ↓
Metadata
```

Inilah yang disebut **filesystem examination**.

Tujuannya bukan sekadar mencari file dengan nama mencurigakan. Kita ingin memahami bagaimana filesystem merepresentasikan data tersebut, di mana file berada, bagaimana metadata-nya tercatat, apakah file masih aktif atau sudah dihapus, dan bagaimana kita dapat mengambil data tersebut tanpa bergantung sepenuhnya pada GUI.

---
## Kenapa kita perlu Filesystem Examination?

Bayangkan kamu mendapatkan:
```text
challenge.E01
```

Kemudian kamu membuka Autopsy dan melihat:
```text
Users
Documents
Downloads
Desktop
```

Kelihatannya mudah, Tetapi bagaimana kalau Autopsy tidak menampilkan file yang kamu cari?
Atau filesystem mengalami kerusakan?
Atau file tersebut sudah dihapus?
Atau challenge memang sengaja menyembunyikan sesuatu di unallocated space?
Atau kamu perlu mengetahui metadata sebuah file secara manual?

Di situ pemahaman filesystem menjadi sangat penting.

Forensic analyst harus mampu turun ke level yang lebih rendah:
```text
Disk Image
    ↓
Partition
    ↓
Filesystem
    ↓
Metadata
    ↓
File Record
    ↓
Data
```

Jadi tool bukan pengganti pemahaman. Tool hanya membantu kita membaca evidence.

---
# The Sleuth Kit

Untuk mulai melakukan filesystem examination, kita akan menggunakan **The Sleuth Kit**, atau biasa disingkat **TSK**.

The Sleuth Kit adalah kumpulan command-line tools untuk melakukan analisis filesystem dan disk image.

Beberapa command penting yang akan kita gunakan adalah:
```text
mmls
fsstat
fls
istat
icat
```

Kamu sebenarnya sudah menggunakan:
```bash
mmls
```

pada materi partition sebelumnya.

`mmls` digunakan untuk melihat struktur partition pada sebuah disk image. Sekarang kita akan melanjutkan dari hasil tersebut.

Secara sederhana:
```text
mmls
  ↓
Partition

fsstat
  ↓
Filesystem

fls
  ↓
Files / Directories

istat
  ↓
File Metadata

icat
  ↓
File Content
```

Perhatikan pola tersebut.

`mmls` membantu kita menemukan **di mana partition berada**.

`fsstat` membantu kita memahami **filesystem di dalam partition**.

`fls` membantu kita melihat **file dan directory**.

`istat` membantu kita melihat **metadata sebuah filesystem entry**.

`icat` membantu kita mengambil **isi file berdasarkan inode atau metadata address**.

Jadi kelima tool tersebut sebenarnya membentuk satu workflow.

---
# 1. `fsstat`

Setelah mengetahui partition menggunakan:
```bash
mmls disk.raw
```

kita perlu mengetahui filesystem yang berada di partition tersebut.

Di sinilah:
```bash
fsstat
```
digunakan.

Misalnya kita mempunyai filesystem NTFS pada partition tertentu. Kita bisa memberikan offset partition kepada `fsstat`.

Secara konseptual:
```bash
fsstat -o <partition_offset> disk.raw
```

Nilai `<partition_offset>` berasal dari informasi partition yang sebelumnya kita dapatkan dari `mmls`.

Misalnya:
```text
Start LBA = 2048
Sector Size = 512
```

maka:
```text
2048 × 512
= 1048576 bytes
```

Tetapi ada satu detail penting yang perlu kamu biasakan dari sekarang.

Tool seperti Sleuth Kit sering menggunakan **sector offset**, bukan byte offset, sehingga penggunaan parameter `-o` harus mengikuti konteks command tersebut.

Misalnya kalau partition dimulai pada sector:
```text
2048
```

kita dapat menggunakan:
```bash
fsstat -o 2048 disk.raw
```

Bukan otomatis:
```bash
fsstat -o 1048576 disk.raw
```

Karena `1048576` merupakan byte offset, sedangkan Sleuth Kit pada konteks ini bekerja dengan sektor.

Ini alasan kita sebelumnya belajar LBA dan offset. Sekarang konsep tersebut mulai benar-benar digunakan.

---
# Apa yang diberikan `fsstat`?

Ketika kita menjalankan `fsstat`, kita ingin mengetahui karakteristik filesystem.

Informasinya dapat mencakup hal-hal seperti:
```text
Filesystem Type
Block Size
Cluster information
Metadata structures
Allocation information
Filesystem statistics
```

Untuk filesystem tertentu, output-nya akan berbeda karena setiap filesystem mempunyai struktur internal yang berbeda.

Misalnya:
```text
NTFS
```

akan mempunyai informasi yang berkaitan dengan struktur NTFS.

Sedangkan:
```text
ext4
```

memiliki struktur yang berkaitan dengan inode, block group, dan metadata ext filesystem.

Jadi `fsstat` membantu kita menjawab:
> "Filesystem apa yang sedang kita analisis dan bagaimana karakteristik internalnya?"

---
# 2. `fls`

Setelah filesystem berhasil dikenali, kita ingin melihat isinya.

Di sinilah kita menggunakan:
```bash
fls
```

`fls` digunakan untuk menampilkan file dan directory yang terdapat dalam filesystem.

Misalnya:
```bash
fls -o 2048 disk.raw
```

Output sederhananya bisa terlihat seperti:
```text
d/d 11:  Documents
d/d 12:  Downloads
r/r 15:  notes.txt
r/r 16:  report.pdf
```

Format sebenarnya dapat berbeda tergantung filesystem dan opsi yang digunakan, tetapi secara konsep kamu akan melihat informasi seperti:
```text
Type
Metadata Address
Filename
```

Bagian yang sangat penting adalah **metadata address**.

Misalnya:
```text
15: notes.txt
```

Angka:
```text
15
```

dapat menjadi identifier filesystem entry yang nantinya kita gunakan untuk pemeriksaan lebih lanjut.

Jadi sekarang workflow mulai menjadi:
```text
fls
 ↓
notes.txt
 ↓
Metadata Address = 15
```

Kemudian:
```text
15
 ↓
istat
```

untuk melihat metadata.

Dan jika ingin mengambil isi:
```text
15
 ↓
icat
```

untuk mengambil content.

---
# Deleted Files

Ada satu kemampuan `fls` yang sangat penting untuk forensic.

Filesystem tidak hanya berisi file yang masih aktif.

Kita juga ingin mengetahui file yang sudah dihapus.

Untuk itu `fls` memiliki opsi:
```bash
-d
```

yang digunakan untuk menampilkan deleted entries.

Misalnya:
```bash
fls -d -o 2048 disk.raw
```

Sekarang kita mulai bisa menemukan sesuatu seperti:
```text
r/r * 25: deleted.txt
```

Tanda tertentu pada output dapat menunjukkan status entry, tergantung filesystem dan versi tool.

Yang penting untuk sekarang adalah konsepnya:
```text
Active Files
      +
Deleted Entries
```

bisa diperiksa dari filesystem metadata.

Ini penting karena user mungkin sudah menghapus file dari Windows, tetapi metadata filesystem atau data terkaitnya belum tentu langsung hilang.

---
# Recursive Listing

Directory filesystem tentu tidak cuma satu level.

Misalnya:
```text
Users/
└── Alice/
    ├── Documents/
    │   ├── report.docx
    │   └── secret.txt
    └── Downloads/
        └── malware.zip
```

Kalau hanya melihat root directory, kamu belum melihat seluruh struktur.

`fls` dapat digunakan secara recursive menggunakan:
```bash
-r
```

Misalnya:
```bash
fls -r -o 2048 disk.raw
```

Sekarang kita dapat melihat struktur directory yang lebih dalam.

Secara konsep:
```text
fls
 ↓
Root
 ↓
Users
 ↓
Alice
 ├── Documents
 │    ├── report.docx
 │    └── secret.txt
 └── Downloads
      └── malware.zip
```

Ini mulai sangat berguna dalam forensic investigation karena kita bisa melakukan enumeration terhadap filesystem tanpa membuka file satu per satu secara manual.

---
# 3. `istat`

Sekarang kita sudah mendapatkan sebuah metadata address.

Misalnya:
```text
15: secret.txt
```

Kita ingin mengetahui informasi lebih detail mengenai file tersebut.

Gunakan:
```bash
istat
```

Contohnya secara konsep:
```bash
istat -o 2048 disk.raw 15
```

`istat` digunakan untuk melihat informasi metadata filesystem entry.

Untuk NTFS, informasi yang ditampilkan dapat berkaitan dengan MFT entry dan atribut yang tersedia.

Misalnya kita bisa menemukan informasi seperti:
```text
File Name
Allocated
Size
MACB timestamps
Metadata address
Data runs
Attributes
```

Nah, di sinilah materi **NTFS dan MFT** yang kamu pelajari sebelumnya mulai benar-benar dipakai.

Sebelumnya kamu belajar:
```text
MFT
 ↓
File Record
 ↓
Metadata
```

Sekarang:
```text
fls
 ↓
MFT entry
 ↓
istat
 ↓
Metadata analysis
```

Jadi materi lama bukan teori yang mengambang. Sekarang dia mulai masuk ke workflow investigation.

---
# MACB Timestamp

Salah satu informasi penting yang sering kita lihat dalam filesystem forensic adalah timestamp.

Istilah **MACB** biasanya digunakan untuk menggambarkan beberapa jenis aktivitas timestamp:
```text
M = Modified
A = Accessed
C = Changed
B = Birth
```

Konsep ini akan menjadi sangat penting ketika kita nanti masuk ke **Timeline Analysis**.

Misalnya kita menemukan:
```text
secret.txt
Created: 2026-08-10
Modified: 2026-08-11
Accessed: 2026-08-12
```

Jangan langsung membuat kesimpulan:
> "Berarti user membuat file tanggal 10."

Timestamp adalah evidence yang harus dikorelasikan dengan artifact lain.

Misalnya:
```text
MFT timestamp
+
Windows Event Log
+
Prefetch
+
Browser history
+
LNK
```

Baru kita dapat membangun timeline yang lebih kuat.

Untuk sekarang cukup pahami bahwa filesystem menyimpan timestamp dan timestamp tersebut merupakan salah satu sumber evidence.

--- 
# 4. `icat`

Sekarang kita sudah mengetahui:

```text
File = secret.txt
Metadata Address = 15
```

Kita ingin mengambil isi file tersebut.

Di sinilah:
```bash
icat
```

digunakan.

Secara konsep:
```bash
icat -o 2048 disk.raw 15
```

Command tersebut mencoba membaca content yang terkait dengan metadata address tersebut.

Kalau file berisi:
```text
This is secret evidence.
```

maka output-nya dapat berupa:
```text
This is secret evidence.
```

Kita juga dapat mengarahkan output ke file:
```bash
icat -o 2048 disk.raw 15 > recovered.txt
```

Sekarang:
```text
Filesystem
    ↓
Metadata Entry
    ↓
icat
    ↓
Recovered Content
```

Ini sangat berbeda dengan:
```bash
cp secret.txt recovered.txt
```

Karena kita tidak sedang meminta operating system untuk membuka file aktif melalui filesystem biasa.

Kita sedang mengambil data melalui **forensic filesystem analysis**.

---
# Mengapa ini penting untuk Deleted Files?

Bagian yang menarik muncul ketika file sudah dihapus.

Misalnya:
```text
secret.txt
```

dihapus oleh user.

File tersebut mungkin tidak lagi muncul sebagai file aktif dalam operating system. Namun forensic examination dapat menemukan metadata entry yang berkaitan dengannya.

Kemudian kita dapat mencoba melakukan recovery berdasarkan metadata tersebut.

Secara konseptual:
```text
Deleted File
     ↓
Filesystem Metadata
     ↓
Metadata Address
     ↓
icat
     ↓
Recovered Content
```

Tetapi recovery tidak selalu berhasil.

Jika data sudah tertimpa:
```text
Old Data
   ↓
Deleted
   ↓
New Data overwrites blocks
   ↓
Old content unavailable
```

maka `icat` mungkin tidak dapat mengembalikan isi file secara utuh.

Ini nanti akan membawa kita ke materi **File Recovery dan File Carving**.

---
# Metadata vs Content

Ini adalah konsep yang perlu kamu tanamkan sekarang.

Sebuah file forensic memiliki setidaknya dua hal yang harus kita bedakan:
```text
Metadata
    +
Content
```

Metadata dapat memberi tahu:
```text
Nama
Ukuran
Timestamp
Allocation
Filesystem reference
```

Content adalah:
```text
Isi sebenarnya dari file
```

Misalnya:
```text
secret.txt
```

Metadata:
```text
Size = 128 bytes
Created = ...
Modified = ...
MFT Entry = 42
```

Content:
```text
CASE-01
Suspicious activity detected
```

Dalam forensic, metadata dan content sama-sama penting.

Kadang content sudah hilang tetapi metadata masih tersedia.

Kadang metadata sudah rusak tetapi sebagian content masih dapat ditemukan melalui carving.

Karena itu forensic examination tidak boleh hanya berfokus pada satu sumber.

---
# Workflow Filesystem Examination

Sekarang kita gabungkan semuanya.

Misalnya kita mendapatkan:
```text
challenge.raw
```

Langkah awal:
```bash
mmls challenge.raw
```

Kita menemukan:
```text
Partition Start = 2048
```

Kemudian:
```bash
fsstat -o 2048 challenge.raw
```

Kita mengetahui filesystem.

Kemudian:
```bash
fls -r -o 2048 challenge.raw
```

Kita mendapatkan daftar file.

Misalnya:
```text
15: report.txt
16: secret.zip
17: suspicious.exe
```

Kemudian kita memilih:
```text
17: suspicious.exe
```

Kita periksa metadata:
```bash
istat -o 2048 challenge.raw 17
```

Kemudian jika ingin mengambil content:
```bash
icat -o 2048 challenge.raw 17 > suspicious.exe
```

Workflow-nya:
```text
Disk Image
     ↓
mmls
     ↓
Partition
     ↓
fsstat
     ↓
Filesystem
     ↓
fls
     ↓
File / Directory
     ↓
istat
     ↓
Metadata
     ↓
icat
     ↓
File Content
```

Nah. Ini adalah salah satu workflow inti yang akan sering kamu gunakan dalam Digital Forensics.

---
Praktik berikutnya : [Praktek 6](Praktek%206.md)
