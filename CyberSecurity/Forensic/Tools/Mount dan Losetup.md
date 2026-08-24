#tool 

Setelah membuat forensic image, muncul pertanyaan: **bagaimana cara melihat isinya?** Dua cara utama: menggunakan Sleuth Kit (yang tidak mengubah image sama sekali), atau melakukan mount. `mount` dan `losetup` digunakan untuk mengakses image seolah-olah ia adalah disk yang terpasang.

Penting: dalam forensic, mounting harus dilakukan dengan hati-hati karena sistem operasi bisa menulis ke filesystem (misalnya memperbarui access time). Prinsipnya: **mount read-only, atau gunakan tool yang memang tidak menulis apa pun**.

---
## 1. Instalasi

`mount` berasal dari `util-linux`, sudah pasti tersedia.

```bash
mount --version
```

Untuk filesystem NTFS, install `ntfs-3g`:

```bash
sudo apt update
sudo apt install ntfs-3g
```

Untuk exFAT:

```bash
sudo apt install exfat-fuse exfatprogs
```

Untuk beberapa filesystem, pastikan package-nya terinstall sebelum mount.

---
# 2. Mount Image Mentah (Raw Image)

Cara paling sederhana untuk image yang berisi satu filesystem:

```bash
mkdir -p /mnt/evidence
```

```bash
sudo mount -o ro,loop evidence.img /mnt/evidence
```

Penjelasan flag:

```text
-o ro   → read-only (wajib untuk forensic)
loop    → perlakukan file sebagai block device
```

Dengan `-o ro`, sistem tidak akan menulis ke filesystem image.

Untuk filesystem NTFS:

```bash
sudo mount -o ro,loop,noatime evidence_ntfs.img /mnt/evidence
```

```
noatime  → jangan perbarui access time
```

Setelah selesai, selalu unmount:

```bash
sudo umount /mnt/evidence
```

---
# 3. Mount dengan Offset: Image Berisi Partition Table

Masalahnya, banyak image berisi partition table (MBR/GPT) dengan beberapa partition di dalamnya. Mount langsung terhadap image tersebut akan gagal karena filesystem tidak dimulai dari sector 0.

Solusinya: mount partition tertentu menggunakan offset byte.

```bash
fdisk -l evidence.img
```

atau:

```bash
mmls evidence.img
```

untuk melihat offset partition dalam sector. Misalnya partition dimulai dari sector 2048:

```bash
sudo mount -o ro,loop,offset=$((512*2048)) evidence.img /mnt/evidence
```

`offset` harus dalam byte, sehingga sector dikalikan dengan ukuran sector (biasanya 512).

Jika partition dimulai dari sector 40960:

```bash
sudo mount -o ro,loop,offset=$((512*40960)) evidence.img /mnt/evidence
```

Cara ini bekerja tanpa perlu mengubah image.

---
# 4. `losetup`: Menjadikan Image sebagai Block Device

`losetup` menghubungkan file image dengan loop device, sehingga image diperlakukan seperti `/dev/loop0`. Ini lebih fleksibel daripada mount dengan offset manual.

```bash
sudo losetup -fP evidence.img
```

Flag:

```text
-f  → gunakan loop device yang kosong
-P  → pindai partition table di dalam image
```

Setelah ini, partition di dalam image tersedia sebagai:

```text
/dev/loop0
/dev/loop0p1
/dev/loop0p2
```

Lihat dengan:

```bash
lsblk
```

Sekarang kamu bisa mount partition tersebut seperti device biasa:

```bash
sudo mount -o ro /dev/loop0p1 /mnt/evidence
```

Melihat semua loop device:

```bash
losetup -a
```

Melepas loop device:

```bash
sudo losetup -d /dev/loop0
```

Jangan lupa unmount partition terlebih dahulu sebelum melepas loop device.

```
Losetup adalah jembatan antara image dan mount. Dengan -P, partition
di dalam image muncul secara otomatis, mirip seperti USB drive yang
dicolok ke mesin.
```

---
# 5. Mount Image E01

Image E01 bukan file mentah, sehingga tidak bisa langsung di-mount. Dua pilihan:

Konversi ke raw:

```bash
ewfexport evidence.E01 -t evidence_raw
```

atau gunakan `ewfmount` agar bisa di-mount sebagai loop device:

```bash
mkdir -p /mnt/ewf
```

```bash
sudo ewfmount evidence.E01 /mnt/ewf
```

Setelah itu `/mnt/ewf/ewf1` adalah representasi raw yang bisa di-mount:

```bash
sudo mount -o ro,loop /mnt/ewf/ewf1 /mnt/evidence
```

---
# 6. Mount vs Sleuth Kit

Mounting memang praktis, tetapi ada konsekuensi penting dalam forensic.

Keuntungan mount:

- Bisa melihat dan membuka file seperti biasa.
- Bisa menggunakan aplikasi GUI.

Kerugian mount:

- Sistem bisa menulis metadata (atime, journal) meskipun sudah `ro`.
- Mount tidak bisa melihat file yang dihapus di unallocated space.
- Mount tidak membaca struktur filesystem secara mendalam.

Sleuth Kit (fls, icat, istat) tidak melakukan mount sama sekali. Ia membaca struktur filesystem langsung dari image, sehingga **tidak ada risiko mengubah apa pun** dan bisa melihat file yang sudah dihapus.

```
Aturan praktis: untuk melihat cepat, gunakan mount read-only.
Untuk analisis serius dan file yang dihapus, gunakan Sleuth Kit.
```

---
# 7. Hal Penting: Jangan Mount Evidence Asli

Jika evidence adalah device fisik (`/dev/sdb`), jangan mount tanpa pengaman. Di dunia nyata, acquisition menggunakan write blocker. Di lab, kita selalu bekerja dengan image.

Kalau kamu terpaksa mount device, gunakan:

```bash
sudo mount -o ro,noatime /dev/sdb1 /mnt/evidence
```

Tetapi ingat: meskipun read-only, beberapa filesystem tetap menulis (misalnya journal NTFS dalam kondisi tertentu). Untuk kepastian, analisis image dengan Sleuth Kit.

---
# 8. Command yang Perlu Kamu Kuasai

```bash
sudo mount -o ro,loop evidence.img /mnt/evidence
```

```bash
sudo mount -o ro,loop,offset=$((512*2048)) evidence.img /mnt/evidence
```

```bash
sudo losetup -fP evidence.img
```

```bash
lsblk
```

```bash
sudo mount -o ro /dev/loop0p1 /mnt/evidence
```

```bash
sudo umount /mnt/evidence
```

```bash
sudo losetup -a
```

```bash
sudo losetup -d /dev/loop0
```
