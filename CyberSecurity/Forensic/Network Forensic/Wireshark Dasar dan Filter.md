#cybersecurity 

Wireshark adalah tool utama untuk membaca PCAP. Versi command line-nya bernama **tshark**, dan di modul ini kita akan banyak menggunakan tshark karena lebih cepat, mudah di-script, dan output-nya bisa diproses dengan grep. Wireshark GUI berguna ketika kamu ingin eksplorasi visual dan klik sana-sini.

Prinsip yang harus kamu pegang sejak awal: **Wireshark dan tshark adalah kaca pembesar, bukan otak.** Mereka menampilkan paket, tapi analisis tetap dilakukan olehmu. Filter yang tepat adalah kunci efisiensi: PCAP besar tanpa filter adalah lautan paket yang tidak ada habisnya.

## Instalasi

```bash
sudo apt update
sudo apt install wireshark tshark
```

Pada saat instalasi, kamu akan ditanya apakah user non-root boleh menangkap paket. Untuk analisis file PCAP, tidak perlu izin khusus; cukup baca file.

Verifikasi:

```bash
tshark --version
```

```bash
wireshark --version
```

## Membaca file PCAP dengan tshark

```bash
tshark -r file.pcap
```

`-r` artinya membaca file. Outputnya adalah daftar paket:

```text
    1   0.000000 192.168.1.50 → 192.168.1.10 TCP 74 50000 → 80 [SYN] Seq=0
    2   1.000000 192.168.1.10 → 192.168.1.50 TCP 74 80 → 50000 [SYN, ACK] Seq=0
    3   2.000000 192.168.1.50 → 192.168.1.10 TCP 66 50000 → 80 [ACK] Seq=1 Ack=1
    4   3.000000 192.168.1.50 → 192.168.1.10 HTTP 151 GET / HTTP/1.1
```

Kolom yang ditampilkan: nomor paket, waktu relatif, sumber, tujuan, protokol, panjang, dan ringkasan.

Kalau file besar, jangan buka semua sekaligus. Mulai dari pandangan luas:

```bash
tshark -r file.pcap -c 20
```

hanya menampilkan 20 paket pertama.

## Melihat informasi file dengan capinfos

Sebelum analisis, kenali dulu file-nya:

```bash
capinfos file.pcap
```

Output menampilkan nama file, ukuran, durasi capture, jumlah paket, dan link layer type. Informasi ini penting untuk dokumentasi evidence.

```bash
capinfos -c file.pcap
```

hanya menampilkan jumlah paket.

## Filter display: cara mempersempit

Filter display (tshark `-Y`) menentukan paket mana yang ditampilkan. Ini senjata utama analisis.

Filter dasar yang wajib kamu kuasai:

```bash
-Y "ip.addr == 192.168.1.50"
```

semua paket yang melibatkan IP tersebut (sumber atau tujuan).

```bash
-Y "ip.src == 192.168.1.50"
```

hanya paket dari IP tersebut.

```bash
-Y "tcp.port == 80"
```

semua paket yang melibatkan port 80.

```bash
-Y "tcp.port == 4444"
```

paket pada port 4444.

```bash
-Y "dns"
```

semua paket DNS.

```bash
-Y "http"
```

semua paket HTTP.

```bash
-Y "tcp.flags.syn == 1"
```

hanya paket dengan flag SYN (bagus untuk melihat handshake dan scan).

```bash
-Y "frame contains \"flag\""
```

paket yang isinya mengandung teks "flag". Ini sering menjadi jalan pintas di CTF.

Kombinasi dengan operator logika:

```bash
-Y "ip.src == 192.168.1.50 && tcp.port == 8080"
```

```bash
-Y "dns || http"
```

```bash
-Y "http && !http.response"
```

request HTTP saja, tanpa response.

## Melihat isi paket dengan -x

```bash
tshark -r file.pcap -Y "tcp.port == 4444" -x
```

menampilkan byte mentah paket dalam hex dan ASCII. Ini setara dengan `xxd` pada paket.

## Menampilkan field tertentu dengan -T fields

Ini cara paling powerful untuk mengekstrak informasi terstruktur.

```bash
tshark -r file.pcap -T fields -e ip.src -e ip.dst -e tcp.port
```

Setiap `-e` mengambil satu field. Daftar field yang sering dipakai:

```text
frame.time
frame.time_relative
ip.src, ip.dst
tcp.srcport, tcp.dstport
tcp.flags
dns.qry.name
http.request.method
http.request.uri
http.authorization
http.user_agent
http.file_data
tcp.payload
```

Contoh menampilkan semua nama domain yang di-query:

```bash
tshark -r file.pcap -Y "dns.qry.name" -T fields -e dns.qry.name
```

Contoh menampilkan URI request:

```bash
tshark -r file.pcap -Y "http.request" -T fields -e http.request.uri
```

## Mengikuti stream (follow stream)

Konsep "follow stream" di Wireshark = menggabungkan semua segmen dari satu koneksi TCP menjadi satu aliran data utuh, supaya kamu bisa membaca percakapan lengkap.

Di tshark, cara sederhananya: filter berdasarkan port pasangan, lalu ekstrak payload:

```bash
tshark -r file.pcap -Y "tcp.port == 8080" -T fields -e tcp.payload | xxd -r -p
```

Hasilnya adalah data mentah seluruh koneksi pada port tersebut. Dari situ kamu bisa membaca HTTP, FTP, atau protokol lain sebagai teks.

Di Wireshark GUI: klik kanan pada paket, pilih "Follow" lalu "TCP Stream".

## Statistik percakapan

Sebelum tahu mau lihat apa, lihat dulu siapa yang bicara dengan siapa:

```bash
tshark -r file.pcap -q -z conv,tcp
```

menampilkan tabel percakapan TCP (pasangan IP:port, jumlah paket, jumlah byte).

```bash
tshark -r file.pcap -q -z io,stat,5
```

menampilkan statistik paket per interval 5 detik. Ini sangat berguna untuk menemukan pola beacon yang berulang.

```bash
tshark -r file.pcap -q -z endpoints,ip
```

daftar IP yang muncul.

```bash
tshark -r file.pcap -q -z io,phs
```

protokol hierarchy: persentase tiap protokol dalam capture.

## Wireshark GUI: warna dan navigasi

Di Wireshark GUI, paket diberi warna berdasarkan protokol. Beberapa warna penting:

- Hijau muda: TCP traffic.
- Biru muda: UDP.
- Kuning: HTTP.
- Oranye/merah: paket yang mencurigakan atau error (misal TCP RST).

Kolom atas menampilkan ringkasan, panel tengah menampilkan detail berlapis (Ethernet, IP, TCP, data), panel bawah menampilkan byte mentah. Klik field di tengah, byte yang bersesuaian langsung ter-highlight di bawah.

## Menggabung dan memotong PCAP

```bash
mergecap -w gabungan.pcap file1.pcap file2.pcap
```

menggabungkan beberapa PCAP.

```bash
editcap -c 1000 file.pcap potongan.pcap
```

membagi PCAP menjadi beberapa file masing-masing 1000 paket.

```bash
editcap -A "2026-08-12 15:00:00" -B "2026-08-12 16:00:00" file.pcap rentang.pcap
```

memotong berdasarkan rentang waktu.

## Timezone dan waktu

Waktu sangat penting di forensic. Periksa timezone capture:

```bash
capinfos file.pcap | grep -i time
```

Wireshark menampilkan waktu relatif (sejak awal capture) dan absolut. Selalu catat timezone saat mendokumentasikan temuan, karena timestamp antar evidence bisa berbeda zona.

## Alur kerja membaca PCAP

```text
capinfos file.pcap
    ↓
tshark -r file.pcap -c 20 (intip dulu)
    ↓
tshark -q -z conv,tcp (siapa bicara dengan siapa)
    ↓
tshark -q -z io,phs (protokol apa saja)
    ↓
Filter protokol mencurigakan
    ↓
Follow stream / ekstrak payload
    ↓
Analisis mendalam
```

Jangan langsung menyelam ke paket pertama. Lihat dulu peta besarnya, baru zoom ke detail.

Sekarang kita praktikkan dengan PCAP yang berisi campuran traffic: [Praktek 3](Praktek%20dan%20Latihan/Praktek%203.md)
