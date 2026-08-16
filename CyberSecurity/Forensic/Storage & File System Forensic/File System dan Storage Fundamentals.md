#cybersecurity 

Sekarang kita masuk ke salah satu fondasi terpenting dalam Digital Forensics. Kalau materi sebelumnya mengajarkan bagaimana memperlakukan evidence agar tetap dapat dipercaya, materi ini mengajarkan **di mana evidence itu sebenarnya berada dan bagaimana komputer menyimpannya**.

Ini penting karena nanti kamu akan sering mendapatkan forensic image seperti `disk.E01`, `image.dd`, atau `drive.raw`. Ketika pertama kali melihatnya, kamu mungkin berpikir, “Oke, ini image disk.” Masalahnya, itu baru permukaan. Di dalamnya terdapat struktur storage yang bertingkat, dan setiap tingkat bisa meninggalkan artefak forensic yang berbeda.

Kalau kamu tidak memahami struktur tersebut, tools seperti Autopsy memang bisa menampilkan banyak informasi, tetapi kamu hanya akan menjadi orang yang menekan tombol lalu berharap komputer menjelaskan semuanya. Kita akan menghindari tradisi manusia yang sangat populer itu.

---
## Dari data sampai file

Ketika kamu menyimpan sebuah file seperti:
```text
secret.txt
```

sebenarnya komputer tidak menyimpan konsep “file” dengan cara sesederhana yang terlihat di File Explorer.

Secara konseptual, data storage memiliki beberapa lapisan:
```text
Physical Disk
      ↓
Partition
      ↓
Volume
      ↓
File System
      ↓
Directory
      ↓
File
      ↓
File Content
```

Mari kita bedah satu per satu.

**Physical disk** adalah media penyimpanan fisik, misalnya HDD atau SSD.

Di dalam disk tersebut dapat terdapat satu atau beberapa **partition**.

Partition merupakan pembagian ruang pada disk. Misalnya sebuah disk 1 TB bisa memiliki satu partition besar, atau beberapa partition dengan ukuran berbeda.

Di dalam partition tersebut dapat terdapat **volume** yang kemudian menggunakan filesystem tertentu.

Filesystem bertugas mengatur bagaimana data disimpan dan ditemukan. Contohnya NTFS pada Windows dan ext4 pada Linux.

Filesystem kemudian mengorganisasi data menjadi directory dan file.

Jadi ketika kamu membuka:
```text
C:\Users\Yanda\Documents\report.pdf
```

sebenarnya kamu sedang melihat hasil abstraksi yang dibangun operating system di atas struktur storage yang jauh lebih kompleks.

Dalam forensic, kita sering perlu turun melewati abstraksi tersebut.

---
# Storage: HDD vs SSD

Sebelum masuk filesystem, kita perlu memahami media penyimpanannya.

HDD atau Hard Disk Drive menggunakan piringan magnetik yang berputar dan head untuk membaca serta menulis data. Karena data disimpan secara magnetik, struktur fisiknya berbeda dari SSD.

SSD atau Solid State Drive menggunakan flash memory dan tidak memiliki piringan yang berputar.

Perbedaan ini penting dalam forensic, terutama ketika membahas **deleted files**.

Pada HDD, ketika sebuah file dihapus, ada kemungkinan data fisiknya masih berada di media sampai ruang tersebut digunakan kembali.

Pada SSD, terdapat mekanisme seperti **TRIM** yang dapat membuat proses recovery deleted data menjadi lebih sulit. Ketika operating system memberi tahu SSD bahwa block tertentu tidak lagi digunakan, controller SSD dapat melakukan garbage collection dan menghapus atau merelokasi data tersebut.

Jadi jangan punya asumsi:
> “File deleted pasti bisa direcover.”

Tidak.

Recovery bergantung pada banyak faktor, termasuk filesystem, kondisi media, apakah data sudah tertimpa, dan pada SSD apakah TRIM serta garbage collection sudah memengaruhi block tersebut.

---
# Sector dan Block

Sekarang kita turun sedikit lebih rendah.

Storage dibagi menjadi unit-unit data.

Pada level disk, kamu akan sering menemukan istilah **sector**. Sector merupakan unit penyimpanan yang digunakan oleh perangkat storage. Ukuran sector historisnya sering 512 bytes, sementara banyak drive modern menggunakan 4096-byte physical sectors atau Advanced Format.

Filesystem kemudian bekerja dengan unit logis yang sering disebut **block** atau **cluster**, tergantung konteks filesystem.

Pada Windows NTFS, misalnya, konsep yang penting adalah **cluster**.

Misalnya sebuah file berukuran:
```text
5000 bytes
```

dan filesystem menggunakan cluster:

```text
4096 bytes
```

File tersebut tidak bisa ditempatkan dalam tepat 5000 bytes jika allocation unit-nya 4096 bytes. Secara sederhana, filesystem membutuhkan dua cluster:

```text
Cluster 1 → 4096 bytes
Cluster 2 → 904 bytes digunakan
```

Sisa ruang pada cluster terakhir menjadi bagian dari allocation yang tidak digunakan oleh file tersebut.

Konsep ini nantinya berhubungan dengan **file slack**.

Dan file slack dapat menjadi menarik dalam forensic karena bagian ruang yang tidak digunakan tersebut kadang masih mengandung data lama.

---
# Partition

Sekarang bayangkan sebuah disk:
```text
1 TB Disk
┌──────────────────────────────┐
│ Partition 1                  │
│ 200 GB                       │
├──────────────────────────────┤
│ Partition 2                  │
│ 700 GB                       │
├──────────────────────────────┤
│ Unallocated                  │
│ 100 GB                       │
└──────────────────────────────┘
```

Operating system dapat menggunakan partition tersebut untuk tujuan berbeda.

Misalnya:

```text
Partition 1 → EFI/System
Partition 2 → Windows
Partition 3 → Recovery
```

Dalam forensic, **unallocated space** juga menarik, Kenapa?
Karena ruang yang terlihat “kosong” oleh filesystem belum tentu benar-benar kosong secara fisik.

Jika sebuah file dihapus, filesystem dapat menandai area tersebut sebagai available.

Secara sederhana:
```text
File:
[DATA DATA DATA]

Deleted:
[???? ???? ????]
```

Filesystem mungkin tidak lagi menganggapnya sebagai file aktif, tetapi sebagian data fisiknya masih bisa berada di sana.

Inilah salah satu sumber deleted-file recovery dan file carving.

---
# File System

Sekarang kita sampai pada komponen yang sangat penting.

Filesystem bertanggung jawab mengatur bagaimana file dan directory disimpan serta bagaimana operating system menemukan data tersebut.

Filesystem menyimpan informasi seperti:
```text
File name
File size
File location
File timestamps
File attributes
Directory structure
Allocation information
```

Struktur sebenarnya jauh lebih kompleks.

Dalam forensic, kita tidak hanya tertarik pada isi file.

Kita juga tertarik pada:
> “Bagaimana filesystem mengatakan bahwa file ini ada?”

> “Di mana data file tersebut berada?”

> “Kapan filesystem mencatat aktivitas tersebut?”

> “Apa yang terjadi setelah file dihapus?”

Pertanyaan-pertanyaan tersebut membawa kita ke filesystem internals.

---
materi lanjutan untuk memahami jenis jenis dari File System: [Jenis-jenis File system](Jenis-jenis%20File%20system.md)

---
# Unallocated Space

Sekarang bagian yang sangat penting untuk forensic.

**Unallocated space** adalah area storage yang tidak sedang dialokasikan oleh filesystem untuk file aktif.

Misalnya sebuah disk memiliki:
```text
Allocated
████████████████

Unallocated
░░░░░░░░░░░░░░░░
```

Bagian unallocated dapat mengandung data lama.

Misalnya user memiliki:
```text
secret.txt
```

Kemudian menghapusnya.

Filesystem dapat menandai ruang tersebut sebagai available:
```text
secret.txt
      ↓
deleted
      ↓
space becomes unallocated
```

Tetapi isi block mungkin belum tertimpa.

Maka forensic analyst dapat melakukan pencarian atau carving terhadap area tersebut.

Ini salah satu konsep yang nanti akan kita praktikkan.

---
# File Slack

Sekarang kita punya satu konsep lagi.

Misalnya cluster berukuran:
```text
4096 bytes
```

File hanya menggunakan:
```text
3000 bytes
```

Maka terdapat:
```text
1096 bytes
```

yang tidak digunakan oleh file tersebut dalam allocation unit terakhir.

Bagian tersebut disebut **file slack**.

Secara konseptual:
```text
Cluster 4096 bytes

┌──────────────────────────────┐
│ File data       │ Slack      │
│ 3000 bytes      │ 1096 bytes │
└──────────────────────────────┘
```

Dalam kondisi tertentu, slack space dapat mengandung residual data dari aktivitas sebelumnya.

Ini bukan berarti selalu ada informasi rahasia di sana. Tetapi dalam forensic, ruang yang tidak terlihat oleh user bisa menjadi sumber evidence.

---
# File Signature dan Magic Bytes

Filesystem bukan satu-satunya cara kita mengenali file.

Misalnya sebuah file bernama:
```text
photo.jpg
```

Kita tidak seharusnya percaya hanya karena extension-nya `.jpg`.

Extension bisa diganti.

Misalnya:
```text
malware.exe
      ↓ rename
photo.jpg
```

Sekarang File Explorer mungkin menampilkan `photo.jpg`, tetapi isi sebenarnya masih executable.

Untuk mengetahui tipe file berdasarkan isi, kita bisa melihat **file signature** atau **magic bytes**.

Misalnya beberapa format file memiliki byte awal tertentu.

Secara konseptual:
```text
File extension
      ↓
"photo.jpg"

Magic bytes
      ↓
actual file format
```

Linux memiliki command:
```bash
file suspicious.bin
```

Command tersebut mencoba mengidentifikasi tipe file berdasarkan konten dan signature.

Ini akan sangat berguna ketika kita masuk ke **file carving**.

---
Praktek: [Praktek 3](Praktek%203.md)

---
# Cara berpikir setelah materi ini

Sebelum materi ini, ketika melihat:
```text
disk.E01
```

kamu mungkin hanya berpikir:
> “Ini file image.”

Sekarang kamu harus mulai berpikir:
```text
disk.E01
   ↓
Physical storage representation
   ↓
Partition
   ↓
Volume
   ↓
Filesystem
   ↓
Filesystem structures
   ↓
Files + Metadata
   ↓
Artifacts
```

Kemudian ketika melihat file:
```text
secret.txt
```

jangan hanya bertanya:
> “Apa isi file ini?”

Mulai bertanya:
> “Di mana file ini berada?”

> “Filesystem apa yang digunakan?”

> “Bagaimana filesystem merepresentasikan file ini?”

> “Kapan file dibuat atau dimodifikasi?”

> “Apakah file pernah dihapus?”

> “Di cluster mana data tersebut berada?”

> “Apakah ada metadata lain?”

> “Apakah ada data residual di unallocated space atau slack?”

Nah, ini sudah mulai masuk ke cara berpikir forensic yang kita butuhkan.
