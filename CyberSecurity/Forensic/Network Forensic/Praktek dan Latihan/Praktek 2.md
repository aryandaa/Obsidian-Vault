#latihan 

Praktik ini fokus pada **membaca protokol**: three-way handshake, layanan FTP, dan koneksi ke port yang tidak biasa. File `praktek2_protocol.pcap` berisi tiga percakapan:

```text
Files/praktek2_protocol.pcap
```

Tiga percakapan yang ada: HTTP ke port 80, FTP ke port 21, dan satu koneksi misterius ke port 4444.

## Langkah 1: Lihat gambaran percakapan

```bash
cd "Network Forensic/Files"
```

```bash
tshark -r praktek2_protocol.pcap -q -z conv,tcp
```

Output menunjukkan tiga percakapan TCP. Catat pasangan IP:port masing-masing. Dari sini kamu sudah bisa menebak layanan apa yang berjalan di tiap port.

## Langkah 2: Baca daftar paket lengkap

```bash
tshark -r praktek2_protocol.pcap
```

Perhatikan urutan flag TCP pada sesi pertama:

```text
SYN
SYN, ACK
ACK
```

Itulah **three-way handshake**. Cari tiga paket tersebut dan catat sequence number-nya.

## Langkah 3: Analisis FTP

FTP adalah protokol teks polos, semua perintahnya bisa dibaca.

```bash
tshark -r praktek2_protocol.pcap -Y "ftp.request" -T fields -e ftp.request.command -e ftp.request.arg
```

Kamu akan melihat perintah `USER` dan `PASS` beserta argumennya. Tulis jawaban:

1. Username apa yang dipakai?
2. Password apa yang dipakai?
3. Mengapa ini berbahaya bagi pemilik akun?

## Langkah 4: Analisis koneksi port 4444

```bash
tshark -r praktek2_protocol.pcap -Y "tcp.port == 4444"
```

Lihat paket-paketnya. Kemudian ekstrak payload-nya:

```bash
tshark -r praktek2_protocol.pcap -Y "tcp.port == 4444" -T fields -e tcp.payload | xxd -r -p
```

Tulis jawaban:

4. Apa isi pesan yang dikirim pada port 4444?
5. Port 4444 adalah port yang tidak standar. Apa artinya sebuah layanan berjalan di port yang tidak biasa?
6. Tulis flag yang kamu temukan.

## Langkah 5: Protokol hierarchy

```bash
tshark -r praktek2_protocol.pcap -q -z io,phs
```

Lihat hierarki protokol: Ethernet → IP → TCP → (HTTP, FTP). Ini menunjukkan bagaimana protokol saling membungkus.

## Jawab

1. Sebutkan tiga percakapan TCP beserta layanannya.
2. Jelaskan urutan three-way handshake beserta flag-nya.
3. Tulis kredensial FTP yang bocor.
4. Tulis isi pesan port 4444 dan flag-nya.
5. Mengapa port saja tidak cukup untuk menentukan protokol?

## Pembahasan singkat

FTP mengirim kredensial dalam teks polos. Ini alasan utama kenapa FTP dianggap tidak aman dan digantikan SFTP/FTPS. Sementara koneksi ke port 4444 menunjukkan pola yang sering dipakai malware atau tool admin: layanan berjalan di port non-standar supaya tidak menarik perhatian. Di praktik berikutnya, kamu akan belajar menyaring traffic campuran untuk menemukan hal yang tidak biasa.
