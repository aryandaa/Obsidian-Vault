#cybersecurity 
# NTFS

Karena kompetisi Digital Forensics sangat sering menggunakan Windows, **NTFS** adalah filesystem yang harus kamu kuasai.

NTFS adalah singkatan dari **New Technology File System** dan merupakan filesystem utama yang digunakan pada banyak instalasi Windows modern.

Salah satu komponen paling penting dalam NTFS adalah:

**Master File Table atau MFT.**

MFT dapat dipahami sebagai database utama yang berisi record mengenai file dan directory dalam volume NTFS.

Secara konseptual:
```text
NTFS Volume
      ↓
MFT
      ↓
File Records
      ↓
Metadata + Data References
```

Setiap file atau directory pada NTFS biasanya memiliki MFT record.

Misalnya:
```text
MFT Record
┌──────────────────────────┐
│ File Name                │
│ Timestamps               │
│ Attributes               │
│ File Size                │
│ Data References          │
│ Security Information     │
└──────────────────────────┘
```

Inilah salah satu alasan NTFS sangat berharga dalam forensic.

File yang sudah dihapus pun dapat meninggalkan MFT record atau sebagian informasi yang berkaitan dengannya, tergantung kondisi filesystem.

Nanti ketika kita melakukan praktik NTFS forensic, kamu akan benar-benar melihat MFT dan bagaimana artifact tersebut digunakan untuk investigation.

---
# MFT dan Deleted Files

Bayangkan terdapat file:
```text
C:\Users\Alice\secret.txt
```

Filesystem memiliki record yang merepresentasikan file tersebut.

Kemudian user menghapus file.

Secara konseptual:
```text
Before:

MFT
 ↓
secret.txt
 ↓
Data blocks
```

Setelah deletion:
```text
MFT
 ↓
record mungkin masih tersisa
 ↓
file marked as deleted
 ↓
data blocks mungkin masih ada
```

Jadi deletion tidak selalu berarti:
```text
DATA = LANGSUNG HILANG
```

Lebih tepatnya:
```text
File system no longer treats it as an active file
```

Sedangkan data fisiknya mungkin masih tersedia.

Tetapi sekali lagi, jangan menganggap recovery selalu berhasil.

---
# FAT32

Filesystem berikutnya adalah **FAT32**.

FAT merupakan singkatan dari File Allocation Table.

FAT32 merupakan filesystem yang sangat umum pada removable media dan perangkat lama.

Struktur sederhananya dapat dibayangkan:
```text
FAT32
├── Boot Sector
├── FAT
├── FAT
└── Data Area
```

FAT berisi informasi mengenai allocation cluster.

Misalnya sebuah file menggunakan cluster:
```text
10 → 11 → 15 → 16
```

Filesystem menggunakan struktur FAT untuk mengetahui hubungan cluster tersebut.

Dalam forensic, informasi allocation seperti ini bisa membantu kita memahami bagaimana file tersusun di storage.

FAT32 juga memiliki keterbatasan seperti ukuran file maksimum sekitar 4 GiB minus 1 byte, sehingga filesystem ini memiliki karakteristik yang berbeda dari NTFS.

---
# exFAT

**exFAT** dikembangkan untuk media flash dan removable storage dengan kebutuhan file yang lebih besar daripada FAT32.

Kamu bisa menemukannya pada:
```text
USB flash drive
SD card
External storage
```

Untuk forensic, exFAT penting karena removable media sering menjadi sumber evidence.

Misalnya dalam sebuah kasus:
> “Apakah attacker menggunakan USB untuk memindahkan file?”

Kalau evidence berupa USB drive, filesystem yang digunakan bisa saja exFAT.

Jadi kamu harus mampu mengenali filesystem sebelum menentukan metode analisis.

---
# ext4

Sekarang kita pindah ke Linux.

Filesystem yang sangat umum pada Linux adalah **ext4**.

Strukturnya berbeda dari NTFS.

Konsep penting pada ext4 adalah **inode**.

Jika pada NTFS kita banyak berbicara mengenai MFT record, pada ext4 kita akan berbicara mengenai inode.

Inode menyimpan metadata mengenai file seperti:
```text
File type
Permissions
Owner
Size
Timestamps
Pointers / extents to data
```

Nama file sendiri dikelola melalui struktur directory yang menghubungkan filename dengan inode.

Secara sederhana:
```text
Directory
    ↓
Filename
    ↓
Inode
    ↓
File Data
```

Ini berbeda dengan model mental sederhana:
```text
filename → file
```

Filesystem sebenarnya jauh lebih terstruktur.