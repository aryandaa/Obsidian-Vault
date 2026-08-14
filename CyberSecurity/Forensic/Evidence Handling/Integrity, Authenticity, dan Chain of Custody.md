#cybersecurity 

Sekarang kita masuk ke bagian yang sangat penting dalam Digital Forensics, yaitu **bagaimana memastikan evidence yang kita gunakan masih dapat dipercaya**. Setelah sebelumnya kita belajar bahwa forensic bergantung pada evidence, muncul pertanyaan yang lebih serius: bagaimana kalau evidence tersebut sudah berubah? Bagaimana kalau file yang kita analisis bukan salinan yang sama dengan evidence awal? Bagaimana kalau seseorang memodifikasi evidence tanpa kita sadari? Dan bagaimana kita membuktikan siapa yang menangani evidence tersebut selama proses investigasi?

Kalau pertanyaan-pertanyaan ini tidak bisa dijawab, maka kesimpulan forensic kita menjadi lemah. Kamu mungkin menemukan sesuatu yang benar, tetapi tidak memiliki dasar yang kuat untuk menunjukkan bahwa data tersebut memang masih autentik dan tidak berubah. Dalam kompetisi CTF, aspek ini kadang tidak terlalu terlihat karena challenge biasanya sudah memberikan evidence siap analisis. Tetapi dalam Digital Forensics dunia nyata, konsep ini sangat fundamental. Bahkan dalam lomba, memahami konsepnya akan membantu kamu mengerti kenapa workflow forensic dilakukan dengan cara tertentu.

Ada tiga konsep utama yang perlu kamu pahami sekarang: **integrity, authenticity, dan chain of custody**.

---
## Integrity: Apakah evidence masih sama?

**Integrity** berarti kondisi data tetap utuh dan tidak mengalami perubahan yang tidak diinginkan.

Bayangkan kamu mendapatkan sebuah file:
```text
evidence.E01
```
File tersebut adalah forensic image dari sebuah hard disk.

Sebelum melakukan analisis, kamu menghitung SHA-256:
```text
SHA-256:
7f8c...a91d
```

Kemudian kamu membuat salinan untuk dianalisis:
```text
evidence.E01
evidence-copy.E01
```

Kamu menghitung hash keduanya dan hasilnya sama.

Artinya, berdasarkan hash tersebut, salinan memiliki isi yang sama dengan evidence awal.

Sekarang bayangkan setelah beberapa proses analisis, hash `evidence-copy.E01` berubah.

Itu merupakan indikasi bahwa data telah berubah.

Kita belum tentu langsung tahu **kenapa** berubah, tetapi kita tahu bahwa kondisi datanya tidak lagi sama.

Inilah fungsi utama integrity verification.

Secara sederhana:
```text
Evidence awal
      ↓
   Hashing
      ↓
   SHA-256
      ↓
Nilai referensi
      ↓
Analisis
      ↓
Hash ulang
      ↓
Bandingkan
```

Jika nilai hash tetap sama, tidak ada perubahan pada isi data yang terdeteksi oleh hash tersebut.

Jika berbeda, ada perubahan.

---
## Kenapa menggunakan hash?

Hash function mengambil input dengan ukuran berapa pun dan menghasilkan output dengan ukuran tertentu.

Contohnya SHA-256 menghasilkan 256-bit digest yang biasanya ditampilkan sebagai 64 karakter hexadecimal.

Misalnya:

```text
evidence.txt
        ↓
     SHA-256
        ↓
a8f4c...92bd
```

Kemudian isi file berubah sedikit saja:
```text
evidence.txt
        ↓
     SHA-256
        ↓
1d73a...f82c
```

Hasilnya akan berubah secara signifikan.

Hal menariknya adalah kita tidak perlu membaca seluruh isi file untuk melakukan perbandingan integrity. Kita cukup membandingkan digest-nya.

Inilah kenapa hashing sangat berguna dalam forensic.

Namun ada satu hal yang harus kamu pahami dengan benar:

**Hash bukan bukti bahwa sebuah file “aman”.**

Hash digunakan untuk membantu memastikan **data tidak berubah** atau untuk membandingkan apakah dua data memiliki isi yang sama.

Misalnya kamu memiliki malware:
```text
malware.exe
SHA-256:
abc123...
```

Hash tersebut tidak berarti:
> “malware.exe aman.”

Justru malware bisa memiliki hash yang valid.

Hash hanya mengatakan:
> “File yang saya periksa menghasilkan digest ini.”

Jangan sampai konsep ini tertukar. Hash bukan antivirus. Komputer sudah cukup punya masalah tanpa kita meminta hash menjadi dokter sekaligus satpam.

---
# Authenticity: Apakah evidence benar-benar berasal dari sumber yang diklaim?

Sekarang kita masuk ke **authenticity**.

Integrity dan authenticity memang berhubungan, tetapi bukan hal yang sama.

**Integrity** berfokus pada:
> Apakah data berubah?

Sedangkan **authenticity** berfokus pada:
> Apakah data tersebut benar-benar berasal dari sumber yang diklaim?

Contohnya kamu mendapatkan sebuah file:
```text
browser-history.db
```

Hash-nya valid dan tidak berubah sejak acquisition.

Itu membuktikan integrity file tersebut berdasarkan hash yang digunakan.

Tetapi apakah file tersebut benar-benar berasal dari komputer korban? Belum tentu.

Bisa saja seseorang memberikan file lain yang kebetulan memiliki nama sama.

Karena itu forensic membutuhkan proses acquisition, documentation, identification, dan evidence handling yang baik.

Jadi:
```text
Integrity
= evidence tidak berubah

Authenticity
= evidence memang berasal dari sumber yang diklaim
```

Keduanya saling melengkapi.

---
# Contoh sederhana

Bayangkan polisi mendapatkan sebuah USB.

USB tersebut diberi label:
```text
USB-KORBAN-01
```

Kemudian USB di-image menjadi:
```text
usb01.E01
```

Hash image:
```text
SHA-256:
ABC123...
```

Hash tersebut membantu memastikan image tidak berubah setelah dibuat.

Tetapi investigator juga perlu mengetahui:
> USB ini diambil dari mana?

> Siapa yang mengambilnya?

> Kapan diambil?

> Bagaimana USB tersebut disimpan?

> Siapa yang melakukan imaging?

> Apakah image tersebut benar-benar berasal dari USB tersebut?

Pertanyaan-pertanyaan ini berhubungan dengan authenticity dan chain of custody.

---
# Chain of Custody

Sekarang kita masuk ke konsep ketiga.

**Chain of Custody** adalah catatan mengenai perjalanan evidence selama proses investigasi.

Bayangkan sebuah evidence berpindah dari satu orang ke orang lain.
```text
Evidence ditemukan
        ↓
Investigator A
        ↓
Forensic Imaging
        ↓
Analyst B
        ↓
Analyst C
        ↓
Reporting
```

Setiap perpindahan dan aktivitas penting terhadap evidence harus dapat ditelusuri.

Tujuannya sederhana:
**kita harus tahu siapa melakukan apa terhadap evidence, kapan, dan bagaimana.**

Misalnya ada sebuah hard disk yang ditemukan di lokasi kejadian.

Investigator A mengambilnya.

Kemudian A menyerahkannya kepada forensic examiner B.

B melakukan imaging.

Kemudian forensic image diberikan kepada analyst C.

C melakukan analysis.

Jika semua proses tersebut terdokumentasi, kita mempunyai chain of custody.

Jika tiba-tiba muncul pertanyaan:
> “Dari mana file image ini berasal?”

kita dapat melihat dokumentasinya.

Kalau tidak ada dokumentasi, investigator akan mengalami masalah.

---
# Chain of Custody bukan sekadar daftar nama

Jangan menganggap chain of custody hanya seperti:
```text
A → B → C
```

Dokumentasi biasanya mencakup informasi yang jauh lebih lengkap, seperti identitas evidence, waktu acquisition, siapa yang memperoleh evidence, lokasi, metode acquisition, hash, siapa yang menyerahkan, siapa yang menerima, bagaimana evidence disimpan, dan aktivitas yang dilakukan terhadap evidence.

Contoh sederhananya:
```text
Evidence ID   : CASE01-USB01
Description   : USB Flash Drive
Acquired By   : Investigator A
Date          : 2026-08-13
Hash          : SHA-256 ...
Acquisition   : Forensic Imaging
Transferred   : Analyst B
Purpose       : Examination
```

Dalam praktik profesional, format dan prosedurnya bisa jauh lebih kompleks tergantung organisasi dan kasus.

Untuk lomba, kamu mungkin tidak diminta membuat dokumen chain of custody lengkap. Tetapi memahami konsep ini akan membangun kebiasaan yang benar.

---
# Write Blocker

Sekarang kita masuk sedikit ke hardware forensic.

Bayangkan kamu mempunyai hard disk evidence.

Kalau kamu memasukkan hard disk tersebut langsung ke komputer biasa, operating system bisa melakukan berbagai aktivitas terhadap media tersebut.

Misalnya filesystem mungkin di-mount.

Operating system mungkin menulis metadata.

Bahkan aktivitas kecil yang tidak disengaja dapat mengubah evidence.

Karena itu dalam forensic acquisition digunakan perangkat atau mekanisme yang disebut **write blocker**.

Tujuannya adalah:
> memungkinkan investigator membaca data dari media tanpa mengizinkan sistem menulis ke media evidence.

Secara sederhana:
```text
Evidence Drive
      │
      ▼
Write Blocker
      │
      ▼
Forensic Workstation
```

Data dapat dibaca:
```text
Evidence → Workstation
```

Tetapi write operation diblokir:
```text
Workstation → Evidence
        X
```

Ini sangat penting ketika kita melakukan acquisition terhadap media asli.

Dalam praktik modern, terdapat hardware write blocker maupun software-based write protection tergantung kebutuhan dan environment.

---
# Evidence Preservation

Setelah evidence ditemukan, kita harus mempertahankan kondisinya.

Prinsip sederhananya:
> **Jangan melakukan sesuatu terhadap evidence asli kalau sebenarnya kamu bisa melakukan analisis terhadap salinannya.**

Misalnya:
```text
ORIGINAL
   │
   ├── Hash
   │
   ▼
FORENSIC IMAGE
   │
   ├── Hash
   │
   ▼
ANALYSIS COPY
   │
   ▼
FORENSIC ANALYSIS
```

Dengan pendekatan seperti ini, evidence original tetap menjadi sumber referensi.

Jika analysis copy rusak atau berubah, kita dapat membuat salinan baru dari image yang sudah diverifikasi.

Ini jauh lebih aman daripada melakukan:
```text
Original Disk
    ↓
Buka file
    ↓
Edit sesuatu
    ↓
Install software
    ↓
Restart
    ↓
“Lho kok evidence berubah?”
```

Kita ingin menghindari skenario tersebut.

---
# Order of Volatility

Sekarang kita hubungkan materi ini dengan materi sebelumnya.

Kamu sudah tahu bahwa beberapa evidence lebih mudah hilang daripada yang lain.

RAM adalah contoh volatile evidence.

Disk adalah contoh non-volatile evidence.

Maka investigator perlu mempertimbangkan **order of volatility** ketika melakukan acquisition.

Secara konsep:
```text
Paling volatile
      ↓
RAM
      ↓
Network state
      ↓
Running processes
      ↓
Temporary system data
      ↓
Disk
      ↓
Backup / archival storage
      ↓
Paling persistent
```

Urutan sebenarnya dapat berbeda tergantung konteks dan environment, jadi jangan menghafalkan diagram tersebut sebagai hukum alam semesta. Yang penting adalah memahami prinsipnya:

**semakin mudah data berubah atau hilang, semakin penting mempertimbangkan acquisition-nya sebelum melakukan tindakan yang dapat menghilangkan data tersebut.**

Misalnya komputer masih menyala dan investigator ingin mengetahui proses yang sedang berjalan.

Kalau komputer langsung dimatikan:
```text
RAM
 ↓
hilang
```

Padahal mungkin di sana terdapat informasi penting.

Sebaliknya, kalau investigator ingin menganalisis file yang tersimpan pada disk, disk evidence biasanya lebih persisten.

---
# Live System vs Dead System

Dari sini muncul dua pendekatan yang penting.

**Live forensics** dilakukan ketika sistem masih menyala.

**Dead-box forensics** dilakukan terhadap media atau image setelah sistem tidak lagi berjalan.

Live system memiliki keuntungan karena kita dapat memperoleh volatile evidence seperti RAM, process, connection, dan system state.

Tetapi live acquisition juga mempunyai risiko karena ketika kita menjalankan command atau tools pada sistem, kita sendiri dapat menyebabkan perubahan terhadap sistem.

Misalnya kamu menjalankan:
```bash
ps aux
```

atau membuka sebuah program.

Aktivitas tersebut sendiri merupakan aktivitas baru yang terjadi pada sistem.

Sedangkan dead-box analysis memberikan lingkungan yang lebih stabil karena investigator melakukan analisis terhadap image atau storage yang sudah di-acquire.

Tidak ada pendekatan yang selalu paling benar. Investigator harus memilih metode berdasarkan tujuan investigasi dan kondisi kasus.

Latihan Integrity, Authenticity, dan Chain of Custody: [Praktek 2](Praktek%202.md)

---
# Cara berpikir yang harus mulai terbentuk

Mulai sekarang kalau kamu mendapatkan evidence, jangan langsung bertanya:

> “Tools apa yang dipakai?”

Biasakan bertanya:
> “Apa evidence yang saya punya?”

Kemudian:

> “Seberapa volatile evidence ini?”

> “Bagaimana saya memastikan integrity-nya?”

> “Dari mana evidence ini berasal?”

> “Bagaimana evidence ini diperoleh?”

> “Apa artifact yang bisa saya ekstrak?”

> “Bagaimana saya membuktikan finding saya?”

Ini perubahan kecil dalam cara berpikir, tetapi sangat penting. Orang yang hanya hafal tools bisa berhenti ketika tool-nya gagal. Orang yang memahami evidence masih bisa mencari jalan lain.