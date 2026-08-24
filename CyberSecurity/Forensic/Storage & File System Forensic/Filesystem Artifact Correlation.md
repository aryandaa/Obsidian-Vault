#cybersecurity 

Sampai sekarang kita sudah mempelajari banyak artifact secara terpisah. Kita sudah melihat MFT, NTFS metadata, `$UsnJrnl`, `$LogFile`, timestamps, deleted files, unallocated space, sampai file carving. Kalau semua itu hanya kita pelajari sebagai kumpulan command dan struktur, kemampuan forensic kita sebenarnya belum lengkap.

Investigator tidak bekerja dengan pola:
```text
MFT → selesai
USN Journal → selesai
Deleted File → selesai
Carving → selesai
```

Yang dilakukan adalah **correlation**, yaitu menghubungkan beberapa artifact untuk menentukan apakah informasi yang mereka berikan saling mendukung, bertentangan, atau masih belum cukup untuk membuat kesimpulan.

Misalnya kita menemukan:
```texth
suspicious.exe
```

MFT mengatakan file tersebut pernah ada.

USN Journal menunjukkan file tersebut dibuat.

Timeline menunjukkan waktu pembuatannya.

Kemudian hasil carving menemukan sebagian content file yang sudah dihapus.

Kalau semua informasi tersebut menunjuk pada kejadian yang sama, kita mulai mempunyai evidence yang jauh lebih kuat dibanding hanya menemukan satu artifact.

Secara sederhana:
```text
                    ┌── MFT
                    │
                    ├── USN Journal
                    │
Evidence ───────────┼── Timeline
                    │
                    ├── Deleted Entry
                    │
                    ├── Unallocated Space
                    │
                    └── Recovered File
                            ↓
                       Correlation
                            ↓
                         Finding
```

Inilah inti dari materi ini.

---
# Artifact tidak berdiri sendiri

Misalnya kita menemukan sebuah file:
```text
C:\Users\Alice\Downloads\tool.exe
```

MFT memberikan informasi:
```text
Filename: tool.exe
Size: 850 KB
Created: 10:15
Modified: 10:16
```

Informasi tersebut memberi kita metadata.

Tetapi metadata tersebut belum menjawab:
> Apakah file tersebut pernah dijalankan?

Sekarang kita menemukan artifact lain yang menunjukkan aktivitas execution pada:
```text
10:17
```

Kemudian network evidence menunjukkan:
```text
10:18
Outbound connection
```

Sekarang kita memiliki:
```text
10:15
File created
    ↓
10:16
File modified
    ↓
10:17
Execution evidence
    ↓
10:18
Network activity
```

Hubungan antar-event tersebut jauh lebih informatif.

Namun tetap ada satu prinsip penting:

**Correlation memperkuat hipotesis, tetapi correlation bukan berarti otomatis membuktikan causation.**

Hanya karena dua event terjadi berdekatan bukan berarti event pertama pasti menyebabkan event kedua.

---
# Direct Evidence dan Supporting Evidence

Dalam investigation, kita dapat membedakan informasi berdasarkan perannya.

Misalnya:
```text
MFT
```

memberikan informasi mengenai keberadaan dan metadata file.

Kemudian:
```text
USN Journal
```

memberikan informasi mengenai perubahan filesystem.

Sementara:
```text
Network Evidence
```

dapat memberikan informasi mengenai komunikasi.

Ketiganya bisa menjadi **supporting evidence** untuk sebuah hypothesis.

Contohnya:
```text
Hypothesis:
suspicious.exe dibuat kemudian digunakan.
```

Evidence:
```text
MFT
→ file exists

USN Journal
→ file creation

Execution Artifact
→ file execution

Network
→ outbound connection
```

Semakin konsisten hubungan tersebut, semakin kuat hypothesis yang kita bangun.

---
# Correlation berdasarkan waktu

Cara paling mudah untuk mulai melakukan correlation adalah menggunakan **timeline**.

Misalnya kita memiliki:
```text
10:00:01
tool.exe created

10:00:03
tool.exe modified

10:00:05
tool.exe executed

10:00:07
Network connection established

10:00:10
tool.exe deleted
```

Sekarang kita bisa membangun sequence:
```text
Creation
   ↓
Modification
   ↓
Execution
   ↓
Network Activity
   ↓
Deletion
```

Tetapi timeline tidak hanya digunakan untuk membuat urutan yang terlihat keren di laporan. Kita harus memeriksa setiap event dan sumbernya.

Contohnya:
```text
10:00:01
MFT

10:00:01
USN Journal

10:00:05
Execution artifact

10:00:07
Network log

10:00:10
USN Journal
```

Kalau beberapa artifact independen memberikan waktu yang konsisten, confidence terhadap timeline tersebut meningkat.

---
# Correlation berdasarkan file identity

Timestamp bukan satu-satunya cara melakukan correlation.

Kita juga bisa menggunakan:

```text
Filename
Path
File size
Hash
MFT record
File signature
```

Misalnya MFT menunjukkan:

```text
tool.exe
Size: 125 KB
```

Kemudian file yang berhasil direcover dari unallocated space memiliki:

```text
Size: 125 KB
```

Dan hash hasil recovery cocok dengan hash yang sebelumnya ditemukan.

Maka kita memiliki hubungan:

```text
MFT Entry
    ↓
tool.exe
    ↓
125 KB
    ↓
Recovered File
    ↓
Hash
```

Ini jauh lebih kuat daripada hanya mengatakan:

> "Ada file bernama tool.exe."

---

# Hash sebagai correlation mechanism

Kita kembali bertemu dengan SHA-256 yang sudah kamu pelajari pada awal modul.

Misalnya terdapat:

```text
File A
SHA-256 = ABC123...
```

Kemudian kita menemukan file hasil recovery:

```text
Recovered File
SHA-256 = ABC123...
```

Jika hash dihitung pada representasi byte yang sama dan keduanya cocok, kita memiliki bukti kuat bahwa content-nya identik.

Secara konseptual:

```text
Known File
    ↓
SHA-256
    ↓
ABC123

Recovered File
    ↓
SHA-256
    ↓
ABC123

ABC123 = ABC123
```

Hash dalam konteks ini bukan hanya untuk integrity. Hash juga dapat digunakan untuk **identification dan correlation**.

Ini salah satu alasan kenapa konsep pertama yang kita pelajari tentang hashing terus muncul sampai bagian advanced.

---

# Correlation MFT dan USN Journal

Sekarang kita ambil contoh yang lebih dekat dengan NTFS.

MFT:

```text
report.txt
Created:
10:00
Modified:
10:05
```

USN Journal:

```text
10:00
FILE_CREATE

10:05
DATA_EXTEND

10:07
RENAME
```

Kita dapat membuat timeline:

```text
10:00
report.txt created
       ↓
10:05
report.txt changed
       ↓
10:07
report.txt renamed
```

Jika kemudian MFT menunjukkan nama akhirnya:

```text
final-report.txt
```

kita dapat memiliki indikasi bahwa:

```text
report.txt
    ↓
RENAMED
    ↓
final-report.txt
```

Ini contoh sederhana bagaimana dua artifact membantu mengisi informasi yang tidak lengkap jika hanya menggunakan salah satunya.

---

# Correlation dengan Deleted Files

Sekarang kita masuk ke skenario yang lebih menarik.

Misalnya file:

```text
secret.txt
```

sudah dihapus.

MFT masih mempunyai informasi terkait record.

USN Journal menunjukkan:

```text
FILE_DELETE
```

Unallocated space masih mengandung data.

Kemudian file carving menemukan sebagian file.

Kita sekarang memiliki:

```text
MFT
 ↓
secret.txt existed
 ↓
USN Journal
 ↓
secret.txt deleted
 ↓
Unallocated Space
 ↓
Residual data
 ↓
File Carving
 ↓
Recovered content
```

Ini jauh lebih kuat daripada hanya menemukan:

```text
secret.txt
```

dari sebuah directory listing.

---

# Correlation dan File Carving

File carving sendiri memiliki masalah konteks.

Misalnya carver menemukan:

```text
recovered_001.jpg
```

Kita tidak langsung tahu:

```text
Filename asli
Path asli
User pemilik
Waktu dibuat
```

Tetapi filesystem artifact mungkin memiliki informasi tersebut.

Misalnya:

```text
MFT
→ photo.jpg
→ C:\Users\Alice\Pictures
→ Created: 12:00
```

Kemudian carving menemukan JPEG yang memiliki hash sama.

Sekarang kita dapat menghubungkan:

```text
MFT Entry
     ↓
photo.jpg
     ↓
Deleted
     ↓
Unallocated Data
     ↓
Recovered JPEG
     ↓
Same Hash
```

Metadata dan raw data saling melengkapi.

---

# Contradictory Evidence

Correlation tidak selalu menghasilkan informasi yang cocok.

Kadang artifact justru memberikan informasi berbeda.

Misalnya:

```text
MFT:
Created = 10:00

USN Journal:
Activity = 11:00
```

atau:

```text
Artifact A:
File exists at 10:00

Artifact B:
File appears deleted at 09:00
```

Kita tidak boleh memilih data yang "kelihatannya paling masuk akal" lalu membuang yang lain.

Kita harus mencari penyebab discrepancy.

Kemungkinan penyebab dapat berupa:

```text
Timezone difference
Timestamp semantics
Clock skew
Artifact limitation
Filesystem behavior
Incomplete evidence
Data modification
Parsing error
```

Jadi contradiction sendiri dapat menjadi **finding yang perlu diselidiki**.

---

# Artifact Reliability

Tidak semua artifact memiliki tingkat interpretasi yang sama.

Misalnya timestamp file bukan otomatis berarti:

> "User melakukan aktivitas pada waktu tersebut."

Timestamp menunjukkan informasi mengenai state atau metadata filesystem tertentu.

Begitu pula sebuah browser history entry tidak otomatis membuktikan bahwa manusia secara sadar membaca halaman tersebut. Program, prefetching, background activity, synchronization, atau mekanisme lain dapat menghasilkan artifact.

Karena itu investigator harus membedakan:

```text
Artifact
   ↓
What does it technically show?
   ↓
What can reasonably be inferred?
   ↓
What cannot be inferred?
```

Ini adalah salah satu kemampuan paling penting dalam forensic analysis.

---

# Evidence, Hypothesis, Conclusion

Mulai sekarang kita harus membiasakan diri memisahkan tiga hal.

**Evidence** adalah apa yang benar-benar ditemukan.

Contohnya:

```text
MFT record 42 exists.
Filename = suspicious.exe.
USN Journal contains FILE_CREATE.
```

**Hypothesis** adalah interpretasi sementara.

Misalnya:

```text
suspicious.exe kemungkinan dibuat pada sistem
pada sekitar waktu tersebut.
```

**Conclusion** adalah kesimpulan setelah evidence dikorelasikan dan dianalisis.

Misalnya:

```text
Multiple filesystem artifacts consistently indicate
that suspicious.exe existed on the system and was
subsequently deleted.
```

Perhatikan bahwa conclusion yang baik tetap sesuai dengan apa yang benar-benar dapat didukung evidence.

---

# Contoh Full Correlation

Sekarang bayangkan kita memiliki satu kasus:

```text
Evidence:
disk.raw
```

Kita menemukan:

```text
MFT:
malware.exe
Created: 14:20
```

USN Journal:

```text
14:20
FILE_CREATE

14:25
DATA_EXTEND

14:30
FILE_DELETE
```

Unallocated space:

```text
Data matching malware.exe
```

File carving:

```text
Recovered executable
```

Hash:

```text
SHA-256 = ABCDEF...
```

Timeline:

```text
14:20
malware.exe created

14:25
malware.exe modified

14:30
malware.exe deleted

14:31
Residual data still present
```

Sekarang kita dapat membuat hubungan:

```text
                 ┌── MFT
                 │
                 ├── USN Journal
                 │
malware.exe ─────┼── Timeline
                 │
                 ├── Unallocated Space
                 │
                 └── Recovered File
                          ↓
                        Hash
                          ↓
                     Correlation
```

Kita bukan lagi sekadar membaca output tools.

Kita sedang membangun **forensic narrative** berdasarkan evidence.

---

# Forensic Narrative

Forensic narrative adalah cara menyusun hasil analysis menjadi urutan kejadian yang dapat dipahami.

Misalnya dari evidence tadi:

```text
14:20
A file named malware.exe was present on the NTFS volume.

14:25
Filesystem artifacts indicate that the file's data was modified.

14:30
USN Journal records indicate deletion activity.

14:31
Residual file data remained within unallocated space.

14:32
File carving recovered a portion of the executable.
```

Perhatikan bahwa setiap pernyataan harus dapat dikaitkan kembali ke artifact.

Inilah yang nantinya akan menjadi dasar laporan forensic.

---

# Chain of Evidence

Semua konsep yang sudah kita pelajari sebenarnya saling terhubung:

```text
Original Evidence
       ↓
Hash
       ↓
Forensic Image
       ↓
Partition
       ↓
Filesystem
       ↓
MFT
       ↓
Metadata
       ↓
Timeline
       ↓
Deleted Entry
       ↓
Unallocated Data
       ↓
Carving
       ↓
Recovered File
       ↓
Hash
       ↓
Correlation
       ↓
Finding
```

Perjalanan tersebut harus dapat ditelusuri kembali.

Jika seseorang bertanya:

> "Dari mana kamu mendapatkan file ini?"

Kita harus bisa menjawab:

```text
Forensic Image
→ partition offset
→ NTFS volume
→ unallocated space
→ carving
→ recovered file
→ SHA-256
```

Itulah yang membuat hasil forensic dapat dipertanggungjawabkan.

---

# Kesalahan yang harus dihindari

Kesalahan terbesar dalam correlation adalah **confirmation bias**.

Misalnya investigator sudah mempunyai dugaan:

> "Ini pasti malware."

Kemudian dia hanya mencari artifact yang mendukung dugaan tersebut.

Kalau menemukan sesuatu yang bertentangan:

```text
"Ah, mungkin artifact-nya salah."
```

Itu adalah cara buruk melakukan forensic investigation.

Pendekatan yang lebih baik:

```text
Hypothesis
    ↓
Collect Evidence
    ↓
Correlate
    ↓
Look for Supporting Evidence
    +
Look for Contradicting Evidence
    ↓
Evaluate
    ↓
Conclusion
```

Tujuan investigator bukan membuktikan bahwa hypothesis-nya benar.

Tujuannya adalah menemukan **apa yang sebenarnya dapat didukung oleh evidence**.

---

# Posisi kita sekarang

Kita sudah sampai di bagian paling akhir dari teori utama Storage & File System Forensics:

```text
Storage & File System Forensics

✓ Storage Fundamentals
✓ Filesystem Fundamentals
✓ Disk Imaging
✓ Partition Analysis
✓ NTFS Fundamentals
✓ MFT Analysis
✓ Advanced NTFS Analysis
✓ NTFS Metadata Artifacts
✓ NTFS Timeline Analysis
✓ Deleted File & Unallocated Space Analysis
✓ File Carving
✓ Filesystem Artifact Correlation      ← SEKARANG

□ Final Storage Investigation
```

Setelah materi ini, kita hanya punya **satu tahap besar terakhir**, yaitu **Final Storage Investigation**.

Di tahap itu seluruh konsep yang sudah kita pelajari akan digabungkan menjadi satu investigation. Bukan lagi belajar MFT sendiri, carving sendiri, atau timeline sendiri. Kita akan mengambil satu forensic image dan melakukan investigation dari awal sampai akhir:

```text
Evidence
 ↓
Hash Verification
 ↓
Partition Analysis
 ↓
Filesystem Identification
 ↓
NTFS Examination
 ↓
MFT Analysis
 ↓
Artifact Analysis
 ↓
Timeline
 ↓
Deleted File Analysis
 ↓
Unallocated Space
 ↓
File Carving
 ↓
Recovery
 ↓
Hash
 ↓
Correlation
 ↓
Finding
 ↓
Forensic Report
```

Kalau tahap final tersebut sudah selesai, **Storage & File System Forensics kita nyatakan selesai secara keseluruhan**, lalu roadmap kita berpindah langsung ke **Network Forensics**.