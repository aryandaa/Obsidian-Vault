#latihan 

Sampai sekarang kita sudah belajar melihat filesystem dari beberapa sudut. MFT memberi kita metadata file, `$UsnJrnl` memberi kita jejak perubahan filesystem, `$LogFile` berkaitan dengan transaction logging, sedangkan artifact lain seperti `$Bitmap` membantu memahami allocation state. Tetapi kalau semuanya hanya kita lihat satu per satu, kita masih belum benar-benar melakukan reconstruction terhadap sebuah kejadian.

Timeline Analysis adalah proses mengumpulkan informasi yang memiliki unsur waktu dari berbagai forensic artifact, kemudian menyusunnya berdasarkan urutan waktu sehingga aktivitas pada sistem dapat direkonstruksi.

Bayangkan kita menemukan sebuah file:
```text
C:\Users\Alice\Downloads\suspicious.exe
```

MFT memberi kita beberapa timestamp. USN Journal mungkin memiliki record mengenai perubahan file tersebut. Browser artifact mungkin menunjukkan bahwa file tersebut didownload. Event Log mungkin menunjukkan aktivitas tertentu. Kalau semua informasi tersebut memiliki timestamp, kita dapat menyusunnya menjadi:

```text
09:41:12
User accessed website

09:42:03
suspicious.exe downloaded

09:42:05
File created on filesystem

09:42:17
File metadata changed

09:43:01
File executed

09:43:15
Network connection established
```

Sekarang kita tidak hanya mempunyai kumpulan artifact. Kita mempunyai **urutan kejadian**.

Itulah tujuan utama timeline analysis.

---
# Kenapa waktu sangat penting dalam forensic?

Dalam investigation, pertanyaan yang sering muncul bukan hanya:
> "File apa yang ditemukan?"

Tetapi:
> "Apa yang terjadi sebelum dan sesudah file tersebut ditemukan?"

Misalnya kita menemukan:
```text
malware.exe
```

Kalau hanya melihat file tersebut, kita mengetahui bahwa file itu ada.

Tetapi timeline dapat membantu kita melihat:
```text
Browser activity
      ↓
Download
      ↓
File creation
      ↓
Execution
      ↓
Network connection
      ↓
File modification
      ↓
Deletion
```

Dengan begitu investigator dapat membangun **sequence of events**.

Ini sangat penting dalam incident response dan digital investigation karena sebuah incident hampir selalu merupakan rangkaian aktivitas, bukan satu event tunggal.

---
# Timestamp pada NTFS

Kamu sebelumnya sudah mempelajari timestamp dari MFT.

Pada NTFS, salah satu informasi penting berasal dari:
```text
$STANDARD_INFORMATION
```

dan:
```text
$FILE_NAME
```

Keduanya dapat memiliki timestamp yang berkaitan dengan file.

Secara sederhana:
```text
$STANDARD_INFORMATION
├── Created
├── Modified
├── MFT Changed
└── Accessed
```

Sedangkan `$FILE_NAME` juga memiliki timestamp yang dapat digunakan dalam analysis.

Karena itu ketika melakukan timeline analysis, kita tidak boleh sekadar melihat satu timestamp lalu menganggapnya sebagai "waktu file dibuat".

Kita perlu memahami **artifact dan field yang menghasilkan timestamp tersebut**.

---
# MACB

Dalam forensic timeline, kamu akan sering menemukan istilah: **MACB**

MACB merupakan singkatan dari:
```text
M = Modified
A = Accessed
C = Changed
B = Birth
```

Secara sederhana:
```text
M → file content modified
A → file accessed
C → metadata changed
B → file created
```

Misalnya sebuah timeline memiliki:
```text
2026-08-16 10:15:20 M...B
```

Kita dapat menginterpretasikannya secara umum sebagai event yang berkaitan dengan modification dan birth/creation.

Format detailnya tergantung tool yang digunakan, tetapi konsep MACB sangat penting karena timeline forensic sering menggunakan representasi seperti ini.

---
# Mengapa satu timestamp tidak cukup?

Misalnya kita menemukan:
```text
Created:
10:00
```

Kita mungkin berpikir:
> "File dibuat pukul 10:00."

Tetapi dalam forensic, kita harus lebih hati-hati.

Timestamp tersebut menunjukkan informasi dari artifact tertentu. Ia tidak otomatis membuktikan siapa yang membuat file, bagaimana file tersebut masuk ke sistem, atau aktivitas manusia apa yang terjadi pada waktu tersebut.

Misalnya sebuah file bisa berasal dari:
```text
Browser download
USB
Network share
Archive extraction
Software installation
File copy
```

Maka timestamp harus dikorelasikan dengan artifact lain.

Inilah prinsip yang sudah kita pelajari sebelumnya:
```text
Artifact
   ↓
Timestamp
   ↓
Correlation
   ↓
Finding
```

Bukan:
```text
Timestamp
   ↓
Kesimpulan
```

---
# Timeline dari MFT

Sumber pertama yang paling jelas adalah MFT.

Misalnya kita mempunyai:
```text
report.txt
secret.txt
suspicious.exe
```

Masing-masing memiliki metadata.

Secara konseptual:
```text
MFT

report.txt
Created    09:00
Modified   09:10

secret.txt
Created    09:30
Modified   09:31

suspicious.exe
Created    10:00
Modified   10:00
```

Kalau kita susun berdasarkan waktu:
```text
09:00  report.txt created
09:10  report.txt modified
09:30  secret.txt created
09:31  secret.txt modified
10:00  suspicious.exe created
```

Ini sudah menjadi timeline sederhana.

Namun timeline ini masih hanya berasal dari satu sumber.

---
# Timeline dari USN Journal

Sekarang tambahkan `$UsnJrnl`.

Misalnya:
```text
09:00
report.txt created

09:10
report.txt modified

09:30
secret.txt created

09:45
secret.txt renamed

09:46
secret.txt deleted
```

Sekarang kita mempunyai informasi aktivitas yang lebih kaya.

MFT:
```text
secret.txt
```

USN Journal:
```text
secret.txt
CREATE
RENAME
DELETE
```

Keduanya dapat dikorelasikan.

---
# Menggabungkan artifact

Sekarang kita gabungkan:

```text
             NTFS Timeline
                  │
        ┌─────────┼─────────┐
        ↓         ↓         ↓
       MFT      USN       $LogFile
        │      Journal       │
        ↓         ↓         ↓
     Metadata   Changes   Transactions
```

Kemudian kita dapat memasukkan artifact lain nantinya:
```text
MFT
USN Journal
$LogFile
Windows Event Logs
Browser
Prefetch
LNK
Recycle Bin
Network
```

Hasil akhirnya menjadi timeline yang jauh lebih kaya.

Misalnya:
```text
10:00:01
Browser downloaded file

10:00:02
File created in Downloads

10:00:03
Filesystem recorded modification

10:00:05
File executed

10:00:07
Network connection established

10:00:15
File deleted
```

Sekarang investigator mempunyai gambaran mengenai sequence of events.

---
# Timeline bukan sekadar daftar timestamp

Ini bagian yang penting.

Timeline analysis bukan pekerjaan:
> "Ambil semua timestamp lalu sort."

Kalau cuma begitu, spreadsheet juga bisa menjadi forensic analyst. Dan kita belum sampai pada titik di mana Excel berhak mengambil pekerjaan manusia.

Timeline analysis membutuhkan **interpretation**.

Misalnya kita menemukan:
```text
10:00
file created

10:01
file modified

10:05
file deleted
```

Pertanyaannya bukan hanya:
> "Apa timestamp-nya?"

Tetapi:

> "Artifact apa yang menghasilkan timestamp tersebut?"

> "Apa event yang direpresentasikan?"

> "Apakah timestamp tersebut konsisten dengan artifact lain?"

> "Apakah ada gap?"

> "Apakah ada event yang mungkin terjadi tetapi tidak tercatat?"

> "Apakah timezone sudah diperhitungkan?"

Pertanyaan-pertanyaan ini yang membuat timeline menjadi forensic analysis.

---
# Timezone

Salah satu masalah yang sering muncul adalah timezone.

Misalnya sebuah artifact menunjukkan:
```text
10:00 UTC
```

Tetapi investigator berada di timezone:
```text
UTC+8
```

Maka waktu lokalnya:
```text
18:00
```

Kalau timezone tidak diperhatikan, timeline dapat terlihat seolah-olah event terjadi pada waktu yang berbeda.

Karena itu timeline harus mempunyai konteks:
```text
Timestamp
+
Timezone
```

Dalam investigation nyata, kita juga harus mempertimbangkan apakah timestamp berasal dari:
```text
UTC
Local Time
System Time
Application Time
```

Tidak semua artifact menggunakan representasi waktu yang sama.

---
# Timeline dan Deleted Files

Kita membuat:
```text
deleted-evidence.txt
```

Kemudian menghapusnya.

Filesystem saat ini tidak lagi menunjukkan file tersebut sebagai file aktif.

Tetapi kita sebelumnya sudah belajar bahwa:
```text
MFT
+
USN Journal
+
Unallocated Space
```

dapat memberikan jejak berbeda.

Misalnya timeline secara konseptual menunjukkan:
```text
10:00
deleted-evidence.txt created

10:05
deleted-evidence.txt modified

10:10
deleted-evidence.txt deleted
```

Walaupun file tersebut sudah tidak terlihat pada directory aktif, timeline dapat membantu menunjukkan bahwa aktivitas tersebut pernah terjadi.

Inilah salah satu alasan timeline analysis sangat berguna untuk deleted evidence.

---
# Timeline dan correlation

Sekarang kita masuk ke konsep yang akan terus kita gunakan sampai tingkat advanced.

Misalnya timeline menunjukkan:
```text
10:00
suspicious.exe created

10:01
suspicious.exe modified

10:02
suspicious.exe executed
```

Kita belum boleh langsung mengatakan:
> "Attacker menjalankan malware pada 10:02."

Kita membutuhkan correlation.

Misalnya kemudian kita menemukan:
```text
Prefetch
→ suspicious.exe execution

Event Log
→ process-related event

Network
→ outbound connection

MFT
→ file existed

USN Journal
→ file creation
```

Sekarang beberapa sumber independen memberikan informasi yang saling mendukung.

Secara konseptual:
```text
MFT
  +
USN Journal
  +
Prefetch
  +
Event Log
  +
Network
       ↓
   Correlation
       ↓
 Stronger Finding
```

Semakin banyak artifact independen yang konsisten, semakin kuat interpretasi kita.

---
# Timeline Analysis dalam investigation

Pada akhirnya workflow kita akan terlihat seperti:
```text
Forensic Image
      ↓
Filesystem Analysis
      ↓
Artifact Extraction
      ↓
Timestamp Extraction
      ↓
Normalization
      ↓
Timeline
      ↓
Correlation
      ↓
Investigation
```

Kita tidak hanya mencari file.

Kita mencoba menjawab:
```text
What happened?
When did it happen?
What happened before it?
What happened after it?
Which artifacts support the event?
```

Ini adalah perubahan besar dalam cara berpikir forensic.

---
# Contoh Mini Investigation

Bayangkan kita mempunyai evidence:
```text
C:\Users\Alice\Downloads\update.exe
```

MFT menunjukkan:
```text
Created: 14:20
Modified: 14:20
```

USN Journal:
```text
14:20
FILE_CREATE

14:21
DATA_EXTEND
```

Kemudian artifact lain menunjukkan:
```text
14:22
Execution
```

Dan network evidence menunjukkan:
```text
14:23
Outbound connection
```

Timeline kita:
```text
14:20
update.exe created
      ↓
14:21
update.exe modified
      ↓
14:22
update.exe executed
      ↓
14:23
Outbound network connection
```

Dari sini kita mempunyai hipotesis:
> `update.exe` kemungkinan dibuat pada sistem, kemudian mengalami perubahan, dieksekusi, dan setelah itu terjadi komunikasi outbound.

Perhatikan penggunaan kata **kemungkinan**.

Forensic analyst harus membedakan:
```text
Evidence
```

dari:
```text
Interpretation
```

dan:
```text
Conclusion
```

Itu akan menjadi semakin penting ketika nanti kita melakukan full case investigation.