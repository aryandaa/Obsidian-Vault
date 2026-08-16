#cybersecurity 

Setelah sebelumnya kita belajar bagaimana menemukan filesystem dan file menggunakan `mmls`, `fsstat`, `fls`, `istat`, dan `icat`, sekarang kita akan memperdalam filesystem yang paling penting untuk investigasi Windows, yaitu **NTFS**.

Sebelumnya kamu sudah mengenal NTFS dan MFT secara konsep. Sekarang targetnya berubah. Kita tidak lagi sekadar mengetahui bahwa "NTFS memiliki MFT", tetapi mulai memahami **bagaimana sebuah file direpresentasikan di dalam MFT dan bagaimana informasi tersebut dapat digunakan untuk investigation**.

--- 
# NTFS sebagai sumber evidence

Ketika Windows menyimpan sebuah file seperti:
```text
C:\Users\Alice\Documents\report.docx
```

yang terlihat oleh pengguna hanyalah:
```text
report.docx
```

Tetapi NTFS menyimpan jauh lebih banyak informasi mengenai file tersebut.

Secara sederhana, kita bisa membayangkan:
```text
report.docx
    │
    ├── Filename
    ├── Size
    ├── Timestamps
    ├── Attributes
    ├── Allocation information
    ├── Security information
    └── File content
```

Informasi tersebut kemudian direpresentasikan melalui struktur NTFS, terutama **MFT record dan attributes**.

Karena itu ketika forensic analyst menemukan sebuah file, pertanyaannya tidak berhenti pada:
> "Apa isi file ini?"

Pertanyaannya berkembang menjadi:

> "Bagaimana NTFS mencatat file ini?"

> "Kapan NTFS mencatat aktivitas terhadap file ini?"

> "Apakah file masih allocated?"

> "Di mana data file berada?"

> "Apakah file pernah dihapus?"

> "Apakah ada perbedaan timestamp yang mencurigakan?"

Pertanyaan-pertanyaan tersebut merupakan inti dari NTFS forensic analysis.

---
# Master File Table

Kita mulai dari MFT.

**Master File Table atau MFT** merupakan struktur utama NTFS yang berisi record mengenai file dan directory.

Secara sederhana:
```text
NTFS Volume
      │
      ▼
     MFT
      │
      ├── Record 0
      ├── Record 1
      ├── Record 2
      ├── Record 3
      ├── ...
      └── Record N
```

Setiap record memiliki ukuran yang umumnya **1024 bytes**, walaupun ukuran tersebut merupakan karakteristik konfigurasi NTFS dan bukan sesuatu yang boleh diasumsikan tanpa memeriksa filesystem.

Sebuah MFT record bukan sekadar tempat menyimpan nama file.

MFT record terdiri dari berbagai **attribute**.

Konsep pentingnya adalah:
```text
MFT Record
    │
    ├── $STANDARD_INFORMATION
    ├── $FILE_NAME
    ├── $DATA
    ├── $SECURITY_DESCRIPTOR
    └── Attributes lainnya
```

Tidak semua record memiliki kombinasi attribute yang sama. Directory, file biasa, dan metadata file system memiliki karakteristik masing-masing.

---
# NTFS Attributes

Dalam NTFS, informasi mengenai file disimpan dalam bentuk **attributes**.

Ini konsep yang sangat penting.

Jangan membayangkan MFT seperti tabel sederhana:

```text
filename | size | created | modified
```

Struktur sebenarnya lebih fleksibel.

Secara konseptual:
```text
MFT Record
     │
     ├── Attribute
     │      └── $STANDARD_INFORMATION
     │
     ├── Attribute
     │      └── $FILE_NAME
     │
     └── Attribute
            └── $DATA
```

Setiap attribute memiliki fungsi tertentu.

Dua attribute yang sangat penting untuk forensic adalah:
```text
$STANDARD_INFORMATION
$FILE_NAME
```

dan tentu saja:
```text
$DATA
```

karena `$DATA` berkaitan dengan isi file.

---
# `$STANDARD_INFORMATION`

Attribute pertama yang harus kamu kenal adalah:
```text
$STANDARD_INFORMATION
```

Attribute ini menyimpan berbagai metadata penting mengenai file.

Di antaranya adalah timestamp.

Secara konseptual:
```text
$STANDARD_INFORMATION
        │
        ├── Created
        ├── Modified
        ├── MFT Changed
        └── Accessed
```

Timestamp tersebut sering digunakan dalam forensic timeline.

Kamu mungkin akan menemukan istilah:
```text
MACE
```

atau variasi:
```text
MACB
```

yang digunakan untuk menggambarkan jenis timestamp.

Salah satu model yang sering digunakan adalah:
```text
M = Modified
A = Accessed
C = Changed
B = Birth
```

Namun kamu harus berhati-hati dengan kata **Changed**.

"Changed" tidak selalu berarti isi file berubah.

Dalam konteks forensic filesystem, perubahan metadata atau filesystem record juga dapat menghasilkan perubahan timestamp tertentu.

Karena itu timestamp tidak boleh dibaca secara naif.

---
# `$FILE_NAME`

Attribute berikutnya adalah:
```text
$FILE_NAME
```

Attribute ini berhubungan dengan informasi nama file dan relasi file terhadap directory.

Misalnya:
```text
C:\Users\Alice\Documents\report.docx
```

Filesystem perlu menyimpan informasi yang memungkinkan NTFS mengetahui bahwa:
```text
report.docx
```

berada di:
```text
Documents
```

dan directory tersebut berada di bawah:
```text
Alice
```

Informasi tersebut direpresentasikan melalui struktur filesystem dan `$FILE_NAME`.

Yang menarik dalam forensic adalah timestamp pada `$FILE_NAME` dapat berbeda dengan timestamp pada `$STANDARD_INFORMATION`.

Jadi kita dapat memiliki dua kelompok timestamp:
```text
$STANDARD_INFORMATION
        │
        ├── timestamps

$FILE_NAME
        │
        ├── timestamps
```

Perbedaan tersebut bisa menjadi sangat berguna dalam analisis.

Nanti ketika kita masuk ke **timeline analysis dan timestomping**, konsep ini akan menjadi semakin penting.

---
# Mengapa timestamp bisa berbeda?

Bayangkan kita mempunyai:
```text
$STANDARD_INFORMATION
Created = 2026-08-10
```

sedangkan:

```text
$FILE_NAME
Created = 2026-08-12
```

Jangan langsung berkata:
> "Ini pasti timestomping."

Tidak.

Perbedaan timestamp bisa muncul karena berbagai aktivitas filesystem dan operasi file.

Dalam forensic, perbedaan timestamp adalah **clue**, bukan otomatis conclusion.

Kita perlu melakukan correlation dengan artifact lain.

Misalnya:
```text
MFT
 +
Prefetch
 +
Event Logs
 +
LNK
 +
Browser History
 +
User Activity
```

Jika semuanya mengarah pada aktivitas yang sama, confidence terhadap finding akan meningkat.

Ini kembali ke prinsip yang sudah kamu pelajari:
```text
Artifact
    ↓
Correlation
    ↓
Finding
    ↓
Conclusion
```

---
# `$DATA`

Sekarang kita masuk ke attribute yang berkaitan dengan data file:
```text
$DATA
```

Misalnya:
```text
secret.txt
```

memiliki content:
```text
CASE-01
Suspicious activity
```

Data tersebut dapat direpresentasikan melalui `$DATA`.

Namun ada dua konsep penting yang perlu kamu pahami:
```text
Resident Data
Non-Resident Data
```

Ini salah satu bagian penting dalam NTFS forensic.

---
# Resident Data

Jika data file cukup kecil, data tersebut dapat disimpan **langsung di dalam MFT record**.

Ini disebut:
**Resident Data.**

Secara konseptual:
```text
MFT Record
┌───────────────────────────┐
│ Header                    │
│ $STANDARD_INFORMATION     │
│ $FILE_NAME                │
│ $DATA                     │
│                           │
│ "Hello forensic"          │
└───────────────────────────┘
```

Artinya content file berada langsung di MFT record.

Untuk file kecil, hal ini dapat terjadi karena data memang cukup kecil untuk ditempatkan di record.

Ini menarik untuk forensic karena kita tidak perlu mengikuti data run menuju cluster lain untuk mendapatkan content tersebut.

---
# Non-Resident Data

Kalau data terlalu besar untuk dimasukkan ke MFT record, NTFS menyimpan data di cluster lain.

Ini disebut: **Non-Resident Data.**

Secara konseptual:
```text
MFT Record
    │
    └── $DATA
          │
          ▼
      Data Runs
          │
          ├── Cluster 100
          ├── Cluster 101
          ├── Cluster 102
          └── Cluster 150
```

MFT record menyimpan informasi yang memungkinkan NTFS menemukan lokasi data tersebut.

Informasi tersebut berkaitan dengan **data runs**.

---
# Data Runs

Data runs adalah konsep yang sangat penting untuk memahami bagaimana NTFS mengetahui lokasi physical/logical clusters yang menyimpan content file.

Misalnya secara sederhana sebuah file membutuhkan:
```text
Cluster 100
Cluster 101
Cluster 102
```

NTFS dapat merepresentasikannya sebagai sebuah run:
```text
Start = 100
Length = 3
```

Kemudian jika bagian berikutnya berada jauh:
```text
Cluster 200
Cluster 201
```

maka file dapat memiliki run lain:
```text
Start = 200
Length = 2
```

Sehingga:
```text
File
 │
 ├── Run 1 → 100-102
 │
 └── Run 2 → 200-201
```

Ini berarti sebuah file tidak harus disimpan secara contiguous.

Jika file mengalami fragmentation:
```text
File
 ↓
Cluster 100
Cluster 101
Cluster 500
Cluster 501
Cluster 900
```

filesystem harus menyimpan informasi yang memungkinkan data tersebut direkonstruksi.

Konsep ini nantinya sangat penting ketika kita membahas **deleted file recovery dan file carving**.

---
# Fragmentation

Fragmentation terjadi ketika bagian-bagian file tersebar di berbagai lokasi storage.

Misalnya file:
```text
large-file.bin
```

tidak disimpan seperti:
```text
100
101
102
103
104
```

tetapi:
```text
100
101
500
501
900
```

Filesystem tetap mengetahui bagaimana menyusun kembali data tersebut karena metadata allocation menyimpan informasi lokasi.

Tetapi dalam forensic recovery, fragmentation membuat recovery lebih kompleks.

Kalau kita hanya mengambil:
```text
Cluster 100
Cluster 101
```

kita belum mendapatkan seluruh file.

Kita harus memahami data runs untuk mengetahui bagian berikutnya.

---
# MFT Record dan Deleted File

Sekarang kita kembali ke deleted file.

Misalnya:
```text
secret.txt
```

awalnya memiliki:
```text
MFT Record
     ↓
$STANDARD_INFORMATION
$FILE_NAME
$DATA
```

Kemudian user menghapus file. Filesystem dapat menandai record tersebut sebagai tidak lagi digunakan untuk file aktif.

Tetapi bukan berarti seluruh informasi langsung lenyap.

Secara konseptual:
```text
Before deletion

MFT
 ↓
secret.txt
 ↓
Data

After deletion

MFT
 ↓
Deleted / unallocated entry
 ↓
Data may still exist
```

Selama record dan data belum tertimpa, forensic analyst mungkin masih dapat menemukan informasi yang berkaitan dengan file tersebut.

Namun kemungkinan recovery bergantung pada kondisi evidence.

Jadi:
```text
Deleted ≠ Guaranteed Gone
```

tetapi juga:
```text
Deleted ≠ Guaranteed Recoverable
```

Dua pernyataan tersebut harus selalu kamu pegang.

---
# MFT Entry Number

Setiap MFT record memiliki identifier atau entry number.

Misalnya: 
```text
MFT Entry 42
```

merepresentasikan:
```text
secret.txt
```

Ketika menggunakan tools seperti `fls` dan `istat`, informasi tersebut menjadi penting.

Workflow kita sekarang menjadi lebih jelas:
```text
disk image
    ↓
mmls
    ↓
partition
    ↓
fsstat
    ↓
NTFS
    ↓
fls
    ↓
MFT entry
    ↓
istat
    ↓
MFT metadata
    ↓
icat
    ↓
file content
```

Ini adalah hubungan langsung antara materi **Filesystem Examination** sebelumnya dengan **Advanced NTFS Analysis** yang sedang kita pelajari sekarang.

---
# Kenapa MFT sangat penting dalam forensic?

Karena MFT dapat memberikan informasi yang tidak terlihat hanya dari directory listing biasa.

Misalnya user melihat:
```text
Documents/
└── report.docx
```

Forensic analyst dapat menemukan:
```text
MFT Entry
Filename
Parent Directory
File Size
Timestamps
Allocation Status
Data Runs
Attributes
```

Dengan informasi tersebut, analyst dapat membangun pemahaman yang jauh lebih lengkap mengenai file.

Bahkan ketika file sudah tidak terlihat secara normal, metadata filesystem dapat menjadi sumber evidence.

---
# Hubungan dengan Investigation

Sekarang kita buat skenario kecil.

Misalnya investigator sedang menyelidiki dugaan bahwa seorang user menjalankan:
```text
malware.exe
```

Dari filesystem examination ditemukan:
```text
C:\Users\Alice\Downloads\malware.exe
```

MFT memberikan:
```text
Filename
Timestamp
Size
MFT Entry
Data location
```

Kemudian ditemukan artifact lain:
```text
Prefetch
```

yang menunjukkan execution.

Kemudian ditemukan:
```text
Windows Event Log
```

yang memberikan aktivitas sistem terkait.

Kemudian:
```text
Browser History
```

menunjukkan file tersebut kemungkinan di-download.

Sekarang kita memiliki:
```text
Browser
   ↓
Download

Filesystem
   ↓
malware.exe exists

MFT
   ↓
Metadata

Prefetch
   ↓
Execution

Event Log
   ↓
System activity
```

Barulah kita dapat mulai membangun timeline.

Ini jauh lebih kuat daripada:
> "Saya menemukan malware.exe, berarti user pasti menjalankannya."

Forensic bukan lomba menebak. Kita mencari evidence yang saling menguatkan.

---
Praktik yang akan kita lakukan [Praktek 7](Praktek%207.md)