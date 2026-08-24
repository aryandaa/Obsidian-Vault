#latihan 

Praktik ini fokus pada **DNS forensic**, termasuk menemukan exfiltration data lewat subdomain. File `praktek4_dns.pcap` berisi query DNS normal, satu query TXT, beberapa query mencurigakan, dan noise DGA.

```text
Files/praktek4_dns.pcap
```

## Langkah 1: Daftar semua query DNS

```bash
cd "Network Forensic/Files"
```

```bash
tshark -r praktek4_dns.pcap -Y "dns.flags.response == 0" -T fields -e dns.qry.name
```

Perhatikan filter `dns.flags.response == 0`. Coba bandingkan dengan tanpa filter:

```bash
tshark -r praktek4_dns.pcap -Y "dns.qry.name" -T fields -e dns.qry.name
```

Kenapa daftar pertama lebih bersih? (Petunjuk: query DNS muncul dua kali, sekali di paket query dan sekali di paket response.)

## Langkah 2: Identifikasi domain mencurigakan

Dari daftar query, pisahkan mana yang normal dan mana yang tidak wajar. Tanda yang perlu diperhatikan:

- Label subdomain yang sangat panjang.
- Domain yang tidak dikenal.
- Pola label acak.

Coba perintah ini untuk menampilkan query dengan label pertama yang panjang:

```bash
tshark -r praktek4_dns.pcap -Y "dns.flags.response == 0" -T fields -e dns.qry.name | awk -F. 'length($1) > 20'
```

## Langkah 3: Cek response code

Beberapa query menghasilkan NXDOMAIN (domain tidak ada). Ini pola DGA.

```bash
tshark -r praktek4_dns.pcap -Y "dns.flags.rcode == 3" -T fields -e dns.qry.name
```

Domain apa yang menghasilkan NXDOMAIN? Apa cirinya?

## Langkah 4: Decode label hex

Subdomain yang panjang ternyata berisi data hex. Ambil label sebelum titik pertama, gabungkan, lalu decode:

```bash
tshark -r praktek4_dns.pcap -Y "dns.qry.name contains exfil && dns.flags.response == 0" -T fields -e dns.qry.name | sed 's/\..*//' | tr -d '\n' | xxd -r -p
```

Tulis flag yang kamu temukan.

Kalau kamu ingin melihat langkah demi langkah, coba potong perintahnya:

```bash
tshark -r praktek4_dns.pcap -Y "dns.qry.name contains exfil && dns.flags.response == 0" -T fields -e dns.qry.name
```

```bash
tshark -r praktek4_dns.pcap -Y "dns.qry.name contains exfil && dns.flags.response == 0" -T fields -e dns.qry.name | sed 's/\..*//'
```

## Langkah 5: Lihat record TXT

```bash
tshark -r praktek4_dns.pcap -Y "dns.qry.type == 16" -T fields -e dns.qry.name -e dns.txt
```

Query TXT ke `verify.example.com` berisi apa? Ini contoh TXT yang dipakai untuk verifikasi domain, tapi ingat: TXT bisa disalahgunakan untuk menyembunyikan data.

## Jawab

1. Sebutkan domain-domain normal yang di-query.
2. Sebutkan domain mencurigakan dan jelaskan cirinya.
3. Domain apa yang menghasilkan NXDOMAIN, dan apa artinya dalam konteks DGA?
4. Tulis flag yang kamu temukan di subdomain.
5. Mengapa penyerang memilih DNS untuk mengirim data keluar?

## Pembahasan singkat

Exfiltration lewat DNS memanfaatkan fakta bahwa query DNS terlihat normal dan jarang diblokir firewall. Data dipecah menjadi potongan kecil, ditaruh di subdomain, lalu dikirim keluar sedikit demi sedikit. Sebagai investigator, label subdomain yang panjang dan tidak masuk akal adalah tanda merah yang paling jelas. Di praktik berikutnya kamu akan menganalisis HTTP yang menyembunyikan kredensial dan file.
