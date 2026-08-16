#tool 

Kalau `file` membantu kita menjawab **“ini benda apa?”**, maka `lsblk` membantu menjawab **“storage apa saja yang sedang terhubung ke sistem ini dan bagaimana strukturnya?”**

Ini penting dalam forensic karena sebelum menganalisis storage, kita harus tahu dulu apa saja block device yang tersedia. Linux memperlakukan hard disk, SSD, USB drive, virtual disk, dan beberapa jenis storage lain sebagai **block device**. `lsblk` membaca informasi tersebut dan menampilkannya dalam bentuk struktur tree.

Secara sederhana:

```text
Computer
├── /dev/sda
│   ├── /dev/sda1
│   └── /dev/sda2
│
└── /dev/sdb
    └── /dev/sdb1
```

Misalnya `/dev/sda` adalah disk utama dan `/dev/sda1` serta `/dev/sda2` adalah partition di dalamnya. `/dev/sdb` mungkin USB drive.

Dalam forensic, informasi seperti ini sangat penting karena kita harus bisa membedakan **disk**, **partition**, **filesystem**, dan **mount point**. Jangan sampai investigator melakukan imaging terhadap `/dev/sda1` padahal evidence yang dibutuhkan sebenarnya seluruh `/dev/sda`. Kesalahan seperti ini bukan sekadar typo, karena bisa membuat sebagian evidence tidak ikut dianalisis.

---
## 1. Instalasi

Di Debian/Kali/Ubuntu, `lsblk` biasanya sudah tersedia karena berasal dari package `util-linux`.

Coba:

```bash
lsblk --version
```

Kemudian:

```bash
which lsblk
```

Biasanya:

```text
/usr/bin/lsblk
```

Kalau belum tersedia:

```bash
sudo apt update
sudo apt install util-linux
```

Kemudian:

```bash
lsblk --version
```

---

# 2. Penggunaan Dasar

Command paling sederhana:

```bash
lsblk
```

Contoh output:

```text
NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sda           8:0    0   100G  0 disk
├─sda1        8:1    0    96G  0 part /
└─sda2        8:2    0     4G  0 part [SWAP]
sdb           8:16   1    32G  0 disk
└─sdb1        8:17   1    32G  0 part /media/user/USB
```

Jangan langsung menghafalkan output ini. Kita bedah.

`NAME` menunjukkan nama block device.

```text
sda
├─sda1
└─sda2
```

Artinya:

```text
/dev/sda
```

adalah disk dan:

```text
/dev/sda1
/dev/sda2
```

adalah partition di dalamnya.

`SIZE` menunjukkan ukuran device.

`TYPE` menunjukkan jenisnya. Yang paling penting untuk sekarang:

```text
disk
part
```

`MOUNTPOINTS` menunjukkan lokasi filesystem tersebut sedang di-mount.

---

# 3. Memahami `/dev/sda`

Kalau kamu melihat:

```text
sda
```

biasanya device tersebut berada di:

```text
/dev/sda
```

Sedangkan:

```text
sda1
```

adalah:

```text
/dev/sda1
```

Ini merupakan naming convention Linux untuk block device.

Pada sistem modern, kamu juga bisa menemukan:

```text
/dev/nvme0n1
/dev/nvme0n1p1
/dev/nvme0n1p2
```

Untuk NVMe, penamaannya memang sedikit berbeda.

Contoh:

```text
nvme0n1
├─nvme0n1p1
└─nvme0n1p2
```

berarti:

```text
/dev/nvme0n1
/dev/nvme0n1p1
/dev/nvme0n1p2
```

---

# 4. Kenapa `lsblk` Penting untuk Forensic?

Misalnya kamu memasang USB drive yang berisi evidence.

Setelah USB dicolok, kamu menjalankan:

```bash
lsblk
```

Kemudian muncul:

```text
sda      500G disk
├─sda1   450G part /
└─sda2    50G part

sdb       32G disk
└─sdb1    32G part /media/yanda/EVIDENCE
```

Kita bisa melihat bahwa:

```text
/dev/sdb
```

adalah disk 32 GB.

Dan:

```text
/dev/sdb1
```

adalah partition 32 GB yang sedang di-mount.

Kalau tujuan kita melakukan forensic acquisition terhadap **seluruh disk**, target yang relevan adalah:

```text
/dev/sdb
```

bukan:

```text
/dev/sdb1
```

Karena `/dev/sdb` bisa mengandung partition table, filesystem, unallocated space, dan struktur lain yang tidak semuanya berada di dalam satu partition.

Ini konsep yang nanti akan sangat penting ketika kita masuk `dd`, `dc3dd`, dan forensic imaging.

---

# 5. Flag `-f`

Sekarang kita mulai CLI flags.

Flag pertama:

```bash
lsblk -f
```

`-f` berarti menampilkan informasi filesystem.

Contohnya:

```text
NAME        FSTYPE FSVER LABEL    UUID                                 FSAVAIL FSUSE% MOUNTPOINTS
sda
├─sda1      ext4   1.0            1234-5678                            80G     15%   /
└─sda2      swap   1              abcd-efgh                                             [SWAP]
sdb
└─sdb1      ntfs         EVIDENCE 9ABC-1234                                      /media/user/EVIDENCE
```

Sekarang informasi yang kita dapat jauh lebih berguna.

Kita bisa melihat:

```text
FSTYPE
```

yang memberitahu filesystem.

Misalnya:

```text
ext4
ntfs
vfat
exfat
swap
```

`LABEL` menunjukkan filesystem label.

`UUID` menunjukkan identifier filesystem.

Ini sangat berguna ketika melakukan forensic karena device name seperti `/dev/sdb1` dapat berubah tergantung bagaimana storage terdeteksi oleh sistem.

UUID dapat membantu mengidentifikasi filesystem secara lebih konsisten.

---

# 6. Flag `-o`

Flag:

```bash
lsblk -o
```

digunakan untuk memilih kolom yang ingin ditampilkan.

Misalnya:

```bash
lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINTS
```

Output akan lebih sederhana:

```text
NAME        SIZE TYPE FSTYPE MOUNTPOINTS
sda         100G disk
├─sda1       96G part ext4   /
└─sda2        4G part swap   [SWAP]
sdb          32G disk
└─sdb1       32G part ntfs   /media/user/EVIDENCE
```

Ini sangat berguna ketika kamu tidak membutuhkan semua informasi default.

Beberapa kolom penting:

```text
NAME
SIZE
TYPE
FSTYPE
FSVER
LABEL
UUID
MOUNTPOINT
MOUNTPOINTS
RO
RM
```

---

# 7. Flag `-p`

Secara default, `lsblk` menampilkan:

```text
sda
├─sda1
└─sda2
```

Dengan:

```bash
lsblk -p
```

hasilnya akan menggunakan path lengkap:

```text
/dev/sda
├─/dev/sda1
└─/dev/sda2
```

Ini sangat berguna ketika command output akan langsung digunakan dalam workflow berikutnya.

Misalnya kamu sedang mengidentifikasi device untuk acquisition.

Daripada harus mengubah:

```text
sdb1
```

menjadi:

```text
/dev/sdb1
```

secara manual, `-p` sudah memberikan path lengkap.

---

# 8. Flag `-l`

Flag:

```bash
lsblk -l
```

berarti **list format**.

Alih-alih tree:

```text
sda
├─sda1
└─sda2
```

output dibuat lebih datar:

```text
sda
sda1
sda2
```

Ini berguna untuk script atau ketika struktur tree justru membuat output sulit diproses.

Bandingkan:

```bash
lsblk
```

dengan:

```bash
lsblk -l
```

Kamu akan langsung melihat perbedaannya.

---

# 9. Flag `-n`

Flag:

```bash
lsblk -n
```

berarti tidak menampilkan header.

Tanpa:

```text
NAME SIZE TYPE
sda  100G disk
```

Dengan:

```bash
lsblk -n
```

menjadi:

```text
sda 100G disk
```

Ini berguna ketika output akan diproses oleh shell script.

Contohnya:

```bash
lsblk -n -o NAME
```

akan menghasilkan daftar device tanpa header.

---

# 10. Flag `-r`

Flag:

```bash
lsblk -r
```

digunakan untuk **raw list format**.

Ini menghilangkan tree formatting.

Misalnya:

```bash
lsblk -r -o NAME,TYPE,SIZE
```

bisa menghasilkan:

```text
sda disk 100G
sda1 part 96G
sda2 part 4G
sdb disk 32G
sdb1 part 32G
```

Format seperti ini lebih mudah diproses menggunakan:

```text
awk
grep
cut
sort
```

yang nanti juga akan kita gunakan dalam automation forensic.

---

# 11. Flag `-a`

Flag:

```bash
lsblk -a
```

menampilkan semua device, termasuk device yang biasanya tidak terlihat dalam output normal.

Ini berguna ketika kamu ingin mendapatkan inventory yang lebih lengkap.

Dalam forensic environment, jangan langsung menganggap device yang tidak muncul pada output default berarti tidak ada. `lsblk` memiliki behavior filtering tertentu, sehingga memahami `-a` penting.

---

# 12. Flag `-d`

Flag:

```bash
lsblk -d
```

menampilkan hanya **disk**, bukan partition turunannya.

Misalnya normal:

```text
sda
├─sda1
└─sda2
sdb
└─sdb1
```

Dengan:

```bash
lsblk -d
```

menjadi:

```text
sda
sdb
```

Ini sangat berguna ketika kamu hanya ingin melihat daftar physical/virtual disks.

Misalnya:

```bash
lsblk -d -o NAME,SIZE,MODEL,SERIAL
```

bisa memberikan inventory disk yang jauh lebih berguna untuk identification.

---

# 13. Flag `-J`

Ini salah satu flag yang sangat berguna kalau nanti kamu membuat automation.

```bash
lsblk -J
```

menghasilkan output JSON.

Contohnya secara struktur:

```json
{
  "blockdevices": [
    {
      "name": "sda",
      "size": "100G",
      "type": "disk"
    }
  ]
}
```

Ini menarik karena JSON dapat diproses menggunakan:

```bash
jq
```

atau Python.

Misalnya:

```bash
lsblk -J | jq
```

Nanti ketika kita sudah masuk scripting cybersecurity, konsep seperti ini akan sangat berguna.

Tool CLI menghasilkan data terstruktur, lalu program kita mengolah data tersebut.

---

# 14. Flag `-b`

Secara default ukuran storage biasanya ditampilkan dalam format human-readable.

Contohnya:

```text
100G
32G
512M
```

Dengan:

```bash
lsblk -b
```

ukuran diberikan dalam bytes.

Misalnya:

```text
100000000000
```

Ini penting ketika kamu membutuhkan angka yang presisi untuk automation atau perhitungan forensic.

---

# 15. Flag `-m`

Flag:

```bash
lsblk -m
```

menampilkan informasi permission dan ownership.

Misalnya:

```text
NAME        OWNER GROUP MODE
sda         root  disk  brw-rw----
```

Ini lebih berguna ketika kita ingin memahami bagaimana device tersebut diperlakukan oleh sistem Linux.

Untuk forensic storage, informasi permission device juga dapat membantu memahami siapa yang memiliki akses terhadap block device.

---

# 16. Flag `-S`

Ada juga:

```bash
lsblk -S
```

yang menampilkan informasi mengenai **SCSI devices**.

Output dapat mencakup informasi seperti:

```text
NAME HCTL       TYPE VENDOR MODEL SERIAL
sda  0:0:0:0    disk ATA   ...
sdb  1:0:0:0    disk USB   ...
```

Ini berguna untuk hardware/storage identification.

---

# 17. Kombinasi Flag yang Penting

Dalam praktik, kita jarang menggunakan satu flag saja.

Contoh:

```bash
lsblk -f
```

untuk filesystem.

Atau:

```bash
lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINTS
```

untuk inventory yang bersih.

Untuk physical disk:

```bash
lsblk -d -o NAME,SIZE,MODEL,SERIAL
```

Untuk automation:

```bash
lsblk -J
```

Untuk path lengkap:

```bash
lsblk -p -f
```

Untuk melihat semuanya secara lebih lengkap:

```bash
lsblk -a -f
```

Kamu harus mulai terbiasa membaca kombinasi option seperti ini, bukan hanya menghafalkan command tunggal.

---

# 18. `lsblk` dan Forensic Evidence

Sekarang kita hubungkan dengan forensic workflow.

Misalnya kamu punya komputer forensic workstation dan memasukkan USB evidence.

Kamu jalankan:

```bash
lsblk
```

Kemudian:

```bash
lsblk -f
```

Lalu:

```bash
lsblk -d -o NAME,SIZE,MODEL,SERIAL
```

Tujuannya adalah mengidentifikasi:

```text
Device apa?
Ukuran berapa?
Disk atau partition?
Filesystem apa?
Apakah sedang mounted?
Model storage apa?
Serial number apa?
```

Informasi tersebut bisa menjadi bagian dari **evidence identification**.

Kemudian baru kita masuk ke acquisition:

```text
Device Identification
        ↓
lsblk
        ↓
Identify Evidence
        ↓
Write Blocker / Read-only Environment
        ↓
Imaging
        ↓
Hash Verification
        ↓
Forensic Analysis
```

Kita belum melakukan imaging sekarang. Itu akan kita bahas saat masuk `dd`, `dc3dd`, dan tool acquisition lainnya.

---

# 19. Hal Penting: Jangan Sembarangan Menyentuh Evidence

Ini bagian yang harus kamu biasakan sejak sekarang.

Kalau kamu melihat:

```text
/dev/sdb
```

jangan melakukan eksperimen seperti:

```bash
sudo mkfs /dev/sdb
```

atau:

```bash
sudo mount /dev/sdb1 ...
```

terhadap evidence asli.

`lsblk` sendiri aman karena sifatnya hanya membaca informasi block device. Tetapi command berikutnya bisa mengubah evidence.

Dalam forensic, prinsip dasarnya adalah menjaga **integrity** evidence.

Untuk lab kita, gunakan disk image atau media yang memang sengaja dibuat untuk latihan. Jangan menggunakan disk utama laptopmu sebagai bahan praktikum hanya karena rasa penasaran sedang mengalahkan survival instinct.