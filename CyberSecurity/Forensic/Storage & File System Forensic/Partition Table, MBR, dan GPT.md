#cybersecurity 

Pada materi sebelumnya kita sudah memahami bahwa sebuah forensic image bukan sekadar file besar yang berisi kumpulan file. Di dalamnya terdapat struktur storage yang bertingkat, dan salah satu struktur paling awal yang harus kita pahami adalah **partition table**.

Kalau sebelumnya kita menggambarkan storage seperti:
```text
Physical Disk
      ↓
Partition
      ↓
Volume
      ↓
Filesystem
      ↓
Files
```

sekarang kita akan melihat bagaimana komputer mengetahui bahwa partition tersebut berada di mana dan berapa ukurannya.

Di sinilah **partition table** berperan.

Ketika forensic analyst mendapatkan sebuah image seperti:
```text
evidence.raw
disk.dd
disk.E01
```

salah satu pertanyaan pertama yang harus dijawab adalah:
> "Bagaimana struktur partition di dalam image ini?"

Karena kita belum tentu langsung menemukan filesystem hanya dengan membuka image. Bisa saja sebuah disk memiliki beberapa partition, ada partition recovery, EFI System Partition, Linux partition, Windows partition, atau bahkan ruang yang belum dialokasikan.

Secara konseptual:
```text
Disk Image
     ↓
Partition Table
     ↓
Partitions
     ↓
Filesystems
     ↓
Files & Artifacts
```

Jadi partition table bisa dianggap sebagai **peta awal storage**.

---
# Apa itu Partition Table?

Partition table adalah struktur pada storage yang menyimpan informasi mengenai partition yang terdapat pada disk.

Informasi yang dapat berkaitan dengan partition antara lain:
```text
Partition start
Partition end
Partition size
Partition type
Partition status
```

Dengan informasi tersebut operating system dapat mengetahui bagaimana storage dibagi.

Misalnya sebuah disk:
```text
Disk
┌─────────────────────────────────────┐
│ Partition 1                         │
├─────────────────────────────────────┤
│ Partition 2                         │
├─────────────────────────────────────┤
│ Partition 3                         │
├─────────────────────────────────────┤
│ Unallocated                         │
└─────────────────────────────────────┘
```

Partition table memberikan informasi yang memungkinkan sistem memahami struktur tersebut.

Dalam forensic, informasi ini sangat berguna karena kita dapat mengetahui **di mana sebuah partition dimulai dan berakhir**.

---
# LBA dan Offset

Sebelum membahas MBR dan GPT, kamu perlu memahami dua istilah yang sering muncul ketika menganalisis disk.

Yang pertama adalah **LBA**, atau Logical Block Addressing.

LBA memberikan alamat terhadap block atau sector secara logis.

Secara sederhana:
```text
LBA 0
LBA 1
LBA 2
LBA 3
LBA 4
...
```

Kamu bisa membayangkan LBA seperti nomor rumah pada sebuah jalan. Daripada berkata "data berada sekitar 2 GB dari awal disk", forensic tool dapat bekerja dengan alamat block tertentu.

Yang kedua adalah **offset**.

Offset menunjukkan posisi relatif suatu data dari titik awal tertentu.

Misalnya sebuah struktur berada pada:
```text
Offset = 1024 bytes
```

berarti struktur tersebut berada 1024 bytes setelah awal data yang menjadi referensi.

Dalam disk forensic, offset sangat penting karena kita sering bekerja pada level byte atau sector.

---
# MBR

Sekarang kita masuk ke partition scheme yang lebih tua dan masih sangat penting untuk dipahami:

**MBR**, atau **Master Boot Record**.

MBR berada di bagian awal disk.

Secara konseptual:
```text
Disk
│
├── MBR
│
├── Partition
├── Partition
└── ...
```

Secara historis, MBR memiliki beberapa fungsi penting. Ia dapat berisi boot code dan partition table.

Struktur sederhananya:
```text
Sector 0
┌──────────────────────────────┐
│ Boot Code                    │
├──────────────────────────────┤
│ Partition Table              │
├──────────────────────────────┤
│ Boot Signature               │
└──────────────────────────────┘
```

Karena MBR berada pada awal disk, forensic analyst sering memeriksa area tersebut ketika melakukan disk examination.

---
# MBR Partition Table

Salah satu keterbatasan penting MBR adalah jumlah partition yang dapat direpresentasikan secara langsung.

Secara tradisional MBR memiliki **empat primary partition entries**.

Model sederhananya:
```text
MBR
├── Partition 1
├── Partition 2
├── Partition 3
└── Partition 4
```

Untuk mengatasi keterbatasan tersebut, konsep **extended partition** dan **logical partition** digunakan.

Misalnya:
```text
MBR
├── Primary Partition
├── Primary Partition
├── Primary Partition
└── Extended Partition
      ├── Logical Partition
      ├── Logical Partition
      └── Logical Partition
```

Ini penting ketika kamu menemukan disk image lama atau sistem yang menggunakan struktur partition berbasis MBR.

---
# MBR dan Batasan Ukuran Disk

MBR memiliki keterbatasan lain yang sangat penting.

MBR menggunakan sistem addressing yang secara tradisional berkaitan dengan 32-bit sector addressing.

Jika menggunakan sector 512 bytes, batas teoritis yang sering dibahas adalah sekitar:
```text
2 TiB
```

Artinya MBR menjadi kurang cocok untuk storage modern berkapasitas sangat besar.

Perkembangan storage kemudian mendorong penggunaan partitioning scheme yang lebih modern: **GPT.**

---
# GPT

GPT adalah singkatan dari: **GUID Partition Table.**

GPT merupakan bagian dari standar modern yang digunakan bersama sistem UEFI.

Secara konseptual:
```text
Disk
│
├── Protective MBR
├── GPT Header
├── Partition Entries
├── Partitions
│
└── Backup GPT
```

Berbeda dengan MBR yang memiliki partition table utama dalam struktur awalnya, GPT memiliki struktur yang lebih fleksibel dan menyediakan mekanisme redundancy.

GPT juga menggunakan **GUID**, atau Globally Unique Identifier, untuk mengidentifikasi partition dan jenis partition.

---
# GPT Header

Salah satu struktur penting pada GPT adalah **GPT Header**.

Header tersebut berisi informasi mengenai struktur GPT.

Secara konseptual:
```text
GPT Header
├── GPT Signature
├── Revision
├── Header Size
├── Header CRC
├── Current LBA
├── Backup LBA
├── First Usable LBA
├── Last Usable LBA
├── Disk GUID
└── Partition Entry Information
```

Tidak perlu menghafalkan semuanya sekarang.

Yang penting kamu memahami bahwa GPT menyimpan metadata yang memungkinkan forensic analyst memahami struktur partition pada disk.

---
# Protective MBR

Ada satu hal yang sering membingungkan ketika pertama kali melihat GPT.

Kalau GPT adalah sistem modern, kenapa ada MBR juga?

Karena GPT biasanya memiliki **Protective MBR** di awal disk.

Tujuannya antara lain untuk mencegah software lama yang hanya memahami MBR menganggap disk GPT sebagai disk kosong.

Secara sederhana:
```text
LBA 0
┌──────────────────────┐
│ Protective MBR       │
└──────────────────────┘

LBA 1
┌──────────────────────┐
│ GPT Header           │
└──────────────────────┘

LBA 2...
┌──────────────────────┐
│ GPT Partition Entries│
└──────────────────────┘
```

Jadi kalau kamu melakukan low-level examination terhadap GPT disk, jangan langsung menganggap keberadaan MBR berarti seluruh disk menggunakan MBR partitioning.

---
# GPT Partition Entries

Setelah GPT header terdapat partition entries.

Secara konseptual:
```text
GPT
│
├── Entry 1
├── Entry 2
├── Entry 3
├── Entry 4
└── ...
```

Setiap entry dapat memberikan informasi mengenai partition seperti:
```text
Partition Type GUID
Partition GUID
Starting LBA
Ending LBA
Attributes
Partition Name
```

Informasi tersebut kemudian membantu forensic analyst mengetahui lokasi dan karakteristik setiap partition.

---
# GPT Backup

Salah satu fitur penting GPT adalah adanya struktur backup.

Secara sederhana:

```text
Beginning of Disk
        ↓
GPT Header
        ↓
Partition Entries
        ↓
Partitions
        ↓
...
        ↓
Backup Partition Entries
        ↓
Backup GPT Header
```

Jadi terdapat GPT metadata di bagian awal dan salinan pada bagian akhir disk.

Hal ini memberikan redundancy.

Dalam forensic, redundancy tersebut juga menarik karena jika struktur utama mengalami kerusakan, struktur backup dapat membantu memahami kondisi disk.

---
# MBR vs GPT

Sekarang kita bandingkan secara sederhana.

|MBR|GPT|
|---|---|
|Lebih tua|Lebih modern|
|Partition table utama di awal|Header + partition entries|
|4 primary partition entries secara tradisional|Mendukung jauh lebih banyak partition|
|Addressing tradisional terbatas|Menggunakan LBA 64-bit|
|Cocok untuk sistem lama|Umum pada sistem modern|
|Berkaitan dengan BIOS|Umumnya digunakan bersama UEFI|
|Tidak memiliki backup partition table seperti GPT|Memiliki backup GPT|

Jangan menghafalkan tabel ini sebagai daftar ujian. Yang jauh lebih penting adalah memahami struktur mentalnya:
```text
MBR:

Disk
 ↓
MBR
 ↓
Partition Table
 ↓
Partitions
```

sedangkan:
```text
GPT:

Disk
 ↓
Protective MBR
 ↓
GPT Header
 ↓
Partition Entries
 ↓
Partitions
 ↓
Backup GPT
```

---
# Kenapa MBR dan GPT Penting dalam Digital Forensics?

Sekarang kita kembali ke forensic image.

Misalnya kamu mendapatkan:
```text
challenge.dd
```

Jangan langsung menjalankan pencarian file.

Pertama kita ingin mengetahui:
```text
Disk
 ↓
Partition Scheme
 ↓
Partitions
 ↓
Filesystem
```

Misalnya hasil pemeriksaan menunjukkan:
```text
Partition 1
Start: 2048
End: 534527
Type: EFI System

Partition 2
Start: 534528
End: 419430399
Type: NTFS
```

Sekarang kita mulai memahami struktur evidence.

Kita tahu bahwa partition kedua kemungkinan merupakan partition yang berisi filesystem utama.

Nanti kita dapat menghitung offset untuk mengakses filesystem tersebut.

---
# Partition Offset

Ini adalah konsep yang sangat penting untuk praktik forensic.

Misalnya sebuah partition dimulai pada:
```text
Start LBA = 2048
```

dan ukuran sector:
```text
512 bytes
```

maka offset awal partition adalah:
```text
2048 × 512
= 1,048,576 bytes
```

atau:

```text
1 MiB
```

Jadi:

```text
Partition Start
      ↓
LBA 2048
      ↓
Byte Offset 1,048,576
```

Ini penting karena sebuah filesystem mungkin **tidak dimulai pada byte 0 dari disk image**.

Misalnya:
```text
disk image
│
├── Partition Table
│
├── unused area
│
├── Partition
│   └── NTFS
│       └── Files
│
└── ...
```

Kalau kamu mencoba membaca NTFS dari offset yang salah, tool bisa gagal mengenali filesystem.

Inilah alasan forensic analyst perlu memahami struktur storage, bukan hanya menggunakan GUI tool.

---

Praktek : [Praktek 5](Praktek%205.md)

---

# Kenapa Kita Belajar `mmls`?

Karena nanti dalam lomba kamu bisa mendapatkan:
```text
challenge.E01
```

atau:
```text
challenge.dd
```

dan salah satu langkah awal yang sangat umum adalah mengetahui struktur partition.

Tools seperti Autopsy memang bisa menyembunyikan kompleksitas tersebut.

Tetapi kalau kamu memahami:
```text
LBA
Offset
Partition
Filesystem
```

kamu dapat melakukan analisis manual ketika tool tidak memberikan hasil yang kamu harapkan.

Dan dalam CTF atau kompetisi forensic, situasi seperti itu cukup mungkin terjadi. Challenge tidak selalu dirancang agar satu tombol menyelesaikan semuanya. Sayangnya, komputer belum punya kewajiban untuk bersikap kooperatif.

---
# Cara Berpikir Setelah Materi Ini

Sekarang ketika melihat:
```text
disk.E01
```

jangan langsung berpikir:
> "Cari file mencurigakan."

Urutannya harus mulai seperti ini:
```text
Evidence Image
      ↓
Image Verification
      ↓
Partition Table
      ↓
MBR / GPT
      ↓
Partition Start / End
      ↓
Partition Offset
      ↓
Filesystem
      ↓
Filesystem Structures
      ↓
Files
```

Dengan pola pikir seperti ini, nanti ketika sebuah tool gagal menemukan filesystem, kamu tidak langsung bingung.

Kamu bisa bertanya:
> Apakah partition table terbaca?

> Apakah ini MBR atau GPT?

> Di LBA berapa partition dimulai?

> Apakah offset yang digunakan benar?

> Filesystem apa yang berada di partition tersebut?

> Apakah filesystem masih intact atau mengalami corruption?

Itulah cara berpikir yang perlahan kita bangun.