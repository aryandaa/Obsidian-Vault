#tool 

Sekarang kita masuk ke tool yang menjaga kepercayaan seluruh proses forensic: **hashing**. `sha256sum` dan `hashdeep` digunakan untuk memverifikasi integrity evidence. Kalau `file`, `strings`, dan `xxd` membantu kita menemukan informasi, maka hashing membantu kita membuktikan bahwa evidence yang kita analisis **masih sama dengan evidence awal**.

Secara konsep:

```text
File
 ↓
Fungsi hash (SHA-256)
 ↓
Nilai hex unik
 ↓
Isi berubah → hash berubah
```

Hash adalah sidik jari digital. Dua file dengan isi yang sama menghasilkan hash yang sama. Satu bit saja berubah, hash langsung berbeda.

---
## 1. Instalasi

`sha256sum` berasal dari package `coreutils`, sudah pasti tersedia di distro manapun.

```bash
sha256sum --version
```

`hashdeep` perlu diinstall:

```bash
sudo apt update
sudo apt install hashdeep
```

Verifikasi:

```bash
hashdeep --version
```

---
# 2. Penggunaan Dasar `sha256sum`

```bash
sha256sum evidence.img
```

Output:

```text
a1b2c3d4e5f6...aabbccdd  evidence.img
```

Untuk beberapa file:

```bash
sha256sum evidence1.img evidence2.img
```

Untuk seluruh isi directory:

```bash
sha256sum *
```

Varian lain yang perlu kamu kenali:

```bash
md5sum file
```

```bash
sha1sum file
```

Untuk forensic, **SHA-256 adalah standar yang paling umum** karena kecepatan dan keamanannya. MD5 dan SHA-1 sudah dianggap lemah untuk integritas serius, tetapi masih sering muncul di soal CTF.

---
# 3. Membuat File Checksum

```bash
sha256sum * > hashes.txt
```

Isi `hashes.txt`:

```text
a1b2c3...  evidence1.img
d4e5f6...  evidence2.img
```

File checksum ini sendiri bisa menjadi bagian dari dokumentasi chain of custody.

---
# 4. Verifikasi dengan `-c`

```bash
-c
```

atau:

```bash
--check
```

memverifikasi hash yang tersimpan di file checksum.

```bash
sha256sum -c hashes.txt
```

Output:

```text
evidence1.img: OK
evidence2.img: FAILED
```

Jika ada file yang berubah, akan muncul `FAILED`. Ini adalah cara standar untuk memastikan evidence tidak berubah setelah disalin atau disimpan.

```
Kebiasaan forensic: hash evidence sebelum analisis, simpan hasilnya,
lalu hash lagi setelah analisis. Dua nilai harus sama.
```

---
# 5. Kenapa Hash Penting dalam Workflow Imaging

Ketika membuat forensic image dengan `dd`:

```text
Evidence asli
    ↓
Hash sebelum imaging
    ↓
dd (imaging)
    ↓
Hash hasil imaging
    ↓
Bandingkan kedua hash
```

Jika hash sama, image adalah salinan yang akurat. Jika beda, ada yang salah: sektor gagal dibaca, media rusak, atau kesalahan command.

Contoh praktik:

```bash
sha256sum /dev/sdb > hash_asli.txt
```

```bash
sudo dd if=/dev/sdb of=evidence.img bs=4M status=progress
```

```bash
sha256sum evidence.img > hash_image.txt
```

```bash
diff hash_asli.txt hash_image.txt
```

Tidak ada output dari `diff` berarti kedua hash sama.

---
# 6. Pengenalan `hashdeep`

`hashdeep` adalah tool yang lebih kuat. Ia bisa menghitung beberapa algoritma hash sekaligus, bekerja secara rekursif, dan yang paling penting: **mode audit**.

Penggunaan dasar:

```bash
hashdeep -c md5,sha1,sha256 evidence.img
```

Menghitung tiga hash sekaligus.

```bash
hashdeep -r evidence_directory/
```

Rekursif ke seluruh directory.

Output `hashdeep` berformat:

```text
%%%% HASHDEEP-1.0
%%%% size,md5,sha1,sha256,filename
## Invoked from: /home/user
## $ hashdeep ...
1024,1a2b3c...,4d5e6f...,7a8b9c...,evidence.txt
```

---
# 7. Flag `-e` (Audit Mode)

Ini hidden gem utama dari `hashdeep`.

```bash
-e
```

atau:

```bash
--audit
```

membandingkan file yang sedang diperiksa dengan daftar hash yang diketahui, lalu melaporkan file mana yang **sama, berubah, baru, atau hilang**.

```bash
hashdeep -e -k known_hashes.txt evidence_directory/
```

Output:

```text
Evidence directory: evidence_directory/
## Files Processed: 12
## New files: 2
## Files with hashes: 10
## Files with mismatched hashes: 1
## Files with missing hashes: 0
```

Fitur ini sangat berguna untuk:

- Memverifikasi hasil imaging tetap konsisten.
- Memantau apakah evidence berubah selama penyimpanan.
- Membandingkan dua salinan directory.

---
# 8. Flag `-k` (Known Hashes)

```bash
-k <file>
```

menggunakan file hash sebagai referensi.

```bash
hashdeep -k baseline.txt -r evidence/
```

Perhatikan bahwa file referensi harus dalam format `hashdeep` (bukan format `sha256sum` biasa).

---
# 9. Flag `-m` dan `-a`

```bash
-m
```

atau:

```bash
--match
```

hanya menampilkan file yang cocok dengan daftar hash.

```bash
-a
```

atau:

```bash
--add
```

menambahkan hash ke file referensi.

Contoh membangun baseline:

```bash
hashdeep -r evidence/ > baseline.txt
```

Kemudian di waktu lain:

```bash
hashdeep -e -k baseline.txt -r evidence/
```

untuk memeriksa apakah ada yang berubah.

---
# 10. Hash untuk File yang Sudah Dihapus

Hash tidak hanya untuk file yang masih ada. Kalau kamu menemukan file yang diduga sudah dihapus, kamu bisa menghitung hash data yang dipulihkan dan membandingkannya dengan hash yang terdokumentasi di tempat lain (misalnya di log, manifest, atau challenge description). Ini cara membuktikan bahwa data yang kamu pulihkan memang file yang dicari.

---
# 11. Posisi Hashing dalam Workflow Forensic

```text
Collection
    ↓
Hash evidence (sebelum)
    ↓
Examination & Analysis
    ↓
Hash evidence (sesudah)
    ↓
Bandingkan
    ↓
Reporting
```

Hashing bukan alat untuk menemukan flag, tetapi ia adalah **pengaman seluruh proses**. Tanpa hash, kamu tidak bisa membuktikan bahwa evidence yang kamu analisis masih asli dan tidak berubah.

---
# 12. Command yang Perlu Kamu Kuasai

```bash
sha256sum <file>
```

```bash
sha256sum * > hashes.txt
```

```bash
sha256sum -c hashes.txt
```

```bash
hashdeep -c md5,sha1,sha256 <file>
```

```bash
hashdeep -r <directory>/
```

```bash
hashdeep -e -k baseline.txt -r <directory>/
```
