#tool 

Setelah mengidentifikasi evidence dengan `lsblk` dan memastikan integrity dengan hash, langkah berikutnya adalah **acquisition**, yaitu membuat salinan forensik dari evidence. Tool utama untuk ini adalah `dd`, dan versi forensic-nya: `dcfldd` dan `dc3dd`.

Penting untuk dipahami sejak awal: dalam forensic, kita **tidak menganalisis evidence asli**. Kita membuat image, lalu menganalisis image tersebut. Image adalah salinan bit-for-bit dari media penyimpanan.

```
Media penyimpanan /dev/sdb
    ↓
dd / dcfldd
    ↓
evidence.img (salinan bit-for-bit)
    ↓
Analisis terhadap image, bukan media asli
```

---
## 1. Instalasi

`dd` berasal dari `coreutils`, sudah pasti tersedia.

```bash
dd --version
```

`dcfldd` dan `dc3dd` perlu diinstall:

```bash
sudo apt update
sudo apt install dcfldd dc3dd
```

Verifikasi:

```bash
dcfldd --version
```

```bash
dc3dd --version
```

---
# 2. Penggunaan Dasar `dd`

Syntax `dd` berbeda dari command biasa. Ia menggunakan format `if=` (input file) dan `of=` (output file):

```bash
sudo dd if=/dev/sdb of=evidence.img
```

Ini menyalin seluruh isi `/dev/sdb` ke `evidence.img`.

Contoh lain yang sering dipakai:

```bash
sudo dd if=/dev/sdb1 of=partition1.img bs=4M status=progress
```

Perhatikan `bs=4M`. Ini adalah block size, menentukan berapa banyak data dibaca sekaligus. Untuk disk besar, block size yang lebih besar membuat proses lebih cepat.

`status=progress` menampilkan progres transfer.

```
Sebelum menjalankan dd, pastikan dengan lsblk bahwa kamu menyalin device
yang benar. Satu kesalahan penulisan if/of bisa menghancurkan evidence
atau menghapus data di mesinmu sendiri.
```

---
# 3. Flag Penting `dd`

```bash
bs=<ukuran>
```

block size, misalnya `bs=4M`.

```bash
count=<jumlah>
```

jumlah block yang disalin. Berguna untuk mengambil sebagian image (misalnya untuk triage cepat).

```bash
skip=<jumlah>
```

melewati sejumlah block pada input. Berguna untuk mengambil partition tertentu dari image tanpa membaca seluruh disk.

```bash
seek=<jumlah>
```

melewati sejumlah block pada output.

```bash
iflag=fullblock
```

memastikan setiap operasi membaca block penuh. Penting saat membaca dari pipe atau device.

```bash
conv=noerror,sync
```

ini adalah kombinasi paling penting untuk forensic:

```text
noerror  → terus lanjut meskipun ada error baca
sync     → isi block yang gagal dibaca dengan null byte
```

Tanpa `noerror,sync`, satu sektor rusak bisa menghentikan seluruh proses imaging. Dengan kombinasi ini, image tetap terbentuk dan posisi data tetap selaras, hanya bagian yang rusak yang terisi byte nol.

---
# 4. Contoh Imaging yang Benar

```bash
sudo dd if=/dev/sdb of=evidence.img bs=4M conv=noerror,sync iflag=fullblock status=progress
```

Setelah selesai, verifikasi:

```bash
sha256sum /dev/sdb evidence.img
```

Perlu diperhatikan: menghitung hash `/dev/sdb` langsung membutuhkan membaca seluruh device. Ini normal dan sah dilakukan selama device tidak sedang berubah.

---
# 5. Mengambil Satu Partition dari Image

Jika kamu punya image penuh dan hanya butuh satu partition:

```bash
fdisk -l evidence.img
```

melihat daftar partition dan offsetnya. Kemudian:

```bash
sudo dd if=evidence.img of=partition2.img bs=512 skip=<offset_partition> count=<jumlah_sector>
```

`bs=512` dipakai karena offset partition biasanya dihitung dalam sector 512 byte. `skip` menentukan mulai dari sector mana, `count` menentukan berapa sector.

Cara ini berguna ketika kamu tidak ingin menganalisis seluruh disk.

---
# 6. `dcfldd`: dd dengan Hash Terintegrasi

`dcfldd` adalah versi forensic dari `dd`. Keunggulannya: **menghitung hash sambil menyalin**, sehingga tidak perlu membaca data dua kali.

```bash
sudo dcfldd if=/dev/sdb of=evidence.img bs=4M hash=sha256 hashlog=hash.txt status=on
```

Output:

```text
 blocks (X bytes) copied.
SHA256 (evidence.img) = a1b2c3...
```

Flag utama `dcfldd`:

```bash
hash=sha256
```

algoritma hash yang dihitung.

```bash
hashlog=<file>
```

menyimpan hash ke file.

```bash
hashwindow=<jumlah>
```

menghitung hash per blok interval (untuk verifikasi bertahap).

```bash
status=on
```

menampilkan progres.

```bash
vf=<file>
```

memverifikasi output terhadap file hash.

Contoh verifikasi:

```bash
dcfldd if=evidence.img vf=hash.txt
```

---
# 7. `dc3dd`: Versi yang Lebih Forensic

`dc3dd` adalah pengembangan dari `dcfldd` yang menambahkan fitur logging yang lebih baik:

```bash
sudo dc3dd if=/dev/sdb of=evidence.img bs=4M hash=sha256 hashlog=hash.txt log=acquisition.log status=on
```

Keunggulan `dc3dd`:

```bash
log=<file>
```

menyimpan catatan seluruh proses (command, waktu, error) ke file log. Log ini bisa menjadi bagian dari chain of custody.

```bash
ofsz=<ukuran>
```

membatasi ukuran output (berguna untuk membagi image menjadi beberapa bagian).

```bash
errlog=<file>
```

menyimpan error baca secara terpisah.

```bash
count=<jumlah>
```

```bash
skip=<jumlah>
```

sama seperti `dd`.

---

# 8. Format Image Lain: E01

`dd` menghasilkan image mentah (raw). Format lain yang sering dipakai di dunia forensic adalah **E01** (EnCase Evidence File) yang menyimpan metadata dan hash di dalam file image-nya sendiri.

Tool untuk membuat E01 adalah `ewfacquire` dari package `libewf`:

```bash
sudo apt install ewf-tools
```

```bash
sudo ewfacquire /dev/sdb -t evidence
```

Hasilnya berupa file dengan ekstensi `.E01` (atau `.E02`, `.E03` jika terbagi).

Untuk membuka E01:

```bash
ewfmount evidence.E01 mountpoint/
```

atau langsung dengan `ewfexport`:

```bash
ewfexport evidence.E01 -t exported
```

Di CTF, format raw (`img`, `dd`) lebih sering muncul karena lebih sederhana. Tetapi di dunia nyata, E01 adalah standar.

---
# 9. Posisi Acquisition dalam Workflow

```text
lsblk
 ↓
Identifikasi device evidence
 ↓
dd / dcfldd / dc3dd
 ↓
Image + hash
 ↓
Verifikasi hash
 ↓
Analisis image
```

Selalu catat: device apa yang di-image, kapan, dengan command apa, dan berapa hash hasilnya. Informasi ini yang membuat image dapat dipertanggungjawabkan.

---
# 10. Command yang Perlu Kamu Kuasai

```bash
sudo dd if=/dev/sdb of=evidence.img bs=4M conv=noerror,sync status=progress
```

```bash
sudo dcfldd if=/dev/sdb of=evidence.img bs=4M hash=sha256 hashlog=hash.txt status=on
```

```bash
sudo dc3dd if=/dev/sdb of=evidence.img bs=4M hash=sha256 hashlog=hash.txt log=acq.log status=on
```

```bash
dcfldd if=evidence.img vf=hash.txt
```

```bash
sha256sum /dev/sdb evidence.img
```
