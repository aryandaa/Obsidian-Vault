#tool 

Kalau kamu hanya boleh membawa satu tool untuk memindai disk image dalam waktu singkat, bawa **bulk_extractor**. Ini adalah hidden gem paling overpower dalam digital forensics. Ia memindai seluruh data mentah (bukan hanya file yang terlihat) dan mengekstrak artefak seperti email, URL, alamat IP, nomor telepon, nomor kartu kredit, kunci AES, string base64, dan masih banyak lagi.

Keunggulan terbesarnya: bulk_extractor **tidak membutuhkan filesystem yang sehat**. Ia membaca byte demi byte, sehingga tetap bekerja pada image yang rusak, unallocated space, slack space, dan file yang sudah dihapus.

```text
Disk image (atau file apa pun)
    ↓
Pindai semua byte
    ↓
Terapkan banyak scanner sekaligus
    ↓
Hasilkan file teks per kategori artefak
```

---
## 1. Instalasi

```bash
sudo apt update
sudo apt install bulk-extractor
```

Verifikasi:

```bash
bulk_extractor --version
```

---
# 2. Penggunaan Dasar

```bash
bulk_extractor evidence.img -o output/
```

`-o` wajib diisi: directory untuk hasil.

Prosesnya bisa berjalan lama untuk image besar, tetapi hasilnya sangat berharga. Setelah selesai, directory output berisi banyak file teks:

```text
output/
├── email.txt
├── url.txt
├── ip.txt
├── telephone.txt
├── creditcard.txt
├── pii.txt
├── aes_keys.txt
├── base64.txt
├── zip.txt
├── domain.txt
└── report.xml
```

Setiap file berisi daftar artefak yang ditemukan beserta offsetnya.

```
bulk_extractor bekerja seperti menyisir pantai dengan metal detector:
semua yang mencurigakan dikumpulkan, lalu kamu yang memilah.
```

---
# 3. Membaca Hasil

Contoh `email.txt`:

```text
bobby@example.com  [offset 1048576]
attacker@malicious.net  [offset 2097152]
```

Contoh `url.txt`:

```text
http://malicious.example.com/payload.exe  [offset 3145728]
```

Contoh `ip.txt`:

```text
192.168.1.10  [offset 1048576]
203.0.113.42  [offset 4194304]
```

Offset menunjukkan posisi artefak di dalam image, yang bisa kamu gunakan untuk kembali ke lokasi tersebut:

```bash
dd if=evidence.img bs=1 skip=4194304 count=64 | xxd
```

---
# 4. Scanner yang Tersedia

Untuk melihat daftar scanner:

```bash
bulk_extractor --help
```

Beberapa scanner yang paling sering berguna:

```text
email      → alamat email
url        → URL
ip         → alamat IP
domain     → nama domain
telephone  → nomor telepon
creditcard → nomor kartu kredit
ssn        → nomor jaminan sosial
pii        → informasi pribadi
aes_keys   → kandidat kunci AES
base64     → string base64 yang mencurigakan
zip        → arsip ZIP
gzip       → arsip gzip
rar        → arsip RAR
exif       → metadata EXIF
windirs    → path Windows
```

Dengan memindai sekaligus, kamu bisa langsung mendapat gambaran besar isi evidence.

---
# 5. Flag `-x` (Exclude Scanner)

Tidak semua scanner diperlukan setiap saat.

```bash
-x <scanner>
```

menonaktifkan scanner tertentu.

```bash
bulk_extractor evidence.img -o output/ -x telephone -x ssn
```

Bisa mempercepat proses ketika kamu tahu artefak yang dicari.

Untuk mematikan semua scanner lalu mengaktifkan beberapa:

```bash
bulk_extractor evidence.img -o output/ -x all -e email
```

```
Kombinasi -x all dan -e <scanner> memberikan kontrol penuh
terhadap scanner yang dijalankan.
```

---
# 6. Flag `-S` (Settings)

```bash
-S <setting>
```

mengubah pengaturan scanner.

Contoh umum: mengubah ambang entropi base64:

```bash
bulk_extractor evidence.img -o output/ -S base64_entropy=3.0
```

Daftar pengaturan bisa dilihat di dokumentasi atau dengan `--help`.

---
# 7. Flag `-R` (Resume)

```bash
-R <directory>
```

melanjutkan proses yang terhenti. bulk_extractor menyimpan state, sehingga proses bisa dilanjutkan tanpa mulai dari nol.

```bash
bulk_extractor evidence.img -o output/ -R output/
```

Ini penting untuk image besar yang prosesnya terputus.

---
# 8. `bulk_extractor` pada Memory Dump

bulk_extractor juga bekerja pada memory dump:

```bash
bulk_extractor memory.raw -o mem_out/
```

Hasilnya bisa berisi email, URL, kredensial, dan command yang ada di memory pada saat dump diambil. Ini pelengkap yang sangat kuat untuk memory forensics dengan Volatility.

---
# 9. Kenapa Ini Overpower?

Alasan utama bulk_extractor sangat kuat:

1. **Tidak butuh filesystem sehat.** Image rusak, partition hilang, tetap bisa dipindai.
2. **Menjangkau unallocated space.** Data yang sudah dihapus tetap terdeteksi selama byte-nya belum tertimpa.
3. **Banyak scanner sekaligus.** Satu kali jalan, banyak kategori artefak.
4. **Parallel processing.** Bisa menggunakan banyak core untuk mempercepat.
5. **Hasil terstruktur.** File teks per kategori mudah diproses dengan `grep`.

```
Ketika kamu tidak tahu harus mulai dari mana pada image besar,
jalankan bulk_extractor. Hasilnya memberi peta awal yang sangat berharga.
```

---
# 10. Posisi dalam Workflow

```text
mmls / file evidence.img
    ↓
bulk_extractor evidence.img -o out/
    ↓
grep hasil: email, url, ip
    ↓
Kembali ke offset dengan dd / xxd
    ↓
Analisis mendalam artifact tertentu
```

bulk_extractor adalah alat triage paling efisien. Ia tidak menggantikan analisis mendalam, tetapi ia menemukan petunjuk yang bisa menjadi titik awal.

---
# 11. Command yang Perlu Kamu Kuasai

```bash
bulk_extractor evidence.img -o output/
```

```bash
grep -i "flag\|secret" output/*
```

```bash
bulk_extractor evidence.img -o output/ -x telephone -x ssn
```

```bash
bulk_extractor evidence.img -o output/ -R output/
```

```bash
bulk_extractor memory.raw -o mem_out/
```
