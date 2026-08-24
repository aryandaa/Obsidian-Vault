#tool 

Ini salah satu tool paling penting dalam Storage & File System Forensic: **The Sleuth Kit (TSK)**. Sleuth Kit adalah kumpulan tool command line untuk menganalisis disk image tanpa melakukan mount, sehingga **image tidak pernah diubah**. Sleuth Kit membaca langsung struktur filesystem: partition table, metadata, file, dan bahkan file yang sudah dihapus.

Kalau selama ini kita menganalisis dari "luar", Sleuth Kit membawa kita masuk ke dalam struktur filesystem itu sendiri.

```
Sleuth Kit tidak mount, tidak menulis, tidak mengubah apa pun.
Ia hanya membaca struktur filesystem dan menampilkannya.
```

---
## 1. Instalasi

```bash
sudo apt update
sudo apt install sleuthkit
```

Verifikasi:

```bash
tsk_version
```

Daftar tool utama yang akan kita pakai:

```text
mmls         → lihat partition table
fsstat       → lihat statistik filesystem
fls          → daftar file dan directory
istat        → detail metadata (inode/MFT entry)
icat         → ambil isi file berdasarkan metadata
ils          → daftar metadata (termasuk yang dihapus)
blkls        → daftar unallocated space
tsk_recover  → recovery file
```

---
# 2. Konsep Penting: Offset

Sebelum masuk ke command, pahami satu konsep yang akan terus dipakai: **offset byte**.

Sebuah disk image biasanya berisi partition table di awal, lalu beberapa partition. Filesystem tidak dimulai dari byte 0 image, melainkan dari offset tertentu.

Dengan Sleuth Kit, kamu bisa memberitahu offset melalui flag `-o`:

```bash
-o <offset>
```

offset dalam satuan **sector** (biasanya 512 byte).

Contoh:

```bash
tsk_recover -o 2048 ...
```

berarti filesystem dimulai dari sector 2048 (atau byte `2048 * 512 = 1048576`).

Untuk mengetahui offset, gunakan `mmls`.

---
# 3. `mmls`: Membaca Partition Table

`mmls` menampilkan layout partition dari sebuah disk image.

```bash
mmls evidence.img
```

Output:

```text
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000204799   0000202752   NTFS (0x07)
003:  -------   0000204800   0000209407   0000004608   Unallocated
```

Perhatikan kolom:

```text
Start   → sektor pertama partition
End     → sektor terakhir
Length  → panjang partition dalam sektor
Description → tipe filesystem
```

Dari output ini, partition NTFS dimulai dari sector `2048`. Offset untuk command selanjutnya adalah `2048`.

```
mmls adalah gerbang pertama. Selalu jalankan mmls sebelum menganalisis
filesystem, supaya kamu tahu di mana partition berada.
```

---
# 4. `fsstat`: Statistik Filesystem

Setelah tahu offset, kita bisa melihat statistik filesystem:

```bash
fsstat -o 2048 evidence.img
```

Output menampilkan banyak informasi:

```text
FILE SYSTEM INFORMATION
--------------------------------------------
File System Type: NTFS
Volume Serial Number: 1234567890ABCDEF
OEM Name: NTFS
Version: 3.1

METADATA INFORMATION
--------------------------------------------
First Cluster of MFT: 0
...

CONTENT INFORMATION
--------------------------------------------
Sector Size: 512
Cluster Size: 4096
Total Cluster Range: 0 - 202751
...
```

Informasi seperti sector size dan cluster size penting untuk memahami cara filesystem menyimpan data.

Untuk filesystem Linux:

```bash
fsstat -o 2048 evidence.img
```

```
fsstat menjawab pertanyaan "filesystem apa ini dan bagaimana strukturnya?"
Sebelum melihat file, kenali dulu filesystem-nya.
```

---
# 5. `fls`: Daftar File

Ini tool yang paling sering dipakai. `fls` menampilkan daftar file dan directory dalam filesystem.

```bash
fls -o 2048 evidence.img
```

Output:

```text
d/d 11:	$AttrDef
d/d 12:	$BadClus
d/d 13:	$Bitmap
d/d 14:	$Boot
...
r/r 45-128-1:	Users
r/r 50-128-4:	Windows
```

Format penulisan:

```text
d/d  → directory
r/r  → regular file
l/l  → symbolic link
-/-  → deleted
```

Angka setelahnya adalah metadata address (inode untuk ext, MFT entry untuk NTFS).

Untuk melihat isi directory tertentu:

```bash
fls -o 2048 evidence.img 45
```

untuk menampilkan path lengkap secara rekursif:

```bash
fls -o 2048 -r evidence.img
```

```
r/r 50-128-4:	Users
```

Angka `50` adalah MFT entry, `128` adalah atribut, `4` adalah nama. Untuk NTFS, kombinasi ini penting ketika kita menggunakan `icat`.

---
# 6. `fls -d`: File yang Dihapus

Ini hidden gem yang sangat penting. Flag:

```bash
-d
```

menampilkan hanya entry yang dihapus:

```bash
fls -o 2048 -d evidence.img
```

Output bisa menunjukkan file yang secara normal tidak terlihat:

```text
r/r 1024-128-1:	secret.txt (deleted)
r/r 2048-128-2:	password.docx (deleted)
```

```
File yang dihapus bukan berarti hilang. Selama entry metadata-nya masih
ada di MFT/inode table, fls -d bisa melihatnya.
```

---
# 7. `istat`: Detail Metadata

`istat` menampilkan detail satu metadata entry (inode atau MFT entry).

```bash
istat -o 2048 evidence.img 50
```

Output:

```text
MFT Entry Header Values:
Entry: 50        Sequence: 128
$LogFile Sequence Number: ...
...

Times:
Created:    2026-08-12 01:30:00.000000000
File Modified: 2026-08-12 01:31:00.000000000
MFT Modified: 2026-08-12 01:30:05.000000000
Accessed:   2026-08-12 01:32:00.000000000

Name: Users
Parent Directory: 5
```

Informasi timestamp sangat berharga untuk timeline analysis.

Untuk entry yang dihapus, `istat` bisa memberikan informasi yang tersisa:

```bash
istat -o 2048 evidence.img 1024
```

---
# 8. `icat`: Ambil Isi File

`icat` mengambil isi file berdasarkan metadata address. Ini cara mengekstrak file tanpa mount.

```bash
icat -o 2048 evidence.img 50 > extracted_users_file
```

Untuk file yang dihapus:

```bash
icat -o 2048 evidence.img 1024 > recovered_secret.txt
```

Output bisa dicek:

```bash
file recovered_secret.txt
```

```
icat + fls -d adalah kombinasi untuk memulihkan file yang dihapus.
```

---
# 9. `ils`: Daftar Metadata (Termasuk Deleted)

`ils` menampilkan daftar metadata entry. Tanpa flag tambahan, ia menampilkan semua entry yang dianggap aktif. Dengan:

```bash
ils -o 2048 evidence.img
```

untuk melihat entry yang dihapus:

```bash
ils -o 2048 evidence.img -d
```

Output:

```text
class|host|device|start_time
st_ino|st_alloc|st_uid|st_gid|st_mtime|st_atime|st_ctime|st_size
1024|0|0|0|1755000000|1755000100|1755000050|12345
```

```
|0| pada kolom kedua (st_alloc) menandakan entry tidak teralokasi,
artinya file sudah dihapus tetapi metadata-nya masih ada.
```

---
# 10. `tsk_recover`: Recovery Massal

`tsk_recover` memulihkan semua file ke directory tujuan.

```bash
mkdir recovered
```

```bash
tsk_recover -o 2048 evidence.img recovered/
```

Untuk memulihkan termasuk file yang dihapus:

```bash
tsk_recover -o 2048 -e evidence.img recovered/
```

Flag `-e` berarti "include deleted files".

Setelah recovery, cek hasilnya:

```bash
file recovered/*
```

---
# 11. `blkls`: Unallocated Space

`blkls` menampilkan blok data yang tidak teralokasi (unallocated space). Ini adalah daerah tempat data yang dihapus sering kali masih tersisa.

```bash
blkls -o 2048 evidence.img > unallocated.bin
```

Hasilnya bisa dianalisis lebih lanjut:

```bash
strings unallocated.bin | grep -i flag
```

atau di-carve menggunakan `foremost`:

```bash
foremost -i unallocated.bin -o carved/
```

```
Unallocated space adalah tempat favorit data yang "sudah dihapus".
blkls mengisolasinya, tool lain yang membedahnya.
```

---
# 12. Workflow Sleuth Kit

```text
mmls evidence.img
    ↓
Tentukan offset partition
    ↓
fsstat -o <offset> evidence.img
    ↓
fls -o <offset> evidence.img
    ↓
istat / icat / fls -d
    ↓
Ekstraksi file atau recovery
```

Semua command ini bekerja pada image tanpa mengubah apa pun. Inilah mengapa Sleuth Kit menjadi standar dalam filesystem forensic.

---
# 13. Command yang Perlu Kamu Kuasai

```bash
mmls evidence.img
```

```bash
fsstat -o 2048 evidence.img
```

```bash
fls -o 2048 evidence.img
```

```bash
fls -o 2048 -r evidence.img
```

```bash
fls -o 2048 -d evidence.img
```

```bash
istat -o 2048 evidence.img <entry>
```

```bash
icat -o 2048 evidence.img <entry> > file.out
```

```bash
tsk_recover -o 2048 -e evidence.img recovered/
```
