#cybersecurity 

Sampai titik ini kita sudah memahami bagaimana NTFS menyimpan file, bagaimana MFT merepresentasikan file, bagaimana metadata dapat dianalisis, bagaimana artifact NTFS dapat digunakan, dan bagaimana timestamp disusun menjadi timeline. Sekarang kita masuk ke salah satu kemampuan paling penting dalam digital forensics, yaitu memahami **apa yang terjadi terhadap data setelah sebuah file dihapus**.

Banyak pemula memiliki model mental sederhana:
```text
File
 ↓
Delete
 ↓
File hilang
 ↓
Data hilang
```

Dalam filesystem, kenyataannya tidak sesederhana itu.

Ketika sebuah file dihapus, yang berubah pertama-tama adalah bagaimana filesystem memperlakukan file tersebut. Sistem operasi tidak selalu langsung menghancurkan setiap byte data yang sebelumnya digunakan file. Dalam kondisi tertentu, metadata file masih dapat tersisa dan data pada cluster yang sebelumnya digunakan file masih dapat berada di storage.

Secara konseptual:
```text
Before deletion

MFT
 ↓
File Record
 ↓
Data Clusters
```

Kemudian file dihapus:
```text
MFT Record
 ↓
Marked as deleted / no longer active

Data Clusters
 ↓
May still contain previous data
```

Tetapi kata **may** sangat penting. Deleted file recovery bukan sihir. Jika cluster tersebut sudah digunakan kembali dan data lama tertimpa, recovery dapat menjadi tidak mungkin atau hanya menghasilkan data yang rusak.

---
# Apa yang sebenarnya terjadi ketika file dihapus?

Misalnya kita mempunyai:
```text
C:\Evidence\secret.txt
```

File tersebut menggunakan beberapa cluster:
```text
Cluster 100
Cluster 101
Cluster 102
```

Dan MFT memiliki record untuk file tersebut.

Sebelum deletion:
```text
MFT Record
    ↓
secret.txt
    ↓
100 → 101 → 102
```

Kemudian user menjalankan:
```bash
rm secret.txt
```

pada filesystem Linux, atau menghapus file melalui Windows.

Secara konseptual, filesystem sekarang tidak lagi memperlakukan `secret.txt` sebagai file aktif.

Tetapi bisa saja:
```text
Cluster 100
Cluster 101
Cluster 102
```

masih berisi data lama.

Filesystem kemudian dapat menganggap ruang tersebut tersedia untuk digunakan kembali:
```text
Allocated
██████████████

Unallocated
░░░░░░░░░░░░░░
```

Jadi ada perbedaan antara:
```text
File tidak lagi terdaftar sebagai file aktif
```

dan:
```text
Byte fisik sudah benar-benar hilang
```

Keduanya bukan hal yang sama.

---
# Unallocated Space

**Unallocated space** adalah area storage yang saat ini tidak dialokasikan oleh filesystem kepada file aktif.

Misalnya volume memiliki 1000 cluster:
```text
Cluster 0
Cluster 1
Cluster 2
...
Cluster 999
```

Kemudian hanya sebagian yang digunakan:
```text
Allocated:
0 - 700

Unallocated:
701 - 999
```

Bagian `701 - 999` tidak berarti semuanya berisi sampah kosong.

Sebagian mungkin benar-benar berisi zero atau data yang belum pernah digunakan.

Tetapi sebagian lainnya dapat mengandung residual data dari file yang sebelumnya berada di sana.

Misalnya:
```text
secret.txt
     ↓
Cluster 850
Cluster 851
Cluster 852
     ↓
File deleted
     ↓
Clusters become unallocated
```

Jika belum tertimpa:
```text
Cluster 850 → old data
Cluster 851 → old data
Cluster 852 → old data
```

Maka investigator memiliki kemungkinan untuk menemukan kembali sebagian data tersebut.

---
# Deleted File vs Unallocated Data

Ini dua konsep yang harus kamu bedakan.

**Deleted file** berarti filesystem tidak lagi memperlakukan file tersebut sebagai file aktif.

Sedangkan **unallocated data** berarti area storage tersebut tidak sedang dialokasikan kepada file aktif.

Keduanya bisa berhubungan, tetapi tidak identik.

Misalnya:
```text
Deleted File
      ↓
MFT information may remain
      ↓
Data clusters may remain
      ↓
Those clusters become unallocated
```

Namun bisa juga terjadi:
```text
Deleted File
      ↓
MFT information partially overwritten
      ↓
Data clusters still contain residual data
```

Atau:
```text
Deleted File
      ↓
Data clusters reused
      ↓
Original content overwritten
```

Maka recovery menjadi jauh lebih sulit.

---
# Mengapa MFT penting untuk deleted files?

Pada NTFS, MFT merupakan salah satu tempat utama yang kita periksa ketika mencari deleted files.

Misalnya sebelumnya:
```text
MFT Record 42

secret.txt
Size: 12000 bytes
Data:
Cluster 500 → 501 → 502
```

Setelah file dihapus, record tersebut dapat berada dalam kondisi yang menunjukkan bahwa file tidak lagi aktif.

Jika informasi record masih tersedia, investigator mungkin bisa mengetahui:
```text
Filename
File size
Timestamps
Attributes
Data runs
```

Bahkan jika file tidak lagi terlihat melalui directory normal.

Inilah alasan forensic examination tidak cukup hanya membuka File Explorer.

File Explorer menunjukkan apa yang **filesystem saat ini anggap sebagai file aktif**.

Forensic tools dapat turun lebih dalam untuk melihat residual structures.

---
# Deleted Directory Entry

Filesystem juga menyimpan informasi mengenai hubungan antara filename dan directory.

Misalnya:
```text
Evidence
├── report.txt
├── image.jpg
└── secret.txt
```

Setelah:
```text
secret.txt
```

dihapus, directory aktif mungkin menjadi:
```text
Evidence
├── report.txt
└── image.jpg
```

Tetapi residual information yang berkaitan dengan `secret.txt` mungkin masih dapat ditemukan tergantung kondisi filesystem.

Hal ini memberikan investigator kesempatan untuk mengetahui bahwa sebuah file pernah ada walaupun file tersebut tidak lagi terlihat pada directory aktif.

---
# File Recovery

Sekarang kita sampai pada konsep **file recovery**.

Ada dua situasi berbeda.

Pertama, metadata file masih cukup lengkap sehingga kita dapat mengetahui lokasi data file.

Kedua, metadata filesystem sudah tidak cukup untuk menemukan file secara normal, sehingga kita perlu mencari pola data langsung pada storage.

Situasi pertama dapat memanfaatkan filesystem metadata.

Situasi kedua membawa kita menuju **file carving**, yang akan kita pelajari setelah ini.

Secara sederhana:
```text
Deleted File
      ↓
Can filesystem metadata identify it?
      │
      ├── YES
      │     ↓
      │   Recover using metadata
      │
      └── NO
            ↓
        File Carving
```

Ini adalah perbedaan penting.

---
# Unallocated Space Analysis

Dalam forensic image, kita tidak hanya melihat file aktif.

Kita juga dapat memeriksa:
```text
Allocated Space
+
Unallocated Space
```

Karena evidence yang sudah dihapus dapat berada di unallocated area.

Bayangkan sebuah forensic image:
```text
┌───────────────────────────────┐
│ Active Files                  │
├───────────────────────────────┤
│ Filesystem Metadata           │
├───────────────────────────────┤
│ Unallocated Space             │
├───────────────────────────────┤
│ Slack Space                   │
└───────────────────────────────┘
```

Investigator dapat melakukan examination terhadap bagian-bagian tersebut sesuai kebutuhan kasus.

---
# Kenapa unallocated space bisa berisi data?

Karena filesystem biasanya hanya perlu mengetahui apakah suatu ruang tersedia atau tidak.

Misalnya:
```text
Before:

Cluster 100
[SECRET DATA]

After delete:

Cluster 100
[SECRET DATA]
```

Filesystem dapat mengubah status allocation:
```text
Before:
Cluster 100 = allocated

After:
Cluster 100 = unallocated
```

Data tidak otomatis harus berubah menjadi:
```text
[000000000000]
```

Pada titik inilah residual data menjadi menarik.

Tetapi ketika file baru menggunakan cluster tersebut:
```text
Old:
[SECRET DATA]

New:
[PHOTO DATA]
```

Maka sebagian atau seluruh data lama dapat tertimpa.

---
# Overwriting

Ini adalah salah satu faktor utama yang menentukan keberhasilan recovery.

Misalnya:
```text
secret.txt
 ↓
Cluster 100
 ↓
deleted
```

Belum tertimpa:
```text
Cluster 100
[SECRET DATA]
```

Recovery mungkin memungkinkan.

Tetapi kemudian file baru ditulis:
```text
photo.jpg
 ↓
Cluster 100
```

Sekarang:
```text
Cluster 100
[PHOTO DATA]
```

Data lama mungkin sudah hilang.

Jika hanya sebagian cluster yang tertimpa:
```text
Cluster 100
[SECRET][NEW DATA]
```

maka hasil recovery bisa menjadi fragment atau corrupt.

Jadi:
```text
Deleted ≠ Guaranteed Recoverable
```

dan:
```text
Unallocated ≠ Guaranteed Empty
```

Dua kalimat ini perlu kamu ingat.

---
# SSD dan TRIM

Sekarang kita kembali ke perbedaan HDD dan SSD yang sudah kita pelajari sebelumnya.

Pada SSD modern terdapat mekanisme **TRIM**.

Ketika operating system menghapus file, filesystem dapat memberi tahu SSD bahwa block tertentu tidak lagi digunakan.

Secara konseptual:
```text
File deleted
    ↓
Filesystem marks space unused
    ↓
TRIM notification
    ↓
SSD controller
    ↓
Garbage collection / block management
```

Akibatnya, data yang sebelumnya berada di block tersebut bisa menjadi jauh lebih sulit untuk direcover.

Karena itu:
```text
HDD
→ deleted data recovery sering lebih memungkinkan

SSD
→ recovery dapat jauh lebih sulit
```

Tetapi jangan mengubah ini menjadi aturan absolut. Kondisi perangkat, filesystem, controller, TRIM, garbage collection, dan waktu sangat memengaruhi hasil.

---
# File Slack dan Deleted Data

Kita juga perlu menghubungkan materi ini dengan **file slack**.

Misalnya cluster berukuran:
```text
4096 bytes
```

File menggunakan:
```text
3000 bytes
```

Maka terdapat:
```text
1096 bytes
```

yang berada di bagian allocation unit tetapi tidak digunakan oleh file tersebut.

Secara konseptual:
```text
┌──────────────────────────────────────────┐
│ Active File │        Slack               │
│ 3000 bytes  │       1096 bytes           │
└──────────────────────────────────────────┘
```

Slack dapat mengandung residual data tergantung bagaimana storage sebelumnya digunakan.

Jadi dalam forensic storage analysis, kita dapat memiliki beberapa tempat potensial:
```text
Active File
     ↓
File Slack
     ↓
Unallocated Space
     ↓
Deleted File Structures
```

Masing-masing memiliki karakteristik dan teknik examination berbeda.

---
# Mengapa recovery harus dilakukan dari forensic image?

Kita sudah membahas ini sejak awal, dan sekarang alasannya semakin jelas.

Misalnya investigator mendapatkan:
```text
evidence.raw
```

Kemudian ingin mencari deleted files.

Jangan langsung mengubah evidence asli.

Workflow yang lebih aman adalah:
```text
Original Evidence
      ↓
Hash
      ↓
Forensic Image
      ↓
Working Copy
      ↓
Analysis
      ↓
Recovery
```

Jika kita melakukan recovery atau eksperimen pada working copy, evidence asli tetap dipertahankan.

Kemudian hash dapat digunakan untuk memastikan image tidak berubah secara tidak sengaja.

---
# Cara melakukan examination

Tools dari **The Sleuth Kit** yang sudah kamu gunakan sebelumnya kembali menjadi relevan.

Misalnya:
```bash
mmls disk.raw
```

digunakan untuk memahami partition layout.

Kemudian:
```bash
fsstat
```

untuk melihat filesystem information.

Kemudian:
```bash
fls
```

untuk melihat file dan directory entries, termasuk informasi yang berkaitan dengan deleted entries.

Kemudian:
```bash
istat
```

untuk memeriksa metadata sebuah inode atau MFT entry.

Dan:
```bash
icat
```

untuk mengambil data berdasarkan metadata identifier ketika data tersebut masih dapat direkonstruksi.

Jadi workflow kita mulai terlihat:
```text
disk.raw
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
File / Deleted Entry
   ↓
istat
   ↓
Metadata
   ↓
icat
   ↓
Recovery
```

Nanti kita akan memperluasnya dengan pemeriksaan unallocated space dan akhirnya file carving.

---
# Cara berpikir forensic

Misalnya investigator menemukan:
```text
secret.txt
```

dalam deleted entry.

Jangan langsung mengatakan:
> "Saya menemukan file rahasia."

Temuan yang lebih tepat pada tahap awal adalah:
> "Terdapat deleted file entry bernama `secret.txt`."

Kemudian kita periksa:
```text
MFT record
↓
Timestamp
↓
File size
↓
Data runs
↓
Allocated / unallocated state
↓
Recoverable content
```

Jika content berhasil direcover:
```text
secret.txt
↓
Recovered content
↓
Hash
↓
Examination
```

Barulah kita memiliki evidence yang lebih kuat untuk dianalisis.

Ini kembali ke prinsip awal yang sudah kamu pelajari:
```text
Evidence
 ↓
Verification
 ↓
Analysis
 ↓
Correlation
 ↓
Conclusion
```

Bukan:
```text
Found something
 ↓
langsung menyimpulkan
```

Manusia sudah cukup sering melakukan itu dalam kehidupan sehari-hari. Dalam forensic, kita jangan ikut-ikutan.