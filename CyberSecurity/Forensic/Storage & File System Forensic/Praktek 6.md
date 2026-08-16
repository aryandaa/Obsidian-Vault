#latihan 

Alur praktiknya akan benar-benar seperti investigation kecil:
```text
disk.raw
   ↓
GPT / Partition
   ↓
NTFS
   ↓
Evidence Files
   ↓
Delete Evidence
   ↓
Forensic Examination
   ↓
MFT
   ↓
Metadata
   ↓
File Content
   ↓
Deleted Evidence
```

Kita akan menggunakan:
```text
mmls
fsstat
fls
istat
icat
```

dan setiap command akan kita jalankan satu per satu.

---
## Bagian 1: Pastikan hasil Praktik 5 masih ada

Pertama kita masuk ke directory tempat `disk.raw` dari praktik sebelumnya berada.
```bash
cd ~/forensic-lab/partition-lab
```

Kemudian lihat isinya:
```bash
ls -lh
```

Kamu seharusnya melihat:
```text
disk.raw
```

Sekarang periksa tipe file:
```bash
file disk.raw
```

Karena sebelumnya kita sudah membuat GPT dan partition, output tidak lagi sekadar mengatakan bahwa file tersebut adalah data kosong.

Sekarang kita pastikan partition table-nya masih ada:
```bash
fdisk -l disk.raw
```

Perhatikan bagian seperti:
```text
Disklabel type: gpt
```

dan informasi partition.

Setelah itu gunakan tool forensic yang sudah kita pelajari:
```bash
mmls disk.raw
```

Output-nya akan menunjukkan struktur sector.

Cari partition yang sebelumnya kita buat. Misalnya:
```text
Slot    Start        End        Length
-----   ----------   ---------- ----------
000:    0000000000   ...
001:    0000002048   ...
```

Catat nilai **Start** dari partition tersebut.

Misalnya:
```text
Start = 2048
```

Jangan langsung memakai angka `2048` kalau output milikmu berbeda. **Gunakan nilai Start dari `mmls` milikmu sendiri.**

Ini penting karena seluruh analisis berikutnya akan menggunakan partition offset tersebut.

---
# Bagian 2: Memastikan filesystem NTFS

Pada Praktik 5 kita baru membuat partition.

Partition tersebut belum otomatis menjadi filesystem.

Sekarang kita akan membuat NTFS di dalam partition tersebut.

Sebelum melakukan ini, pastikan `disk.raw` memang merupakan **image latihan**, bukan disk asli.

Jalankan:
```bash
sudo losetup -Pf --show disk.raw
```

Perintah ini meminta Linux membuat loop device berdasarkan partition yang terdapat dalam `disk.raw`.

Output bisa berupa:
```text
/dev/loop0
```

Kemudian lihat loop device yang dibuat:
```bash
lsblk
```

Kamu mungkin melihat sesuatu seperti:
```text
loop0
├─loop0p1
```

Kalau partition yang dibuat sebelumnya adalah partition pertama, maka device-nya kemungkinan:
```text
/dev/loop0p1
```

Tetapi **jangan menebak**. Gunakan hasil `lsblk` milikmu.

Sekarang kita akan membuat filesystem NTFS pada partition tersebut:
```bash
sudo mkfs.ntfs -F /dev/loop0p1
```

Jika loop device atau nomor partition milikmu berbeda, sesuaikan.

Parameter:
```text
-F
```

digunakan untuk memaksa pembuatan filesystem pada device yang dianggap kecil atau tidak biasa untuk filesystem NTFS.

Setelah selesai, kita sudah memiliki:
```text
disk.raw
   ↓
GPT
   ↓
Partition
   ↓
NTFS
```

Sekarang image kita mulai menjadi media forensic yang benar-benar berisi filesystem.

---
# Bagian 3: Mount filesystem latihan

Sekarang kita perlu memasukkan beberapa file evidence ke dalam filesystem.

Buat mount point:
```bash
mkdir -p ~/forensic-lab/mnt
```

Kemudian mount partition:
```bash
sudo mount /dev/loop0p1 ~/forensic-lab/mnt
```

Periksa:
```bash
ls -la ~/forensic-lab/mnt
```

Kamu akan melihat filesystem NTFS yang masih kosong.

Sekarang buat struktur directory yang menyerupai aktivitas user:
```bash
sudo mkdir -p ~/forensic-lab/mnt/Users/Alice/Documents
sudo mkdir -p ~/forensic-lab/mnt/Users/Alice/Downloads
```

Sekarang kita akan memasukkan evidence.

Buat file pertama:
```bash
echo "CASE-06: Normal document" | sudo tee ~/forensic-lab/mnt/Users/Alice/Documents/report.txt
```

Kemudian file kedua:
```bash
echo "CASE-06: Confidential information" | sudo tee ~/forensic-lab/mnt/Users/Alice/Documents/secret.txt
```

Kemudian file ketiga:
```bash
echo "CASE-06: Suspicious executable placeholder" | sudo tee ~/forensic-lab/mnt/Users/Alice/Downloads/suspicious.exe
```

Sekarang periksa struktur directory:
```bash
find ~/forensic-lab/mnt -type f -print
```

Seharusnya terdapat tiga file:
```text
Users/Alice/Documents/report.txt
Users/Alice/Documents/secret.txt
Users/Alice/Downloads/suspicious.exe
```

Sekarang kita memiliki evidence sederhana:
```text
Alice
├── Documents
│   ├── report.txt
│   └── secret.txt
└── Downloads
    └── suspicious.exe
```

---

# Bagian 4: Buat satu file lalu hapus

Sekarang bagian penting dari praktik.

Kita akan membuat satu file khusus yang nantinya kita hapus.
```bash
echo "CASE-06: Deleted evidence" | sudo tee ~/forensic-lab/mnt/Users/Alice/Documents/deleted-evidence.txt
```

Pastikan file tersebut benar-benar ada:
```bash
ls -la ~/forensic-lab/mnt/Users/Alice/Documents
```

Kamu harus melihat:
```text
deleted-evidence.txt
report.txt
secret.txt
```

Sekarang kita hapus:
```bash
sudo rm ~/forensic-lab/mnt/Users/Alice/Documents/deleted-evidence.txt
```

Periksa lagi:

```bash
ls -la ~/forensic-lab/mnt/Users/Alice/Documents
```

Sekarang:
```text
deleted-evidence.txt
```

tidak terlihat lagi.

Bagi user biasa, file tersebut sudah hilang.

Tetapi kita sekarang tidak akan bertanya kepada operating system:
> "File ini masih ada nggak?"

Kita akan bertanya kepada **filesystem forensic metadata**.

Inilah perbedaan mindset forensic.

---
# Bagian 5: Unmount evidence

Sebelum melakukan forensic examination, kita hentikan akses filesystem melalui operating system.

```bash
sudo umount ~/forensic-lab/mnt
```

Kemudian pastikan sudah tidak mounted:
```bash
mount | grep forensic-lab
```

Kalau tidak menghasilkan output, berarti mount sudah dilepas.

Sekarang kita kembali ke kondisi:
```text
disk.raw
   ↓
GPT
   ↓
Partition
   ↓
NTFS
   ↓
Evidence
```

dan kita akan menganalisisnya sebagai **forensic image**.

Ini penting karena kita tidak ingin examination berikutnya bercampur dengan aktivitas normal filesystem.

---
# Bagian 6: Periksa partition menggunakan `mmls`

Sekarang jalankan kembali:
```bash
mmls disk.raw
```

Cari:
```text
Start
```

Misalnya hasilnya:
```text
Start = 2048
```

Simpan nilai tersebut.

Kita sebut:
```text
PARTITION_OFFSET=2048
```

Kalau milikmu bukan `2048`, gunakan nilai milikmu.

Sekarang kita sudah mengetahui:
```text
disk.raw
    ↓
Partition Start = 2048
```

---
# Bagian 7: Periksa filesystem menggunakan `fsstat`

Sekarang kita masuk satu level lebih dalam.

Jalankan:

```bash
fsstat -o 2048 disk.raw
```

Sesuaikan `2048` dengan offset milikmu.

Karena filesystem yang kita buat adalah NTFS, output akan berisi informasi mengenai filesystem tersebut.

Cari informasi seperti:
```text
File System Type
Cluster Size
MFT
```

Output dapat berbeda tergantung versi The Sleuth Kit.

Yang ingin kita buktikan sekarang adalah:
> Partition yang kita temukan memang berisi filesystem NTFS.

Jadi workflow kita sekarang:

```text
mmls
 ↓
Partition ditemukan
 ↓
fsstat
 ↓
NTFS ditemukan
```

---
# Bagian 8: Melihat file menggunakan `fls`

Sekarang kita ingin melihat isi filesystem tanpa melakukan mount.

Gunakan:
```bash
fls -o 2048 disk.raw
```

Sesuaikan offset.

Kita mungkin mendapatkan directory atau entry pada root filesystem.

Karena file kita berada cukup dalam:
```text
Users
└── Alice
    ├── Documents
    └── Downloads
```

kita akan menggunakan recursive listing:
```bash
fls -r -o 2048 disk.raw
```

Sekarang perhatikan output.

Kamu seharusnya dapat menemukan sesuatu yang menyerupai:
```text
Documents
report.txt
secret.txt
Downloads
suspicious.exe
```

Yang menarik adalah apakah:
```text
deleted-evidence.txt
```

juga muncul.

Karena file tersebut sudah dihapus, kita perlu meminta `fls` untuk menampilkan deleted entries.

Gunakan:
```bash
fls -r -d -o 2048 disk.raw
```

Sekarang perhatikan apakah:
```text
deleted-evidence.txt
```

muncul.

Kalau muncul, kita baru saja mendapatkan salah satu finding pertama dari investigation:
```text
Operating System:
deleted-evidence.txt tidak terlihat

Filesystem Examination:
deleted-evidence.txt masih memiliki evidence pada filesystem metadata
```

Itulah mengapa filesystem examination penting.

---
# Bagian 9: Mendapatkan metadata address

Ketika menjalankan:
```bash
fls -r -d -o 2048 disk.raw
```

kamu akan melihat entry yang memiliki identifier.

Misalnya secara ilustrasi:
```text
r/r * 42: deleted-evidence.txt
```

Angka:
```text
42
```

adalah informasi penting yang akan kita gunakan untuk pemeriksaan selanjutnya.

**Jangan gunakan angka `42` secara otomatis.**

Gunakan angka yang benar-benar muncul di output `fls` milikmu.

Misalnya output milikmu:
```text
r/r * 37: deleted-evidence.txt
```

berarti:
```text
MFT Entry = 37
```

Catat angka tersebut.

---
# Bagian 10: Analisis MFT dengan `istat`

Sekarang kita akan memeriksa entry tersebut.

Misalnya MFT entry milikmu:
```text
37
```

jalankan:
```bash
istat -o 2048 disk.raw 37
```

Sesuaikan:
```text
2048 → partition offset milikmu
37   → metadata address milikmu
```

Sekarang perhatikan output.

Kita ingin mencari informasi seperti:
```text
File Name
Allocated / Unallocated
Size
Timestamps
Attributes
Data
```

Karena file tersebut sudah dihapus, status allocation menjadi sangat menarik.

Kita sekarang tidak hanya tahu:
```text
deleted-evidence.txt pernah ada
```

tetapi mulai dapat melihat:
```text
bagaimana filesystem merepresentasikan entry tersebut.
```

Inilah yang disebut **MFT examination**.

---
# Bagian 11: Melihat timestamps

Di output `istat`, perhatikan timestamp.

Kita ingin menemukan informasi seperti:
```text
Created
Modified
Accessed
Changed
```

Catat timestamp tersebut.

Misalnya:
```text
Created : 2026-08-16 12:20:10
Modified: 2026-08-16 12:20:10
Accessed : ...
Changed : ...
```

Jangan langsung menyimpulkan bahwa timestamp tersebut membuktikan seseorang melakukan tindakan tertentu.

Untuk saat ini kita hanya mencatatnya sebagai:
```text
Filesystem Artifact
```

Nanti ketika kita masuk **Timeline Analysis**, timestamp ini akan dikorelasikan dengan artifact lain.

---
# Bagian 12: Mencoba mengambil content dengan `icat`

Sekarang bagian yang paling menarik.

Kita sudah memiliki:
```text
disk.raw
partition offset
MFT entry
```

Kita akan mencoba mengambil content menggunakan:
```bash
icat -o 2048 disk.raw 37
```

Sesuaikan `2048` dan `37` dengan nilai milikmu.

Kalau berhasil, kita mungkin mendapatkan:
```text
CASE-06: Deleted evidence
```

Artinya:
```text
User deleted file
        ↓
File tidak terlihat melalui filesystem normal
        ↓
MFT entry masih dapat ditemukan
        ↓
Data masih tersedia
        ↓
icat berhasil membaca content
```

Ini merupakan contoh sederhana **deleted file recovery berbasis filesystem metadata**.

Kalau `icat` tidak menghasilkan content, jangan langsung menganggap praktik gagal. Ada banyak faktor filesystem yang memengaruhi recovery. Justru hasil tersebut merupakan sesuatu yang harus kita analisis.

---
# Bagian 13: Simpan hasil recovery

Kalau `icat` berhasil menampilkan content, kita bisa menyimpannya sebagai working copy:
```bash
icat -o 2048 disk.raw 37 > recovered-deleted-evidence.txt
```

Kemudian:
```bash
cat recovered-deleted-evidence.txt
```

Kita dapat memeriksa:
```text
CASE-06: Deleted evidence
```

Sekarang kita memiliki:
```text
Original:
deleted-evidence.txt
```

yang sudah tidak terlihat melalui filesystem normal.

Dan:
```text
Recovered:
recovered-deleted-evidence.txt
```

yang dibuat berdasarkan forensic examination.

Perhatikan bahwa `recovered-deleted-evidence.txt` **bukan evidence original**. Ini adalah hasil recovery atau working artifact dari proses examination.

---
# Bagian 14: Dokumentasikan Finding

Sekarang kita melakukan hal yang sering dilupakan ketika orang belajar tools forensic: **mencatat hasilnya.**

Buat file:
```bash
nano ~/forensic-lab/praktik-6-findings.txt
```

Isi misalnya:
```text
CASE: PRAKTIK-06

Evidence:
disk.raw

Filesystem:
NTFS

Partition Offset:
[isi dari mmls]

Files Found:
report.txt
secret.txt
suspicious.exe

Deleted File:
deleted-evidence.txt

MFT Entry:
[isi hasil fls]

Filesystem Status:
Deleted entry identified

Recovery:
[Berhasil / Tidak berhasil]

Recovered Content:
CASE-06: Deleted evidence

Tools:
mmls
fsstat
fls
istat
icat
```

Simpan file tersebut.

Sekarang kamu sudah melakukan workflow forensic kecil dari awal sampai akhir.

---
# Apa yang sebenarnya baru saja kita lakukan?

Kalau disederhanakan:
```text
Praktik 5
Disk Image
    ↓
GPT
    ↓
Partition
    ↓
NTFS
    ↓
────────────────────
Praktik 6
    ↓
Filesystem Examination
    ↓
mmls
    ↓
Partition Offset
    ↓
fsstat
    ↓
NTFS
    ↓
fls
    ↓
File Enumeration
    ↓
Deleted Entry
    ↓
istat
    ↓
MFT Metadata
    ↓
icat
    ↓
File Recovery
```

Dan yang paling penting, sekarang kamu sudah melihat hubungan langsung antara teori yang sebelumnya kita pelajari:
```text
NTFS
  ↓
MFT
  ↓
MFT Entry
  ↓
Attributes
  ↓
Metadata
  ↓
File Data
```

dengan command-line forensic examination.

## Status Praktik 6

**Praktik 6: NTFS & MFT Examination**

-  Menyiapkan `disk.raw` dari Praktik 5
    
-  Membuat NTFS pada partition
    
-  Mount filesystem
    
-  Membuat evidence files
    
-  Menghapus evidence
    
-  Unmount filesystem
    
-  Memeriksa partition dengan `mmls`
    
-  Memeriksa NTFS dengan `fsstat`
    
-  Enumerasi file dengan `fls`
    
-  Menemukan deleted entry
    
-  Menganalisis MFT dengan `istat`
    
-  Memeriksa timestamps
    
-  Mencoba recovery dengan `icat`
    
-  Menyimpan recovered content
    
-  Membuat catatan finding
    

**Penting:** kita jangan menganggap Praktik 6 selesai hanya karena command-nya sudah ditulis. Jalankan dari **Bagian 1**, lalu kirim output command yang kamu dapat. Dari situ kita lanjut ke bagian berikutnya dengan **output mesinmu sendiri**, termasuk menyesuaikan partition offset, loop device, MFT entry, dan hasil `fls`. Itu baru praktik forensic yang nyata, bukan sekadar daftar mantra Linux yang kebetulan memakai nama tool keren.
