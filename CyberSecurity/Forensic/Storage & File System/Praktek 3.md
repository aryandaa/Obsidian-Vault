#latihan 

Sekarang kita mulai praktik filesystem menggunakan Linux.

Buat directory:
```bash
mkdir filesystem-lab
cd filesystem-lab
```

Buat beberapa file:
```bash
echo "Forensic evidence" > evidence.txt
echo "This is a normal file" > normal.txt
```

Lihat informasi filesystem:
```bash
df -T .
```

Kamu akan mendapatkan informasi mengenai filesystem yang digunakan oleh directory tersebut.

Kemudian lihat informasi file:
```bash
ls -lah
```

Kamu akan melihat ukuran dan metadata dasar file.

Kemudian:
```bash
stat evidence.txt
```

Perhatikan bagian seperti:
```text
Size
Access
Modify
Change
Birth
```

Tergantung filesystem dan environment, tidak semua timestamp selalu tersedia atau memiliki makna yang sama.

Ini penting karena nanti kita akan membahas timestamp secara khusus.

---
# Praktik File Signature

Sekarang lihat tipe file:
```bash
file evidence.txt
```

Kemungkinan hasilnya:
```text
evidence.txt: ASCII text
```

Sekarang buat sebuah file binary sederhana:
```bash
printf '\x89PNG\r\n\x1a\n' > fake.png
```

Kemudian:
```bash
file fake.png
```

Perhatikan bahwa command `file` menggunakan karakteristik isi file untuk mencoba mengidentifikasi tipe data.

File tersebut belum menjadi PNG yang valid hanya karena header-nya dibuat seperti PNG. Kita sengaja membuatnya untuk menunjukkan bahwa **file extension bukan satu-satunya cara menentukan file type**.

---
# Praktik Deleted File sederhana

Sekarang buat file:
```bash
echo "This file should be investigated" > deleted.txt
```

Kemudian:
```bash
cat deleted.txt
```

Setelah itu hapus:
```bash
rm deleted.txt
```

Sekarang:
```bash
ls
```

File tersebut sudah tidak terlihat.

Tetapi jangan langsung menyimpulkan bahwa data fisiknya sudah benar-benar hilang.

Dalam filesystem biasa, `rm` menghapus directory entry atau membuat ruang tersebut dapat digunakan kembali. Apakah data fisik masih dapat dipulihkan tergantung filesystem dan kondisi storage.

Pada lab sederhana seperti ini, kita belum akan mencoba recovery dari filesystem aktif. Kita akan melakukannya nanti menggunakan **forensic image**, karena itu jauh lebih mendekati workflow forensic yang benar.

---
# Menghubungkan dengan Case 01

Mulai dari sini kita akan mulai membangun kasus utama kita.

Untuk sementara struktur case kita:
```text
CASE-01/
├── evidence/
│   ├── evidence.txt
│   └── evidence.sha256
│
└── notes/
    └── investigation.md
```

Nanti struktur tersebut akan berkembang menjadi:

```text
CASE-01/
├── evidence/
│   ├── disk.E01
│   ├── memory.raw
│   ├── traffic.pcap
│   └── suspicious_files/
│
├── extracted/
│   ├── files/
│   ├── metadata/
│   └── artifacts/
│
├── timeline/
│   └── timeline.csv
│
└── report/
    └── final-report.md
```

Kita belum membutuhkan semua file tersebut sekarang. Itu akan datang bertahap.

Untuk tahap ini, yang perlu kamu pahami adalah bahwa **disk image nantinya menjadi sumber utama Case 01**. Dari disk tersebut kita akan belajar menemukan filesystem, partition, file, metadata, deleted data, dan berbagai artifact.
