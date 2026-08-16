#cybersecurity 

Setelah memahami bagaimana storage dibentuk menjadi partition, volume, dan filesystem, sekarang kita masuk ke konsep yang sangat penting dalam praktik Digital Forensics, yaitu **forensic disk image**. Ini adalah titik ketika pembelajaran kita mulai bergerak dari sekadar memahami bagaimana storage bekerja menjadi memahami bagaimana seorang forensic analyst bekerja terhadap salinan evidence yang sebenarnya.

Bayangkan investigator mendapatkan sebuah laptop yang diduga digunakan dalam sebuah insiden. Di dalam laptop tersebut terdapat sistem operasi, file pengguna, browser history, deleted files, log, konfigurasi, dan mungkin malware. Secara teori kita bisa saja langsung membuka laptop tersebut dan memeriksa isinya. Masalahnya, setiap tindakan yang kita lakukan pada storage dapat mengubah evidence. Operating system bisa menulis file baru, memperbarui timestamp, membuat log, mengubah access time, atau melakukan berbagai aktivitas background tanpa kita sadari.

Karena itu dalam forensic kita sebisa mungkin tidak menjadikan **original storage** sebagai tempat utama untuk melakukan analisis. Kita membuat salinan forensik dari storage tersebut, kemudian melakukan examination terhadap salinan tersebut.

Konsep sederhananya:
```text
Original Evidence
       ↓
Forensic Acquisition
       ↓
Forensic Image
       ↓
Verification
       ↓
Forensic Analysis
```

Dengan cara ini, investigator dapat melakukan analisis berulang kali tanpa harus terus menyentuh evidence asli.

---
# Apa itu Disk Image?

**Disk image** adalah representasi digital dari media storage yang dibuat untuk merepresentasikan isi media tersebut sehingga dapat dianalisis sebagai evidence.

Misalnya terdapat hard disk:
```text
Physical Disk
┌─────────────────────────────┐
│ Partition                   │
│ Filesystem                  │
│ Files                       │
│ Deleted Data                │
│ Unallocated Space           │
└─────────────────────────────┘
```

Kemudian dilakukan acquisition.

Hasilnya bisa berupa:
```text
disk.dd
```

atau:
```text
disk.raw
```

atau format forensic seperti:
```text
disk.E01
```

Kita kemudian melakukan analisis terhadap image tersebut.

Jadi ketika nanti kamu mendapatkan:
```text
evidence.E01
```

jangan menganggapnya sebagai "sebuah file biasa".

Secara konseptual, itu adalah **wadah yang merepresentasikan evidence storage**.

---
# Imaging vs Copy File

Ini bagian yang sangat penting.

Misalnya kamu memiliki:
```text
C:\Users\Alice\Documents\
```

dan kamu melakukan:
```bash
cp report.pdf backup/
```

Itu adalah **file copy**.

Sedangkan forensic imaging memiliki tujuan yang jauh berbeda.

Kita ingin mendapatkan representasi storage yang mencakup sebanyak mungkin informasi yang relevan, termasuk area yang tidak terlihat melalui filesystem biasa.

Secara sederhana:
```text
File Copy

Disk
 ↓
File A
 ↓
Copy File A
```

Sedangkan:
```text
Forensic Image

Physical Disk
 ↓
Sector / Block
 ↓
Forensic Image
```

Forensic image dapat mencakup:
```text
Active files
Deleted data
Filesystem structures
Unallocated space
Partition information
Metadata
```

tergantung metode acquisition dan format yang digunakan.

Inilah alasan forensic imaging jauh lebih penting daripada sekadar menyalin folder.

---
# Logical Acquisition dan Physical Acquisition

Dalam acquisition, terdapat beberapa pendekatan.

**Logical acquisition** mengambil data yang terlihat atau dapat diakses melalui logical filesystem.

Misalnya:
```text
Users/
Documents/
Downloads/
Pictures/
```

Pendekatan ini lebih mudah dan sering lebih cepat, tetapi tidak selalu mencakup seluruh storage.

Sedangkan **physical acquisition** berusaha mendapatkan representasi storage pada level yang lebih rendah.

Secara sederhana:
```text
Logical Acquisition
Filesystem
    ↓
Files
```

sedangkan:
```text
Physical Acquisition
Storage
    ↓
Sectors / Blocks
    ↓
Filesystem
    ↓
Files
```

Physical acquisition lebih berguna ketika kita ingin melakukan analisis seperti deleted file recovery atau file carving.

---
# Raw Image

Format paling sederhana yang sering digunakan adalah **raw image**.

Contohnya:
```text
disk.dd
```

atau:
```text
disk.raw
```

Raw image pada dasarnya merupakan representasi data storage dalam bentuk raw.

Secara konseptual:
```text
Physical Disk
      ↓
Raw acquisition
      ↓
disk.dd
```

Keuntungannya adalah format ini relatif sederhana dan didukung oleh banyak forensic tools.

Namun raw image sendiri tidak menyediakan banyak metadata tambahan mengenai acquisition.

---
# E01

Format yang sangat penting untuk kamu kenal adalah **E01**.

E01 merupakan format forensic imaging yang digunakan secara luas dalam forensic investigation.

Contohnya:
```text
evidence.E01
```

Salah satu kelebihan format forensic seperti E01 adalah dapat menyimpan metadata mengenai evidence dan acquisition serta mendukung mekanisme integritas tertentu.

Image juga dapat dipecah menjadi beberapa segment.

Misalnya:
```text
evidence.E01
evidence.E02
evidence.E03
```

Ketiganya dapat menjadi bagian dari satu forensic image.

Jadi jangan menganggap:
```text
E01
E02
E03
```

sebagai tiga disk berbeda hanya karena namanya berbeda.

Mereka bisa merupakan **segment dari satu evidence image**.

---
# Kenapa Forensic Image Harus Diverifikasi?

Sekarang kita kembali ke konsep yang sudah kita pelajari di Evidence Handling.

Misalnya investigator membuat image:

```text
original disk
      ↓
evidence.E01
```

Bagaimana kita tahu bahwa image tersebut tidak berubah?

Kita dapat menggunakan hash.

Misalnya:
```text
SHA-256
```

Secara konseptual:
```text
Evidence
   ↓
SHA-256
   ↓
ABC123...
```

Kemudian setelah acquisition:
```text
Forensic Image
   ↓
SHA-256
   ↓
ABC123...
```

Jika nilai yang dibandingkan sesuai berdasarkan prosedur dan sumber hash yang tepat, kita mendapatkan bukti bahwa data yang diverifikasi memiliki integritas yang konsisten.

Ini menghubungkan materi sekarang dengan **Evidence Integrity** yang sudah kita pelajari.

Jadi konsepnya mulai menyatu:
```text
Evidence Handling
       ↓
Acquisition
       ↓
Forensic Image
       ↓
Hash Verification
       ↓
Analysis
```

---
# Write Blocker

Sekarang kita kembali sebentar ke hardware.

Dalam forensic acquisition, investigator harus mencegah komputer melakukan write ke evidence source apabila prosedurnya membutuhkan preservation pada media asli.

Salah satu perangkat yang digunakan adalah: **Write blocker.**

Secara sederhana, write blocker memungkinkan:
```text
Forensic Workstation
       ↓
     READ
       ↓
Evidence Drive
```

tetapi mencegah:
```text
Forensic Workstation
       ↓
     WRITE
       X
Evidence Drive
```

Tujuannya adalah menjaga agar investigator tidak secara tidak sengaja mengubah evidence.

Misalnya investigator hanya ingin membaca:
```text
secret.txt
```

tetapi operating system melakukan operasi write ke filesystem tanpa disadari.

Kalau itu terjadi pada original evidence, integrity evidence dapat dipertanyakan.

Karena itu prinsipnya adalah:
> **Read evidence, don't modify evidence.**

---
# Acquisition Workflow

Sekarang kita satukan konsep yang sudah kita pelajari.

Secara umum workflow acquisition dapat digambarkan:

```text
Identify Evidence
       ↓
Document Evidence
       ↓
Preserve Evidence
       ↓
Connect Evidence
       ↓
Acquire Image
       ↓
Verify Image
       ↓
Store Original Safely
       ↓
Analyze Working Copy
```

Perhatikan bahwa **analysis datang setelah acquisition dan verification**.

Jangan langsung:
```text
Laptop ditemukan
      ↓
Buka Windows
      ↓
Klik folder
```

Itu bukan workflow forensic yang ideal untuk original evidence.

Workflow yang lebih baik:
```text
Evidence
   ↓
Preservation
   ↓
Acquisition
   ↓
Verification
   ↓
Examination
   ↓
Analysis
   ↓
Reporting
```

---
# Live Acquisition vs Dead Acquisition

Sekarang ada satu konsep penting.

**Dead acquisition** dilakukan ketika sistem tidak sedang berjalan.

Misalnya:
```text
Laptop
   ↓
Power off
   ↓
Storage removed
   ↓
Forensic acquisition
```

Sedangkan **live acquisition** dilakukan ketika sistem masih aktif.

Misalnya komputer sedang menyala dan investigator perlu mengambil volatile evidence seperti:
```text
RAM
Running processes
Network connections
Logged-in users
```

Ini berkaitan dengan **Order of Volatility** yang sudah kita pelajari.

Karena RAM bersifat volatile, mematikan komputer terlebih dahulu dapat menyebabkan informasi di RAM hilang.

Jadi kita tidak bisa mengatakan:
> "Selalu matikan komputer sebelum forensic."

Konteks investigation menentukan tindakan.

Untuk disk imaging biasa, kondisi media dan prosedur acquisition harus dipertimbangkan. Untuk memory forensics, sistem aktif justru bisa sangat penting.

---
# Apa yang Bisa Ada di Dalam Disk Image?

Bayangkan kita memiliki:
```text
evidence.E01
```

Di dalamnya mungkin terdapat:
```text
Partition Table
      ↓
Partition
      ↓
Filesystem
      ↓
Windows
      ↓
Users
      ↓
Documents
Downloads
Desktop
AppData
      ↓
Browser Artifacts
Registry
Event Logs
Prefetch
Deleted Files
Unallocated Space
```

Dan inilah alasan kita belajar storage dan filesystem terlebih dahulu.

Ketika nanti menggunakan Autopsy atau The Sleuth Kit, tool akan membantu kita melihat struktur tersebut.

Tetapi kamu harus memahami apa yang sebenarnya sedang ditampilkan.

Misalnya Autopsy menunjukkan:
```text
Deleted Files
```

kamu harus sudah memahami bahwa konsep deleted file berhubungan dengan filesystem allocation.

Kalau tool menunjukkan:
```text
Unallocated Space
```

kamu sudah memahami bahwa area tersebut tidak sedang dialokasikan sebagai file aktif.

Kalau tool menunjukkan:
```text
MFT
```

kamu tahu bahwa kita sedang berhadapan dengan struktur penting NTFS.

Jadi tools bukan pengganti pemahaman.

---

Praktek: [Praktek 4](Praktek%204.md)

---
# Cara berpikir setelah materi ini
Sebelum materi ini, kamu melihat:

```text
disk.E01
```

dan berpikir:
> “Ini image disk.”

Sekarang pola berpikirmu harus menjadi:
```text
Evidence
   ↓
Acquisition
   ↓
Forensic Image
   ↓
Hash Verification
   ↓
Partition
   ↓
Filesystem
   ↓
Artifacts
```

Kemudian kamu harus mulai bisa membedakan:
```text
Original Evidence
       ≠
Forensic Image
       ≠
Working Copy
```

Original evidence adalah sumber awal yang harus dipreservasi.

Forensic image adalah hasil acquisition yang merepresentasikan evidence tersebut.

Working copy adalah salinan yang digunakan untuk melakukan examination dan analysis sesuai workflow.

Ini penting karena nanti dalam lomba kamu akan sering diberi file seperti:
```text
challenge.E01
challenge.raw
disk.dd
image.aff4
```

dan tugasmu bukan sekadar membuka file tersebut. Kamu harus memahami **apa yang sedang kamu analisis, bagaimana image tersebut diperoleh, bagaimana memverifikasinya, dan bagaimana masuk ke struktur filesystem di dalamnya**.