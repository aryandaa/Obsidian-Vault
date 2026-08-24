#latihan 

Praktik pertama network forensic. Tujuannya: **kenalan dengan PCAP dan tshark**. Kamu akan membaca file `praktek1_hello.pcap` yang berisi traffic sederhana: ARP, ping (ICMP), dan satu sesi HTTP.

File yang dipakai:

```text
Files/praktek1_hello.pcap
```

## Langkah 1: Lihat informasi file

```bash
cd "Network Forensic/Files"
```

```bash
capinfos praktek1_hello.pcap
```

Perhatikan jumlah paket dan durasi capture. Catat angka paketnya.

## Langkah 2: Baca daftar paket

```bash
tshark -r praktek1_hello.pcap
```

Kamu akan melihat kurang lebih urutan seperti ini:

```text
ARP      (siapa punya 192.168.1.1?)
ICMP     (echo request / reply, alias ping)
TCP      (handshake SYN, SYN ACK, ACK)
HTTP     (GET /)
HTTP     (200 OK)
```

Tulis jawaban untuk pertanyaan berikut:

1. Berapa banyak paket ARP?
2. Berapa banyak paket ICMP?
3. Siapa yang melakukan handshake TCP (IP sumber dan tujuan, port berapa)?

## Langkah 3: Lihat isi paket HTTP

Filter protokol HTTP:

```bash
tshark -r praktek1_hello.pcap -Y "http"
```

Kamu akan melihat dua paket: request `GET /` dan response `200 OK`.

## Langkah 4: Ekstrak payload TCP

Ikuti aliran data pada port 80 (ini versi sederhana dari follow stream):

```bash
tshark -r praktek1_hello.pcap -Y "tcp.port == 80" -T fields -e tcp.payload | xxd -r -p
```

Kamu akan melihat request HTTP dan response-nya sebagai teks. Di dalam response ada pesan dan sebuah flag.

## Langkah 5: Cari flag dengan strings

Cara alternatif yang lebih cepat: ekstrak semua string dari file PCAP.

```bash
strings praktek1_hello.pcap | grep -i flag
```

Atau:

```bash
strings praktek1_hello.pcap | grep -o "flag{[^}]*}"
```

## Jawab

1. Tulis flag yang kamu temukan.
2. Kapan (detik ke berapa) paket HTTP response dikirim?
3. Aplikasi apa yang dipakai klien untuk mengirim request (lihat header User-Agent)?
4. Mengapa menurutmu PCAP disebut "rekaman CCTV jaringan"?

## Pembahasan singkat

File ini sengaja dibuat kecil supaya kamu fokus pada mekanisme dasar: membaca PCAP, memfilter, dan mengekstrak data. Di praktik berikutnya traffic akan lebih ramai dan mulai ada yang disembunyikan. Semua command yang kamu pakai di sini akan terus dipakai sampai capstone.
