#cybersecurity 

Pada tahap ini kita berhenti melihat forensic artifact sebagai materi yang berdiri sendiri. Sebelumnya kamu sudah mempelajari bagaimana membuat dan memverifikasi forensic image, membaca partition table, mengenali filesystem, memahami NTFS, menganalisis MFT, membaca metadata, memahami deletion, mencari data di unallocated space, melakukan file carving, sampai melakukan correlation antar-artifact.

Sekarang semuanya kita satukan.

Bayangkan kamu menerima sebuah forensic image:
```text
case01.raw
```

Kamu tidak tahu sebelumnya apa yang ada di dalamnya. Kamu tidak boleh langsung membuka filesystem dan mulai mengubah data. Kamu harus memperlakukannya sebagai evidence.

Workflow investigation kita:
```text
Evidence
   ↓
Integrity Verification
   ↓
Disk Identification
   ↓
Partition Analysis
   ↓
Filesystem Identification
   ↓
Filesystem Examination
   ↓
NTFS Metadata
   ↓
MFT Analysis
   ↓
Timeline
   ↓
Deleted Files
   ↓
Unallocated Space
   ↓
File Carving
   ↓
Recovered Evidence
   ↓
Artifact Correlation
   ↓
Finding
   ↓
Forensic Report
```

Perhatikan bahwa ini sebenarnya adalah gabungan dari hampir semua materi yang sudah kamu pelajari.

---
## 1. Evidence Intake

Langkah pertama adalah melakukan identification terhadap evidence.

Misalnya:
```bash
ls -lh case01.raw
```

Kemudian:
```bash
file case01.raw
```

Kita ingin mengetahui terlebih dahulu apa yang sedang kita hadapi.

Jangan langsung melakukan:
```bash
mount case01.raw ...
```

atau menjalankan tool yang memodifikasi image.

Prinsipnya:
```text
Identify first
Analyze second
```

Ini terdengar sederhana karena memang sederhana. Justru manusia sering gagal melakukan hal sederhana karena terlalu bersemangat menekan tombol.

---
## 2. Integrity Verification

Sekarang kita menghitung hash:
```bash
sha256sum case01.raw
```

Jika investigator sebelumnya sudah memberikan reference hash:
```bash
sha256sum -c case01.sha256
```

hasil yang kita harapkan:

```text
case01.raw: OK
```

Kalau verification gagal, investigation tidak otomatis berhenti, tetapi discrepancy tersebut harus dicatat dan diselidiki.

Kita kembali menggunakan konsep awal:
```text
Evidence
   ↓
SHA-256
   ↓
Reference
   ↓
Verification
```

---
## 3. Disk Structure

Setelah integrity diverifikasi, kita melihat struktur disk.

Gunakan:
```bash
mmls case01.raw
```

Sekarang kita mencari:
```text
Partition
Start Sector
End Sector
Length
Filesystem
```

Misalnya kita menemukan:
```text
Partition
Start = 2048
End   = ...
```

Informasi `Start Sector` sangat penting.

Kenapa?

Karena filesystem mungkin tidak dimulai dari byte pertama image.

Misalnya:
```text
Disk Image
0
│
├── GPT
│
├── Partition
│
│   └── NTFS
│
└── Unallocated
```

Maka untuk menganalisis filesystem secara langsung, kita perlu memahami **offset** partition tersebut.

---
## 4. Filesystem Identification

Setelah mengetahui partition, kita menentukan filesystem yang digunakan.

Kamu mungkin menemukan:
```text
NTFS
```

Kalau filesystem-nya NTFS, kita dapat melanjutkan menggunakan tool NTFS dari The Sleuth Kit.

Misalnya:
```bash
fsstat -o 2048 case01.raw
```

Angka:
```text
2048
```

di sini merupakan contoh offset berdasarkan hasil `mmls`.

Jangan asal menyalin angka tersebut ke semua image. Offset harus selalu berasal dari hasil examination terhadap image yang sedang dianalisis.

Ini penting karena:
```text
Different image
    ↓
Different partition layout
    ↓
Different offset
```

---
# 5. NTFS Examination

Sekarang kita mulai masuk ke filesystem.

Dengan:
```bash
fsstat -o <START> case01.raw
```

kita dapat memperoleh informasi mengenai filesystem.

Kita ingin memahami:
```text
Filesystem type
Cluster size
MFT information
Volume information
Filesystem layout
```

Ini membantu kita membangun model:
```text
Disk
 ↓
Partition
 ↓
NTFS
 ↓
MFT
```

---
# 6. File Listing

Sekarang kita melihat file dan directory.

Gunakan:
```bash
fls -o <START> case01.raw
```

Untuk melakukan recursive listing:
```bash
fls -r -o <START> case01.raw
```

Sekarang kita mulai melihat struktur filesystem.

Misalnya:
```text
Users
Users/Alice
Users/Alice/Documents
Users/Alice/Downloads
```

Kemudian kita mencari file yang menarik.

Misalnya:
```text
suspicious.exe
report.docx
secret.zip
```

Jangan langsung menyimpulkan bahwa file bernama `suspicious.exe` adalah malware.

Nama file adalah **artifact**.

Bukan verdict.

---
# 7. Menganalisis MFT Record

Misalnya `fls` memberikan metadata address:
```text
123
```

Kita dapat menganalisis record tersebut menggunakan:
```bash
istat -o <START> case01.raw 123
```

Sekarang kita dapat melihat informasi yang lebih detail mengenai file tersebut.

Kita mencari:
```text
File name
MACB timestamps
File size
Attributes
Data runs
MFT information
```

Di tahap ini kamu mulai menggunakan pemahaman yang sudah dipelajari pada materi NTFS.

---
# 8. MACB Timeline

Salah satu bagian penting adalah timestamp.

Dalam forensic NTFS kita sering berhadapan dengan konsep:
```text
M = Modified
A = Accessed
C = Changed
B = Birth
```

Kita tidak boleh langsung menerjemahkan:
```text
Created = user created the file
```

secara sembarangan.

Timestamp harus dibaca berdasarkan semantics artifact dan dikorelasikan dengan sumber lainnya.

Misalnya:
```text
10:10
File created

10:15
File modified

10:20
File accessed

10:30
File deleted
```

Kita mendapatkan sequence awal.

Tetapi sequence tersebut belum menjadi kesimpulan.

---
# 9. Deleted File

Sekarang kita mencari deleted entry.

Gunakan:
```bash
fls -d -r -o <START> case01.raw
```

Kita mungkin menemukan:
```text
* suspicious.exe
```

Tanda tersebut menunjukkan entry yang telah dihapus dalam konteks output tool.

Sekarang kita punya indikasi:
```text
File existed
      ↓
File was deleted
```

Tetapi kita masih ingin mengetahui apakah content file tersebut masih tersedia.

---
# 10. Recovery dengan icat

Jika MFT record masih memiliki informasi data yang cukup, kita dapat mencoba mengambil file:
```bash
icat -o <START> case01.raw <INODE> > recovered.bin
```

Kemudian:
```bash
file recovered.bin
```

dan:
```bash
sha256sum recovered.bin
```

Sekarang hasil recovery mempunyai identity sendiri:
```text
recovered.bin
SHA-256
```

Kita tidak menganggap hasil tersebut sebagai "file asli" secara otomatis.

Kita harus memeriksa apakah recovery lengkap dan valid.

---
# 11. Unallocated Space

Kalau metadata tidak cukup, kita masuk ke unallocated space.

Salah satu pendekatan yang sudah kita pelajari adalah menggunakan:
```bash
blkls -o <START> case01.raw > unallocated.raw
```

Sekarang kita memiliki representasi data yang berasal dari area unallocated.

Strukturnya:
```text
case01.raw
    ↓
Partition
    ↓
Filesystem
    ↓
Unallocated
    ↓
unallocated.raw
```

Di sinilah file carving menjadi berguna.

---
# 12. File Carving

Kita dapat melakukan carving menggunakan tool seperti:
```text
foremost
scalpel
photorec
```

Misalnya:
```bash
foremost -i unallocated.raw -o carving-output
```

Kemudian kita memeriksa hasil:
```bash
find carving-output -type f
```

Misalnya ditemukan:
```text
carving-output/
├── jpg/
│   ├── 000001.jpg
│   └── 000002.jpg
└── pdf/
    └── 000003.pdf
```

Sekarang jangan langsung percaya.

Kita melakukan validation.

Misalnya:
```bash
file carving-output/jpg/000001.jpg
```

Kemudian:
```bash
sha256sum carving-output/jpg/000001.jpg
```

Kalau diperlukan, buka file tersebut menggunakan viewer yang sesuai dan periksa apakah struktur file memang valid.

---
# 13. Correlation

Sekarang bagian terpenting dari final investigation.

Misalnya kita memiliki:
```text
MFT:
suspicious.exe
```

Kemudian:
```text
USN Journal:
FILE_CREATE
FILE_DELETE
```

Kemudian:
```text
MFT:
Deleted entry
```

Kemudian:
```text
Unallocated:
Residual executable data
```

Kemudian:
```text
File Carving:
Recovered executable
```

Kemudian:
```text
SHA-256:
ABC123...
```

Kita sekarang menghubungkan semuanya.
```text
                 MFT
                  │
                  ▼
           suspicious.exe
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
   USN Journal          Timeline
        │                   │
        └─────────┬─────────┘
                  ▼
               Deleted
                  │
                  ▼
          Unallocated Space
                  │
                  ▼
             Carving
                  │
                  ▼
          Recovered File
                  │
                  ▼
               SHA-256
```

Ini bukan lagi sekadar filesystem analysis.

Ini sudah menjadi investigation.

---
# 14. Menyusun Finding

Setelah semua evidence dikorelasikan, kita membuat **finding**.

Contoh:
```text
Finding:

A file named suspicious.exe was identified within the NTFS
filesystem. Filesystem metadata indicates that the file existed
on the volume and was subsequently deleted. Residual data
associated with the file was identified within unallocated space
and a recoverable file was obtained through file carving.
```

Perhatikan bahasa yang digunakan.

Kita tidak menulis:
```text
User definitely executed malware.
```

kalau kita belum mempunyai evidence execution.

Kita hanya mengatakan apa yang benar-benar didukung evidence.

---
# 15. Evidence vs Interpretation

Ini sangat penting untuk laporan forensic.

Misalnya evidence:
```text
MFT:
suspicious.exe
Created: 14:20
```

Interpretasi yang aman:
```text
The filesystem contains metadata indicating that
suspicious.exe existed at the recorded time.
```

Interpretasi yang terlalu jauh:
```text
The user downloaded suspicious.exe at 14:20.
```

Kenapa?

Karena MFT tidak membuktikan proses download.

Untuk mengatakan file tersebut didownload, kita membutuhkan artifact tambahan seperti browser history, download record, network evidence, atau evidence lain yang mendukung.

Ini adalah perbedaan antara:
```text
Evidence-based analysis
```

dan:
```text
Guessing with timestamps
```

---
# 16. Final Case Timeline

Pada akhirnya kita dapat membuat timeline gabungan:
```text
14:20
File created
        ↓
14:22
File modified
        ↓
14:25
Filesystem activity recorded
        ↓
14:30
File deleted
        ↓
14:31
Residual data remains
        ↓
14:35
File recovered through carving
```

Setiap event harus memiliki sumber.

Misalnya:
```text
14:20 → MFT
14:22 → MFT
14:25 → USN Journal
14:30 → USN Journal
14:31 → Unallocated analysis
14:35 → File carving
```

Dengan begitu timeline kita **traceable**.

---
# 17. Forensic Report

Investigation tidak selesai ketika command terakhir selesai dijalankan.

Hasilnya harus dapat dijelaskan.

Minimal laporan final kita memiliki:
```text
Case Information
Evidence Identification
Integrity Verification
Disk Structure
Partition Analysis
Filesystem
Relevant Artifacts
Timeline
Deleted Files
Recovered Files
Hash Values
Artifact Correlation
Findings
Limitations
Conclusion
```

Bagian **limitations** juga penting.

Misalnya:
```text
The analysis cannot determine whether the recovered executable
was executed because no sufficient execution artifact was
identified within the examined evidence.
```

Kalimat seperti ini justru menunjukkan analisis yang matang.

Investigator yang baik bukan orang yang selalu punya jawaban.

Investigator yang baik tahu **batas jawaban yang dapat diberikan evidence**.

---
# Praktik Final: Mini Storage Forensic Case: [Praktek Final](Praktek%20Final.md)