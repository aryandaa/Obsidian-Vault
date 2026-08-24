#latihan 

Praktik ini mensimulasikan **traffic malware**: sebuah mesin korban melakukan beacon ke server C2, lalu mengirim data hasil exfiltration. File `praktek6_c2.pcap` berisi semua komunikasi tersebut.

```text
Files/praktek6_c2.pcap
```

## Langkah 1: Cari percakapan mencurigakan

```bash
cd "Network Forensic/Files"
```

```bash
tshark -r praktek6_c2.pcap -q -z conv,tcp
```

Ada satu pasangan IP yang menonjol: korban `192.168.1.50` bicara ke `203.0.113.77` pada port 8080. Catat pasangan tersebut.

## Langkah 2: Amati pola beacon

Lihat request HTTP ke server tersebut beserta waktunya:

```bash
tshark -r praktek6_c2.pcap -Y "ip.addr == 203.0.113.77 && http.request" -T fields -e frame.time_relative -e http.request.uri
```

Perhatikan waktunya. Apakah ada interval yang teratur? Hitung selisih antar request.

Tulis jawaban:

1. IP server C2 dan port-nya.
2. Interval beacon (berapa detik sekali).
3. URI pattern yang dipakai beacon.

## Langkah 3: Periksa User-Agent

```bash
tshark -r praktek6_c2.pcap -Y "http.user_agent" -T fields -e http.user_agent | sort | uniq -c
```

Apa yang aneh dari User-Agent yang dipakai? (Petunjuk: lihat versi browser dan sistem operasi yang diklaim.)

## Langkah 4: Analisis parameter request

Lihat URI lengkap beacon:

```bash
tshark -r praktek6_c2.pcap -Y "http.request.method == GET" -T fields -e http.request.full_uri
```

Ada parameter `key` yang berisi teks aneh. Itu adalah potongan base64. Catat: potongan yang sama dikirim berulang kali (ciri beacon yang mengirim status, bukan data baru).

## Langkah 5: Temukan POST exfiltration

Ada satu request yang berbeda: `POST /exfil`.

```bash
tshark -r praktek6_c2.pcap -Y "http.request.method == POST" -T fields -e tcp.payload | xxd -r -p
```

Isi body-nya adalah base64. Decode:

```bash
echo "<nilai_base64>" | base64 -d
```

atau langsung dari pipeline:

```bash
tshark -r praktek6_c2.pcap -Y "http.request.method == POST" -T fields -e tcp.payload | xxd -r -p | tail -1 | base64 -d
```

Tulis flag yang kamu temukan.

## Langkah 6: Periksa pola DNS

Apakah ada query DNS ke domain yang berhubungan? 

```bash
tshark -r praktek6_c2.pcap -Y "dns.flags.response == 0" -T fields -e dns.qry.name
```

## Jawab

1. IP server C2, port, dan interval beacon.
2. URI pattern beacon.
3. Apa yang aneh dari User-Agent?
4. Tulis flag yang dikirim lewat POST /exfil.
5. Sebutkan IOC (Indicator of Compromise) dari traffic ini.

## Pembahasan singkat

Pola beacon terlihat dari keteraturan interval dan URI yang sama berulang kali. User-Agent lama (`MSIE 7.0`) adalah penanda umum malware. Data exfiltration dikirim dalam base64 yang bisa langsung di-decode. Dalam investigasi nyata, IOC seperti IP C2, interval, dan User-Agent inilah yang dibagikan ke seluruh organisasi untuk mendeteksi serangan yang sama. Di praktik berikutnya kamu berpindah dari PCAP ke artifacts di dalam host.
