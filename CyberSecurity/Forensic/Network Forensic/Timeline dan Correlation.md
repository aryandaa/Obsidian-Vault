#cybersecurity 

Sampai di sini kamu sudah bisa membaca PCAP, menganalisis DNS, HTTP, dan pola C2, serta menggali artifacts di host. Sekarang saatnya menggabungkan semuanya. **Timeline analysis** adalah kemampuan menyusun kejadian-kejadian dari berbagai sumber evidence menjadi urutan waktu yang bisa diceritakan, dan **correlation** adalah kemampuan menghubungkan kejadian-kejadian itu menjadi satu cerita utuh.

Ini keterampilan yang paling sering diuji dalam lomba forensic: bukan "cari satu flag", tetapi "ceritakan apa yang terjadi, dalam urutan apa, dan buktikan dengan evidence apa".

## Kenapa timeline penting

Sebuah PCAP memberi tahu paket demi paket. Tetapi manusia tidak berpikir dalam paket. Kita berpikir dalam peristiwa:

```text
15:00  penyerang melakukan port scan
15:30  penyerang login ke panel admin
15:31  webshell di-upload
15:32  webshell dieksekusi
16:00  malware mulai beacon ke C2
17:00  data dikirim keluar (exfiltration)
```

Timeline mengubah kumpulan paket menjadi cerita. Dan cerita itulah yang menjawab pertanyaan investigasi: apa yang terjadi, kapan, dan dalam urutan apa.

## Sumber waktu

Waktu datang dari banyak tempat, dan semuanya punya karakteristik sendiri:

```text
frame.time (PCAP)          → waktu paket tertangkap
syslog / access log        → waktu dicatat server
file timestamps            → waktu file dibuat/dimodifikasi
event log (Windows)        → waktu event terjadi
browser history            → waktu halaman dikunjungi
```

Masalahnya: sumber-sumber ini bisa berbeda timezone, berbeda jam sistem, bahkan berbeda format. Sebelum menggabungkan, **samakan dulu semua waktu ke satu timezone**.

## Timezone: musuh yang tidak terlihat

PCAP menyimpan timestamp dalam UTC biasanya (tergantung cara capture). Log server sering memakai zona lokal. Browser history memakai zona mesin.

Langkah yang benar:

1. Catat timezone setiap evidence.
2. Ubah semuanya ke satu zona (biasanya UTC untuk standardisasi).
3. Baru urutkan.

Contoh: `12/Aug/2026:15:30:02 +0000` di Apache sudah UTC. `2026-08-12 22:30:02+07:00` di file timestamp adalah UTC+7, artinya 15:30:02 UTC. Keduanya adalah waktu yang sama.

Kalau kamu mengurutkan tanpa menyamakan zona, seluruh timeline bisa salah.

## Membangun timeline

Cara paling sederhana dan efektif: kumpulkan semua kejadian dalam satu daftar, lalu sortir.

```bash
tshark -r file.pcap -T fields -e frame.time -e ip.src -e ip.dst -e _ws.col.Info > events.txt
```

Ekstrak kejadian dari log:

```bash
grep -E "login|upload|beacon" syslog.txt >> events.txt
```

Gabungkan, sortir berdasarkan waktu, dan baca sebagai cerita.

Untuk project kecil, spreadsheet atau bahkan sort manual sudah cukup. Kuncinya bukan tool-nya, tetapi disiplin mencatat: setiap baris harus punya waktu, sumber, dan deskripsi.

## Correlation: menghubungkan antar evidence

Korelasi berarti menemukan **benang merah** antara evidence yang berbeda. Pola-pola korelasi yang umum:

### IP yang sama di banyak tempat

IP penyerang muncul di PCAP (SYN scan), di access log (request HTTP), di syslog (login gagal SSH), dan di firewall log. Satu IP menghubungkan semua artefak.

```text
10.10.14.2 di PCAP    → SYN scan port 80
10.10.14.2 di access.log → POST /admin/login.php
10.10.14.2 di syslog   → Invalid user admin
```

Kesimpulan: 10.10.14.2 adalah sumber serangan.

### Proses dan koneksi

Di host artifacts, PID yang sama muncul di netstat (koneksi keluar) dan di process list (nama proses). Korelasi menghubungkan komunikasi dengan program tertentu.

### Domain dan file

Domain C2 di DNS cache, lalu file yang diunduh dari domain yang sama di browser history, lalu proses dengan nama mirip di process list. Satu cerita dari tiga sumber.

### Waktu yang berdekatan

Kejadian yang waktunya berdekatan sering berkaitan:

```text
15:30:02  login admin berhasil (log)
15:31:05  file di-upload (log)
15:31:10  webshell dieksekusi (access log)
```

Urutan ini membentuk fase: akses, instalasi, eksekusi.

```
Ingat prinsip dari materi pertama: korelasi bukan kausalitas.
Dua kejadian berdekatan waktunya belum tentu saling menyebabkan.
Tetapi semakin banyak evidence yang konsisten, semakin kuat hipotesisnya.
```

## Pola 5W1H dalam network forensic

Saat menyusun timeline dan korelasi, biasakan bertanya:

```text
What?   apa yang terjadi (scan, exploit, beacon, exfil)
Where?  di jaringan mana, IP dan port apa
When?   kapan, urutan waktunya
Who?    IP penyerang, user, proses
How?    lewat metode apa (SQLi, webshell, DNS tunnel)
Why?    apa tujuannya (paling hati-hati, butuh banyak evidence)
```

## Dari timeline ke laporan

Struktur laporan sederhana yang bisa kamu pakai:

```text
1. Ringkasan eksekutif (2-3 kalimat)
2. Kronologi (timeline berurutan)
3. Evidence yang mendukung (per fase)
4. IOC (IP, domain, hash, interval)
5. Kesimpulan dan batasan
```

Dalam lomba, kamu tidak perlu menulis dokumen panjang. Tetapi melatih menyusun kronologi membuatmu menjawab soal bertingkat dengan cepat: IP, port, domain, waktu, urutan.

## Alur kerja

```text
Kumpulkan semua evidence (pcap + log + artifacts)
    ↓
Normalisasi waktu (samakan timezone)
    ↓
Ekstrak kejadian dari tiap sumber
    ↓
Gabungkan dan sortir
    ↓
Cari korelasi (IP, PID, domain, waktu)
    ↓
Susun cerita per fase
    ↓
Tulis laporan
```

Sekarang kita praktikkan timeline dan korelasi menggunakan PCAP dari beberapa fase serangan plus log host: [Praktek 8](Praktek%20dan%20Latihan/Praktek%208.md)

Setelah itu, semua keterampilan ini akan diuji dalam [Capstone Study Kasus](Capstone%20Study%20Kasus.md).
