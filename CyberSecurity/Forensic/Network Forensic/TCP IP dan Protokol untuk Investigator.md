#cybersecurity 

Sebelum membaca PCAP dengan lancar, kamu harus memahami bahasa yang dipakai jaringan: **TCP/IP dan protokol**. Paket yang kamu lihat di Wireshark bukan sekadar byte acak, ia adalah hasil dari lapisan-lapisan protokol yang saling membungkus. Investigator yang paham struktur ini bisa langsung membaca arti setiap byte tanpa menebak.

Konsep kunci yang akan kamu bawa: **setiap paket adalah kotak di dalam kotak di dalam kotak.**

```text
Frame Ethernet
 └── Paket IP
      └── Segmen TCP / Datagram UDP
           └── Data aplikasi (HTTP, DNS, FTP, ...)
```

## Model TCP/IP

Jaringan modern bekerja dengan model berlapis. Untuk kepentingan investigator, empat lapis ini yang paling penting:

```text
Application   → HTTP, DNS, FTP, SSH, SMTP (data yang dikirim aplikasi)
Transport     → TCP, UDP (cara data dikirim: andal atau cepat)
Internet      → IP (alamat tujuan: dari mana ke mana)
Link          → Ethernet, Wi-Fi (pengiriman fisik antar perangkat)
```

Ketika Wireshark menampilkan sebuah paket, ia menampilkan semua lapisan ini sekaligus. Kemampuan membaca paket = kemampuan membaca lapisan-lapisannya.

## Lapisan Link: Ethernet dan MAC

Di lapisan paling bawah, perangkat berkomunikasi menggunakan **MAC address** (48 bit, ditulis seperti `00:1a:2b:3c:4d:5e`).

Sebuah frame Ethernet berisi:

```text
Destination MAC (6 byte)
Source MAC (6 byte)
Type (2 byte, misal 0x0800 untuk IPv4)
Payload (data IP)
```

Wireshark menampilkan MAC dalam bentuk readable. Dalam investigasi, MAC membantu menghubungkan paket dengan perangkat fisik, terutama di jaringan lokal. Tapi ingat: MAC bisa di-spoof, jadi jangan jadikan satu-satunya bukti identitas.

## Lapisan Internet: IP

Paket IP berisi informasi penting:

```text
Version (IPv4 atau IPv6)
Source IP
Destination IP
Protocol (6 = TCP, 17 = UDP, 1 = ICMP)
TTL (time to live)
Total Length
```

Contoh paket IPv4 di Wireshark:

```text
Internet Protocol Version 4, Src: 192.168.1.50, Dst: 192.168.1.10
    Protocol: TCP (6)
```

**TTL** menarik untuk forensic. TTL awal biasanya 64 (Linux), 128 (Windows), atau 255 (router). Kalau sebuah paket sampai dengan TTL rendah, itu bisa menandakan jarak hop yang jauh. TTL yang tidak wajar kadang menjadi petunjuk sumber paket.

## Lapisan Transport: TCP

TCP adalah protokol yang paling sering dianalisis. Ia menyediakan pengiriman yang andal dengan mekanisme:

- **Port** untuk membedakan aplikasi (sumber dan tujuan).
- **Sequence number** untuk mengurutkan data.
- **Acknowledgement (ACK)** untuk konfirmasi penerimaan.
- **Flags** untuk mengontrol koneksi.

### Flags TCP yang wajib kamu hafal

```text
SYN  (0x02)  → memulai koneksi
ACK  (0x10)  → mengonfirmasi penerimaan
FIN  (0x01)  → menutup koneksi secara normal
RST  (0x04)  → memutus koneksi secara paksa
PSH  (0x08)  → dorong data segera
URG  (0x20)  → data mendesak
```

Kombinasi flag sering ditulis seperti `SYN, ACK`. Di tshark, flags direpresentasikan dalam bentuk yang bisa kamu filter (misalnya `tcp.flags.syn == 1`).

### Three-way handshake

Setiap koneksi TCP dimulai dengan tiga paket:

```text
Client → Server : SYN
Server → Client : SYN, ACK
Client → Server : ACK
```

Ini adalah sidik jari awal sebuah koneksi. Ketika kamu melihat handshake lengkap diikuti pertukaran data, berarti koneksi itu nyata dan berhasil. Ketika kamu hanya melihat SYN dan tidak ada kelanjutannya, itu bisa jadi percobaan koneksi, port scan, atau koneksi yang gagal.

### Sequence number

Setiap byte data diberi nomor urut. Kalau payload sebuah segmen sepanjang 100 byte dimulai dengan seq 1000, segmen berikutnya akan memakai seq 1100. Dengan memahami ini, kamu bisa mendeteksi data yang terfragmentasi dan me-reassemble isi komunikasi.

## Lapisan Transport: UDP

UDP adalah saudara TCP yang lebih sederhana: **tanpa handshake, tanpa jaminan sampai**. Ia hanya membawa port sumber, port tujuan, panjang, dan data.

```text
Source Port (2 byte)
Destination Port (2 byte)
Length (2 byte)
Checksum (2 byte)
Data
```

UDP dipakai oleh protokol yang mengutamakan kecepatan atau yang hanya butuh sekali kirim: DNS (53), DHCP (67/68), NTP (123), streaming, dan game online.

Dalam forensic, UDP penting karena banyak teknik penyalahgunaan memanfaatkannya, misalnya DNS tunneling dan amplification attack.

## Protokol aplikasi dan port penting

Setiap protokol aplikasi punya port default. Hafalkan yang paling sering muncul di lomba dan investigasi:

```text
20/21   FTP            transfer file (plaintext!)
22      SSH            remote shell terenkripsi
23      Telnet         remote shell plaintext (jarang, tapi berbahaya)
25      SMTP           kirim email
53      DNS            resolve nama domain (UDP biasanya)
67/68   DHCP           alamat IP otomatis
80      HTTP           web plaintext
110     POP3           ambil email
123     NTP            sinkronisasi waktu
137-139 NetBIOS        berbagi file Windows lama
143     IMAP           ambil email (lebih modern)
443     HTTPS          web terenkripsi
445     SMB            berbagi file Windows modern
1433    MSSQL          database SQL Server
3306    MySQL          database MySQL
3389    RDP            remote desktop Windows
8080    HTTP-alt       web alternatif (sering dipakai C2!)
```

Penting untuk dipahami: port hanyalah angka. Seorang penyerang bisa menjalankan layanan apa pun di port mana pun. C2 di port 8080, DNS tunneling di port 53, bahkan web server di port 4444. Karena itu jangan pernah menyimpulkan "port 80 berarti HTTP" tanpa melihat isi paketnya.

## Membaca sebuah koneksi mencurigakan

Latihan mentalnya begini. Kamu melihat rangkaian paket:

```text
192.168.1.50 → 203.0.113.77 : SYN
203.0.113.77 → 192.168.1.50 : SYN, ACK
192.168.1.50 → 203.0.113.77 : ACK
192.168.1.50 → 203.0.113.77 : PSH, ACK (GET /update HTTP/1.1)
203.0.113.77 → 192.168.1.50 : ACK
203.0.113.77 → 192.168.1.50 : PSH, ACK (HTTP/1.1 200 OK)
```

Yang bisa kamu baca dari rangkaian ini:

- Ada koneksi TCP yang berhasil (handshake lengkap).
- Port tujuan 8080 (perhatikan: bukan 80).
- Mesin 192.168.1.50 mengirim request HTTP ke server C2.
- Server merespons dengan 200 OK.

Ini pola khas beacon malware: mesin korban secara berkala menghubungi server C2 untuk mengambil perintah.

## TCP sebagai fingerprint aktivitas

Pola flags bisa menjadi petunjuk aktivitas:

```text
SYN saja berulang ke banyak port   → port scan
SYN, SYN, ACK, RST                 → scan yang berhasil menemukan port terbuka
SYN tanpa balasan                   → port tertutup atau difilter firewall
RST tiba-tiba setelah handshake     → koneksi ditolak atau diputus paksa
Banyak koneksi paralel              → brute force, download massal, atau DDoS
```

Kemampuan membaca pola ini yang membedakan "membaca paket" dan "menganalisis lalu lintas".

## Hubungan dengan tool

Semua konsep ini akan muncul di tshark dan Wireshark sebagai kolom dan filter:

```bash
tshark -r file.pcap -Y "tcp.flags.syn == 1"
```

```bash
tshark -r file.pcap -Y "tcp.port == 8080"
```

```bash
tshark -r file.pcap -Y "ip.src == 192.168.1.50"
```

Kamu tidak perlu menghafal struktur byte per byte. Tetapi kamu harus bisa membaca apa yang ditampilkan tool dan menerjemahkannya menjadi cerita.

Sekarang kita praktikkan membaca protokol pada PCAP yang sudah disediakan: [Praktek 2](Praktek%20dan%20Latihan/Praktek%202.md)
