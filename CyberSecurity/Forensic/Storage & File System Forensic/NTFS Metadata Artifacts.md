#latihan 

Sampai titik ini kamu sudah memahami bahwa NTFS tidak hanya menyimpan file, tetapi juga meninggalkan berbagai metadata. Kita sudah membahas MFT, `$STANDARD_INFORMATION`, `$FILE_NAME`, `$DATA`, resident dan non-resident data, data runs, fragmentation, serta bagaimana deleted file masih mungkin meninggalkan jejak.

Sekarang kita akan memperluas cara berpikir tersebut.

Bayangkan investigator menemukan sebuah file:
```text
C:\Users\Alice\Downloads\suspicious.exe
```

MFT dapat memberi tahu bahwa file tersebut pernah ada dan memberikan berbagai metadata. Tetapi ada pertanyaan yang belum bisa dijawab sepenuhnya hanya dengan MFT:

> Apakah file tersebut pernah dibuat lalu dihapus?

> Apakah file tersebut pernah diganti namanya?

> Apakah file tersebut dipindahkan?

> Apakah ada perubahan lain terhadap filesystem yang terjadi setelah file dibuat?

> Kapan filesystem mencatat perubahan tersebut?

Untuk menjawab pertanyaan seperti ini, kita membutuhkan **NTFS metadata artifacts** lainnya.

Beberapa artifact penting yang akan kita pelajari adalah:
```text
MFT
$UsnJrnl
$LogFile
$Bitmap
$Boot
$Secure
```

Masing-masing memiliki fungsi berbeda. Jangan menganggap semuanya sebagai "log aktivitas", karena struktur dan tujuan masing-masing berbeda.

---
# `$UsnJrnl`

Artifact pertama yang akan kita pelajari adalah:
```text
$UsnJrnl
```

Nama lengkapnya:
**NTFS Update Sequence Number Journal**

atau sering disebut **USN Journal**.

USN Journal merupakan mekanisme NTFS untuk mencatat perubahan terhadap file dan directory pada volume.

Secara sederhana, kita dapat membayangkannya seperti:
```text
File Activity
     ↓
NTFS
     ↓
USN Journal
     ↓
Record perubahan
```

Misalnya user membuat:
```text
secret.txt
```

Kemudian mengganti namanya menjadi:
```text
secret-old.txt
```

Kemudian menghapusnya.

MFT mungkin memberikan informasi mengenai kondisi filesystem dan metadata file, tetapi USN Journal dapat memberikan jejak perubahan yang lebih berorientasi pada **peristiwa perubahan filesystem**.

Secara konseptual:
```text
Create
   ↓
Rename
   ↓
Modify
   ↓
Delete
```

USN Journal dapat menyimpan record yang berkaitan dengan aktivitas tersebut.

---
# Mengapa USN Journal penting?

Misalnya kita hanya melihat filesystem saat ini.

Kita menemukan:
```text
Documents/
└── report.txt
```

Tetapi investigator menduga sebelumnya ada file:

```text
secret.txt
```

yang kemudian dihapus.

Kalau entry aktifnya sudah tidak ada, kita membutuhkan artifact lain.

USN Journal dapat menjadi salah satu sumber informasi untuk mengetahui bahwa pernah terjadi perubahan terhadap filesystem.

Misalnya secara konseptual:
```text
USN Journal

secret.txt
   ↓
FILE_CREATE

secret.txt
   ↓
DATA_EXTEND

secret.txt
   ↓
FILE_DELETE
```

Jadi USN Journal dapat membantu menjawab:
> "Apa yang terjadi terhadap file tersebut?"

Ini berbeda dengan pertanyaan:
> "Apa kondisi file tersebut sekarang?"

Perbedaan tersebut sangat penting dalam forensic.

---
# USN Record

USN Journal terdiri dari record.

Sebuah record dapat berisi informasi seperti:
```text
File Reference Number
Parent File Reference Number
USN
Timestamp
Reason
Source Information
Security ID
Filename
Filename Length
```

Tidak perlu menghafalkan semuanya sekarang. Yang penting kamu memahami konsepnya.

Misalnya:
```text
USN Record
├── File Reference
├── Parent Reference
├── Timestamp
├── Reason
└── Filename
```

Bagian **Reason** sangat menarik karena menunjukkan alasan mengapa record tersebut dibuat.

Misalnya terdapat reason yang berkaitan dengan:
```text
FILE_CREATE
FILE_DELETE
RENAME_OLD_NAME
RENAME_NEW_NAME
DATA_EXTEND
DATA_OVERWRITE
BASIC_INFO_CHANGE
```

Nama dan representasi flag dapat berbeda tergantung tool yang digunakan, tetapi konsepnya sama: **record tersebut memberi konteks mengenai perubahan filesystem.**

---
# Contoh Investigation

Bayangkan kita menemukan:
```text
C:\Users\Alice\Downloads\invoice.pdf
```

Kemudian ditemukan indikasi bahwa file tersebut mencurigakan.

MFT menunjukkan:
```text
invoice.pdf
Created: ...
Modified: ...
```

Tetapi kita ingin mengetahui apakah file tersebut pernah berganti nama.

USN Journal dapat memberikan pola seperti:
```text
invoice.tmp
    ↓
RENAME_OLD_NAME

invoice.pdf
    ↓
RENAME_NEW_NAME
```

Sekarang kita memiliki informasi tambahan:
```text
invoice.tmp
      ↓
rename
      ↓
invoice.pdf
```

Ini jauh lebih berguna dibanding hanya melihat nama file saat ini.

---
# USN Journal dan Deleted Files

Sekarang hubungkan dengan Praktik 6.

Kita sebelumnya membuat:
```text
deleted-evidence.txt
```

kemudian:
```text
rm deleted-evidence.txt
```

MFT dapat memberikan indikasi mengenai deleted entry.

Tetapi USN Journal berpotensi memberikan informasi mengenai aktivitas deletion tersebut.

Secara konseptual:
```text
deleted-evidence.txt
       │
       ├── MFT
       │     ↓
       │   metadata
       │
       └── USN Journal
             ↓
          deletion event
```

Jadi kedua artifact tersebut dapat digunakan bersama.

Ini adalah pola penting dalam digital forensics:
```text
Artifact A
    +
Artifact B
    ↓
Correlation
    ↓
Stronger Finding
```

---
# `$LogFile`

Artifact berikutnya adalah:
```text
$LogFile
```

Kalau USN Journal lebih mudah dipahami sebagai catatan mengenai **perubahan filesystem**, `$LogFile` berhubungan dengan **NTFS transaction logging**.

NTFS menggunakan logging untuk membantu menjaga konsistensi filesystem ketika terjadi operasi.

Secara sederhana:
```text
Filesystem Operation
       ↓
NTFS Transaction
       ↓
$LogFile
```

Misalnya filesystem sedang melakukan operasi metadata.

Jika terjadi gangguan seperti:
```text
Power loss
System crash
```

filesystem dapat menggunakan informasi transaction logging untuk membantu recovery dan menjaga konsistensi struktur filesystem.

---
# `$LogFile` bukan sekadar activity log

Ini penting.

Jangan menyamakan:
```text
$LogFile
```

dengan:
```text
Windows Event Log
```

atau:
```text
USN Journal
```

Ketiganya memiliki tujuan berbeda.

Secara sederhana:
```text
USN Journal
→ perubahan file/directory

$LogFile
→ transaction/logging internal NTFS

Windows Event Log
→ event yang dicatat oleh Windows dan aplikasi
```

Karena itu ketika melakukan forensic investigation, kita harus memahami **konteks artifact**, bukan hanya mencari semua file yang namanya mengandung kata "log".

Manusia memang suka menamai sesuatu "log" lalu membuat analyst sepuluh tahun kemudian menyesal.

---
# `$Bitmap`

Artifact berikutnya:
```text
$Bitmap
```

`$Bitmap` berkaitan dengan status allocation cluster pada NTFS.

Kita sebelumnya sudah mempelajari:
```text
Allocated
Unallocated
```

Sekarang kita melihat bagaimana NTFS mempertahankan informasi tersebut.

Secara konseptual:
```text
$Bitmap

Cluster 0 → allocated
Cluster 1 → allocated
Cluster 2 → free
Cluster 3 → allocated
Cluster 4 → free
```

Sehingga:
```text
Cluster
0  1  2  3  4
A  A  F  A  F
```

`A`:
```text
Allocated
```

`F`:
```text
Free
```

Informasi allocation seperti ini penting ketika menganalisis:

```text
Deleted files
Unallocated space
File recovery
Filesystem consistency
```

---
# Hubungan `$Bitmap` dengan Deleted File

Misalnya:
```text
secret.txt
```

menggunakan:
```text
Cluster 100
Cluster 101
Cluster 102
```

Ketika file masih aktif:
```text
100 → allocated
101 → allocated
102 → allocated
```

Setelah file dihapus, filesystem dapat menandai cluster tersebut sebagai tersedia untuk digunakan kembali.

Secara konseptual:
```text
Before:

100 → A
101 → A
102 → A

After deletion:

100 → F
101 → F
102 → F
```

Tetapi isi cluster belum tentu langsung hilang.

Inilah alasan:
```text
Free cluster
```

tidak selalu berarti:
```text
Zero data
```

dan konsep tersebut nantinya akan membawa kita menuju **unallocated space analysis dan file carving**.

---
# `$Boot`

Artifact berikutnya adalah:
```text
$Boot
```

Ini merupakan metadata file NTFS yang berkaitan dengan struktur boot dan informasi penting mengenai filesystem.

Di dalamnya terdapat informasi seperti:
```text
Bytes Per Sector
Sectors Per Cluster
Total Sectors
MFT location
MFT Mirror location
```

Informasi seperti ini sangat berguna untuk memahami layout filesystem.

Misalnya kita ingin mengetahui:
```text
Cluster size
```

kita perlu memahami parameter filesystem yang mendasarinya.

Karena itu `$Boot` merupakan salah satu sumber informasi fundamental mengenai struktur NTFS.

---
# `$MFTMirr`

NTFS juga memiliki:
```text
$MFTMirr
```

yang merupakan mirror terhadap bagian awal MFT.

Tujuannya berkaitan dengan filesystem recovery dan redundancy terhadap bagian penting MFT.

Secara konseptual:
```text
MFT
 ↓
Primary metadata

MFTMirr
 ↓
Backup / mirror of critical MFT records
```

Ini menunjukkan satu hal penting:

Filesystem modern tidak hanya terdiri dari file dan directory yang terlihat oleh user.

Di belakang layar terdapat berbagai **metadata files** yang digunakan NTFS untuk mengelola dirinya sendiri.

---
# NTFS Metadata Files

Sekarang kamu mulai perlu mengenal bahwa beberapa nama yang terlihat aneh seperti:
```text
$MFT
$MFTMirr
$LogFile
$Volume
$AttrDef
$Bitmap
$Boot
$BadClus
$Secure
$UpCase
$Extend
```

bukan file biasa yang dibuat oleh user.

Mereka merupakan bagian dari **NTFS metadata infrastructure**.

Secara konseptual:
```text
NTFS
│
├── $MFT
├── $MFTMirr
├── $LogFile
├── $Volume
├── $Bitmap
├── $Boot
├── $BadClus
├── $Secure
├── $UpCase
└── $Extend
      │
      └── $UsnJrnl
```

Tidak semuanya akan menjadi fokus investigation setiap saat.

Tetapi sebagai forensic analyst, kamu harus tahu bahwa filesystem memiliki internal artifacts sendiri.

---
# `$Extend`

Salah satu struktur penting adalah:
```text
$Extend
```

Directory ini digunakan NTFS untuk menyimpan beberapa metadata extension.

Di dalamnya kita dapat menemukan artifact seperti:
```text
$UsnJrnl
```

dan struktur lain yang berhubungan dengan fitur NTFS.

Secara konseptual:
```text
$Extend
   │
   ├── $UsnJrnl
   └── ...
```

Jadi ketika nanti kita mencari USN Journal secara langsung dari forensic image, kamu tidak boleh kaget ketika lokasinya bukan:
```text
C:\Users\Alice\Documents\
```

karena ini bukan file milik user.

Ini adalah filesystem metadata.

---
# Hubungan MFT, USN Journal, dan `$LogFile`

Sekarang kita gabungkan.

Misalnya user melakukan:
```text
Create file
      ↓
Modify file
      ↓
Rename file
      ↓
Delete file
```

Berbagai artifact dapat meninggalkan jejak berbeda:
```text
                NTFS Activity
                     │
          ┌──────────┼──────────┐
          ↓          ↓          ↓
         MFT      USN Journal  $LogFile
          │          │          │
       metadata   change      transaction
                   records
```

Tidak berarti setiap aktivitas akan memberikan bukti identik di semua artifact.

Justru tugas analyst adalah memahami **apa yang dapat dan tidak dapat dibuktikan oleh masing-masing artifact**.

Misalnya:
```text
MFT
→ metadata file

USN Journal
→ perubahan filesystem

$LogFile
→ transaction-level information

$Bitmap
→ allocation state
```

Dengan memahami perbedaan ini, kamu mulai bergerak dari sekadar "menggunakan tool" menjadi benar-benar melakukan **artifact interpretation**.

---
# Kenapa materi ini penting untuk timeline analysis?

Sebelumnya kamu sudah belajar timestamp:

```text
Created
Modified
Accessed
Changed
```

Sekarang kita mempunyai sumber timestamp tambahan dari berbagai artifact.

Misalnya:
```text
10:00
File created

10:05
File modified

10:07
File renamed

10:10
File deleted
```

Jika kita hanya melihat filesystem saat ini, sebagian informasi tersebut mungkin tidak lagi terlihat.

Tetapi dengan menggabungkan:
```text
MFT
+
USN Journal
+
$LogFile
+
Windows Event Logs
+
Prefetch
+
LNK
```

kita dapat membangun **timeline aktivitas**.

Inilah alasan kita mempelajari metadata artifact sebelum masuk ke timeline analysis.

---
# Prinsip penting: Artifact bukan kebenaran absolut

Misalnya USN Journal menunjukkan:
```text
FILE_DELETE
```

Kita dapat mengatakan:
> "Terdapat record yang menunjukkan operasi deletion terhadap file tersebut."

Tetapi jangan langsung mengubahnya menjadi:
> "Alice sengaja menghapus file tersebut pada pukul X."

Itu sudah melompat terlalu jauh.

USN Journal memberi kita informasi mengenai filesystem activity, bukan otomatis identitas manusia yang melakukan aktivitas tersebut.

Untuk menghubungkan aktivitas filesystem dengan user, kita membutuhkan artifact tambahan.

Misalnya:
```text
USN Journal
+
Windows Security Event Log
+
User Session
+
Process Execution
+
Prefetch
```

Barulah kita dapat membangun hipotesis yang lebih kuat.

Ini kembali ke prinsip:
```text
Artifact
   ↓
Interpretation
   ↓
Correlation
   ↓
Finding
   ↓
Conclusion
```