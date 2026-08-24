#tools

Kumpulan tool yang membantu selama belajar Digital Forensics, diorganisasi berdasarkan alur kerja forensic.
## Identifikasi & Triage

1. [File](File.md) - identifikasi tipe file berdasarkan magic bytes, bukan ekstensi
2. [Lsblk](Lsblk.md) - lihat struktur block device, disk vs partition, filesystem
3. [Strings](Strings.md) ⭐ - ekstrak teks dari file binary, tool pertama mencari flag
4. [Xxd dan Hexdump](Xxd%20dan%20Hexdump.md) - lihat dan analisis byte mentah file
5. [Exiftool](Exiftool.md) ⭐ - baca metadata semua jenis file: author, GPS, timestamp

## Integrity

6. [Sha256sum dan Hashdeep](Sha256sum%20dan%20Hashdeep.md) - verifikasi evidence tidak berubah

## Acquisition (Imaging)

7. [Dd dan Dcfldd](Dd%20dan%20Dcfldd.md) - buat salinan forensik bit-for-bit
8. [Mount dan Losetup](Mount%20dan%20Losetup.md) - akses image secara read-only

## Filesystem Analysis

9. [Sleuth Kit](Sleuth%20Kit.md) ⭐ - mmls, fsstat, fls, istat, icat: analisis filesystem tanpa mount

## Carving & Recovery

10. [Foremost dan Scalpel](Foremost%20dan%20Scalpel.md) - pulihkan file dari data mentah via signature
11. [Binwalk](Binwalk.md) ⭐ - temukan dan ekstrak file yang tertanam di dalam file
12. [Bulk Extractor](Bulk%20Extractor.md) ⭐ - pindai seluruh image: email, URL, IP, kunci, dan lainnya

## Memory Forensics

13. [Volatility](Volatility.md) - analisis memory dump: proses, network, command line

## Alur Pemakaian Singkat

```text
lsblk → identifikasi device evidence
dd / dcfldd → buat image
sha256sum → verifikasi integrity
file / strings / exiftool → triage awal
mmls → cari partition
fls / istat / icat → analisis filesystem
blkls → isolasi unallocated space
foremost / binwalk → carving
bulk_extractor → pindai artefak massal
volatility → analisis memory dump
```
