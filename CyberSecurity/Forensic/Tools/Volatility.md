#tool 

Setelah storage, kita masuk ke salah satu sumber evidence paling menarik: **memory (RAM)**. Volatility adalah framework memory forensics yang paling populer. Ia menganalisis memory dump dan mengekstrak informasi seperti proses yang berjalan, command line, koneksi jaringan, module, registry, dan file yang ada di memory.

Kenapa memory penting? Karena banyak hal tidak pernah menyentuh disk. Malware bisa hidup hanya di memory, command bisa dijalankan tanpa menulis file, dan data sensitif bisa berada di RAM tanpa pernah disimpan.

```
Memory adalah tempat kejadian perkara yang paling hidup.
Volatility adalah alat untuk membacanya.
```

Ada dua versi utama yang perlu kamu pahami: **Volatility 2** (Python 2, menggunakan profile) dan **Volatility 3** (Python 3, menggunakan symbol table). Syntax keduanya berbeda.

---
## 1. Instalasi

### Volatility 2

```bash
sudo apt update
sudo apt install volatility
```

atau dari git:

```bash
git clone https://github.com/volatilityfoundation/volatility.git
cd volatility
python2 vol.py --help
```

### Volatility 3

```bash
git clone https://github.com/volatilityfoundation/volatility3.git
cd volatility3
python3 vol.py -h
```

atau via pip:

```bash
pip install volatility3
```

Verifikasi:

```bash
python3 vol.py -h
```

Volatility 3 membutuhkan symbol table untuk analisis. Beberapa versi perlu mengunduh symbol secara otomatis atau manual.

---
# 2. Menentukan Profil (Volatility 2)

Volatility 2 membutuhkan **profile**: identifikasi sistem operasi dan arsitektur dari memory dump.

```bash
volatility -f memory.raw imageinfo
```

Output:

```text
Volatility Foundation Volatility Framework 2.6.1
INFO    : Volatility Systems ...
          Suggested Profile(s) : Win7SP1x64, Win7SP0x64, ...
```

Ambil profile yang disarankan, lalu gunakan di command berikutnya:

```bash
volatility -f memory.raw --profile=Win7SP1x64 pslist
```

```
Di Volatility 2, hampir semua command membutuhkan --profile.
imageinfo adalah langkah pertama yang wajib.
```

---
# 3. Command Utama Volatility 2

```bash
volatility -f memory.raw --profile=Win7SP1x64 pslist
```

daftar proses yang berjalan saat dump diambil.

```bash
pstree
```

proses dalam bentuk tree (melihat parent dan child).

```bash
psscan
```

memindai proses langsung dari memory (bisa menemukan proses yang tersembunyi).

```bash
netscan
```

koneksi jaringan aktif dan socket.

```bash
cmdline
```

command line setiap proses.

```bash
dlllist
```

DLL yang di-load oleh proses.

```bash
malfind
```

mencari kode yang disuntikkan (injected code), ciri khas malware.

```bash
hashdump
```

mengekstrak hash password dari SAM.

```bash
memdump -p <PID> --dump-dir=out/
```

mendump memory proses tertentu ke file.

```bash
procdump -p <PID> --dump-dir=out/
```

mendump executable proses.

```bash
iehistory
```

riwayat Internet Explorer.

Contoh lengkap:

```bash
volatility -f memory.raw --profile=Win7SP1x64 pstree
```

```bash
volatility -f memory.raw --profile=Win7SP1x64 netscan
```

```bash
volatility -f memory.raw --profile=Win7SP1x64 cmdline
```

---
# 4. Command Utama Volatility 3

Volatility 3 menggunakan struktur `plugin.modul`:

```bash
python3 vol.py -f memory.raw windows.pslist
```

Command yang paling sering dipakai:

```bash
python3 vol.py -f memory.raw windows.pstree
```

```bash
python3 vol.py -f memory.raw windows.cmdline
```

```bash
python3 vol.py -f memory.raw windows.netscan
```

```bash
python3 vol.py -f memory.raw windows.malfind
```

```bash
python3 vol.py -f memory.raw windows.filescan
```

mencari file yang ada di memory, termasuk file yang sudah dihapus dari disk.

```bash
python3 vol.py -f memory.raw windows.dumpfiles -Q <offset>
```

mendump file dari memory berdasarkan offset hasil filescan.

```bash
python3 vol.py -f memory.raw windows.hashdump
```

```bash
python3 vol.py -f memory.raw windows.registry.printkey -K "Software\Microsoft\Windows\CurrentVersion\Run"
```

membaca registry dari memory.

```bash
python3 vol.py -f memory.raw windows.modscan
```

memindai module kernel.

Untuk melihat semua plugin:

```bash
python3 vol.py -f memory.raw windows.info
```

```
Volatility 3 tidak perlu imageinfo. Ia langsung membaca struktur memory
menggunakan symbol table. Lebih sederhana dan lebih cepat.
```

---
# 5. Workflow Dasar Memory Forensics

```text
1. Identifikasi dump
    ↓
2. Proses yang berjalan (pslist / pstree)
    ↓
3. Proses mencurigakan
    ↓
4. Command line proses (cmdline)
    ↓
5. Koneksi jaringan (netscan)
    ↓
6. Kode yang disuntik (malfind)
    ↓
7. Dump proses mencurigakan
    ↓
8. Analisis dump dengan strings / exiftool / binwalk
```

Pola pikirnya: temukan proses yang tidak biasa, lalu gali proses tersebut.

---
# 6. Hidden Gem: Analisis Dump Proses

Setelah mendump proses mencurigakan:

```bash
volatility -f memory.raw --profile=Win7SP1x64 memdump -p 1234 --dump-dir=out/
```

hasilnya adalah file mentah berisi memory proses. Sekarang analisis dengan tool lain:

```bash
strings out/1234.dmp | grep -iE "password|token|secret"
```

```bash
strings -e l out/1234.dmp | grep -i "http"
```

```bash
binwalk out/1234.dmp
```

Kombinasi Volatility + strings + binwalk sangat sering menghasilkan flag di CTF.

---
# 7. Hidden Gem: `filescan` dan `dumpfiles`

`filescan` di Volatility 3 menemukan objek file di memory, termasuk file yang sudah dihapus dari disk. Ini sangat berguna ketika malware menghapus dirinya sendiri setelah dieksekusi.

```bash
python3 vol.py -f memory.raw windows.filescan | grep -i "secret\|flag\|evidence"
```

```text
0x123456789abc  File: \Users\Alice\Desktop\flag.txt
```

Lalu dump:

```bash
python3 vol.py -f memory.raw windows.dumpfiles -Q 0x123456789abc
```

```
File yang dihapus dari disk bisa tetap ada di memory.
filescan + dumpfiles mengambilnya kembali.
```

---
# 8. Keterbatasan

- Volatility 2 butuh profile yang tepat; profil salah menghasilkan output salah.
- Volatility 3 butuh symbol table yang sesuai dengan versi Windows di dump.
- Memory dump hanya menggambarkan kondisi saat dump diambil, bukan seluruh sejarah.

---
# 9. Command yang Perlu Kamu Kuasai

### Volatility 2

```bash
volatility -f memory.raw imageinfo
```

```bash
volatility -f memory.raw --profile=<PROFILE> pslist
```

```bash
volatility -f memory.raw --profile=<PROFILE> pstree
```

```bash
volatility -f memory.raw --profile=<PROFILE> netscan
```

```bash
volatility -f memory.raw --profile=<PROFILE> cmdline
```

```bash
volatility -f memory.raw --profile=<PROFILE> malfind
```

### Volatility 3

```bash
python3 vol.py -f memory.raw windows.pslist
```

```bash
python3 vol.py -f memory.raw windows.cmdline
```

```bash
python3 vol.py -f memory.raw windows.netscan
```

```bash
python3 vol.py -f memory.raw windows.malfind
```

```bash
python3 vol.py -f memory.raw windows.filescan
```
