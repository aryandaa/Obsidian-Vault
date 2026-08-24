#tool 

`binwalk` adalah salah satu hidden gem paling overpower dalam forensic. Ia digunakan untuk **memindai file binary dan menemukan file atau struktur yang tertanam di dalamnya**. Sering kali sebuah file "polos" ternyata berisi file lain: ZIP di dalam JPEG, firmware di dalam binary, atau script di dalam gambar.

Secara konsep:

```text
File mencurigakan
    ↓
Pindai seluruh byte
    ↓
Cocokkan dengan database signature
    ↓
Temukan file yang tertanam
```

`foremost` dan `scalpel` memang bisa carving, tetapi `binwalk` jauh lebih teliti dalam mendeteksi struktur tertanam, termasuk kompresi, firmware, dan file system image.

---
## 1. Instalasi

```bash
sudo apt update
sudo apt install binwalk
```

Beberapa fitur ekstraksi membutuhkan dependency tambahan. Untuk penggunaan umum di CTF, install juga:

```bash
sudo apt install unzip p7zip-full
```

Verifikasi:

```bash
binwalk --help
```

---
# 2. Penggunaan Dasar

```bash
binwalk suspicious.jpg
```

Output menampilkan daftar signature yang ditemukan beserta offsetnya:

```text
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
134           0x86            Zip archive data, at least v2.0 to extract
```

Perhatikan: di dalam `suspicious.jpg` ternyata ada ZIP pada offset `0x86`. Ini bisa menjadi awal dari investigasi.

`binwalk` menampilkan:

```text
DESCRIPTION  → apa yang ditemukan
```

dan offset dalam decimal serta hex.

```
Kebiasaan baik: jalankan binwalk pada setiap file yang mencurigakan,
termasuk file yang terlihat normal. Data tersembunyi sering bersembunyi
di file yang tidak mencurigakan.
```

---
# 3. Ekstraksi dengan `-e`

```bash
-e
```

atau:

```bash
--extract
```

mengekstrak semua file yang ditemukan.

```bash
binwalk -e suspicious.jpg
```

Hasilnya diletakkan di directory:

```text
_suspicious.jpg.extracted/
```

Di dalamnya terdapat file yang berhasil diekstrak.

Untuk ekstraksi rekursif (mengekstrak file yang di dalam file yang diekstrak):

```bash
-M
```

atau:

```bash
--matryoshka
```

```bash
binwalk -Me suspicious.jpg
```

Ini akan terus membongkar sampai tidak ada lagi yang bisa diekstrak. Sangat berguna untuk archive bersarang.

```
binwalk -Me adalah cara termudah membongkar lapisan demi lapisan.
Seperti membuka kotak di dalam kotak, sampai tidak ada kotak lagi.
```

---
# 4. Flag `-y` dan `-x` (Filter)

```bash
-y <filter>
```

hanya menampilkan signature yang cocok dengan pola tertentu.

```bash
binwalk -y zip file.bin
```

hanya mencari ZIP.

```bash
-x <filter>
```

mengecualikan signature tertentu.

```bash
binwalk -x jpeg file.bin
```

mengabaikan hasil JPEG.

Filter ini berguna ketika output terlalu ramai dengan false positive.

---
# 5. Flag `-D` (Custom Extract)

`-D` memungkinkan aturan ekstraksi kustom berdasarkan tipe:

```bash
-D '<tipe>:<ekstensi>[:<command>]'
```

Contoh:

```bash
binwalk -D 'png:raw' file.bin
```

mengekstrak data PNG sebagai file dengan ekstensi `.raw`.

Untuk menentukan command yang dijalankan saat mengekstrak:

```bash
binwalk -D 'zip:zip:unzip %e -d extracted/'
```

`%e` adalah placeholder untuk file yang diekstrak.

---
# 6. Flag `-l` dan `-A`

```bash
-l <panjang>
```

membatasi berapa banyak data yang dipindai dari awal file.

```bash
-A
```

atau:

```bash
--opcodes
```

memindai file executable untuk menemukan opcode yang bisa dieksekusi. Berguna untuk membedakan data dan kode pada firmware atau binary.

---
# 7. Mengidentifikasi Entropy

Salah satu fitur menarik `binwalk` adalah analisis entropy:

```bash
-E
```

atau:

```bash
--entropy
```

menampilkan grafik entropy file. Daerah dengan entropy tinggi biasanya adalah data terkompresi atau terenkripsi, sedangkan entropy rendah biasanya data yang bisa dibaca atau struktur biasa.

```bash
binwalk -E suspicious.bin
```

Grafik entropy membantu menemukan bagian file yang "aneh", bahkan ketika signature tidak dikenali.

```
Entropy adalah radar untuk data tersembunyi. Daerah yang terlalu rapi
atau terlalu acak sering menjadi petunjuk.
```

---
# 8. Contoh Kasus

Kamu menemukan `photo.jpg` dari evidence.

```bash
file photo.jpg
```

```text
photo.jpg: JPEG image data
```

```bash
binwalk photo.jpg
```

```text
DECIMAL       HEXADECIMAL     DESCRIPTION
0             0x0             JPEG image data
1048576       0x100000        Zip archive data
```

Ada ZIP di offset `0x100000`.

```bash
binwalk -e photo.jpg
```

```bash
cd _photo.jpg.extracted/
```

```bash
ls
```

```text
100000.zip
```

```bash
unzip 100000.zip
```

Di dalamnya mungkin ada file yang menjadi evidence: dokumen, script, atau flag.

```
Pola serangan umum: penyerang menyisipkan archive ke dalam gambar agar
tidak mencurigakan. binwalk langsung membongkarnya.
```

---
# 9. Keterbatasan

- `binwalk` mengandalkan signature yang dikenali. Data tanpa signature jelas tidak terdeteksi.
- False positive sering terjadi; verifikasi dengan `file` dan `xxd`.
- Ekstraksi file terfragmentasi bisa gagal.

Untuk data yang dienkripsi atau diencode, `binwalk` tidak membantu. Itu saatnya menggunakan entropy analysis dan analisis manual.

---
# 10. Posisi dalam Workflow

```text
file evidence.bin
    ↓
strings evidence.bin
    ↓
binwalk evidence.bin
    ↓
Temukan file tertanam
    ↓
binwalk -Me evidence.bin
    ↓
Verifikasi hasil ekstraksi
```

`binwalk` berada di antara triage dan analisis mendalam. Ia menjawab pertanyaan: **"apakah ada sesuatu di dalam file ini?"**

---
# 11. Command yang Perlu Kamu Kuasai

```bash
binwalk <file>
```

```bash
binwalk -e <file>
```

```bash
binwalk -Me <file>
```

```bash
binwalk -y zip <file>
```

```bash
binwalk -E <file>
```

```bash
binwalk -D 'png:raw' <file>
```
