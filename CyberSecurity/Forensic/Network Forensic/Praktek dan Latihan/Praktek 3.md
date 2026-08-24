#latihan 

Praktik ini menguji kemampuanmu **menyaring traffic campuran**. File `praktek3_filter.pcap` berisi campuran DNS, HTTP ke beberapa server, dan satu koneksi mencurigakan yang menyembunyikan flag. Tugasmu: temukan flag dengan filter yang tepat, tanpa membaca semua paket satu per satu.

```text
Files/praktek3_filter.pcap
```

## Langkah 1: Kenali isi file

```bash
cd "Network Forensic/Files"
```

```bash
tshark -r praktek3_filter.pcap -q -z io,phs
```

Perhatikan protokol yang ada: berapa paket DNS, berapa HTTP, dan apa saja yang lain.

## Langkah 2: Daftar percakapan

```bash
tshark -r praktek3_filter.pcap -q -z conv,tcp
```

Catat semua pasangan IP:port. Ada beberapa percakapan HTTP ke server berbeda, dan satu percakapan yang menonjol.

## Langkah 3: Lihat port-port yang tidak biasa

Filter semua paket TCP:

```bash
tshark -r praktek3_filter.pcap -Y "tcp" -T fields -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport
```

Perhatikan: sebagian besar traffic memakai port 80, tetapi ada satu percakapan dengan port 1337. Itu bukan port standar layanan web.

## Langkah 4: Periksa port 1337

```bash
tshark -r praktek3_filter.pcap -Y "tcp.port == 1337"
```

Lihat detail paket-paketnya. Kemudian ekstrak payload:

```bash
tshark -r praktek3_filter.pcap -Y "tcp.port == 1337" -T fields -e tcp.payload | xxd -r -p
```

Tulis flag yang kamu temukan.

## Langkah 5: Bandingkan dengan lalu lintas normal

Coba beberapa filter untuk memahami traffic "normal" di file ini:

```bash
tshark -r praktek3_filter.pcap -Y "dns.flags.response == 0" -T fields -e dns.qry.name
```

```bash
tshark -r praktek3_filter.pcap -Y "http.request" -T fields -e http.request.uri -e http.host
```

Perhatikan bahwa traffic normal tampak rutin: query DNS biasa, GET asset web. Yang menonjol justru yang tidak biasa.

## Jawab

1. Protokol apa saja yang ada di file ini?
2. Berapa percakapan TCP yang terjadi?
3. IP dan port apa yang dipakai koneksi mencurigakan?
4. Tulis flag yang kamu temukan.
5. Filter apa yang paling efektif untuk menemukan flag?

## Pembahasan singkat

Filter adalah keterampilan inti: di PCAP besar, membaca semua paket tidak mungkin. Strategi yang benar adalah menyempitkan dari gambaran luas (protocol hierarchy, conversations) ke detail yang mencurigakan (port tidak standar), lalu memeriksa isinya. Di praktik berikutnya, data yang disembunyikan tidak berada di port aneh, melainkan di dalam protokol yang sangat normal: DNS.
