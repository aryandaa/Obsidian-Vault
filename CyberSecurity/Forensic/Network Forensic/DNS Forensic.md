#cybersecurity 

DNS (Domain Name System) adalah **buku telepon internet**: ia menerjemahkan nama domain seperti `example.com` menjadi alamat IP seperti `93.184.216.34`. Hampir semua aktivitas jaringan dimulai dengan query DNS. Itu sebabnya DNS adalah salah satu sumber artefak terbaik dalam forensic: **setiap kali seseorang mengakses sesuatu, jejak DNS bisa tertinggal.**

Dari sudut pandang investigator, DNS menarik karena:

1. Ia memetakan aktivitas pengguna ke nama domain, bukan sekadar IP.
2. Query DNS sering tersimpan di cache host dan log server.
3. Penyerang sering menyalahgunakan DNS untuk command & control dan exfiltrasi data.
4. DNS menggunakan UDP (port 53) dan payload-nya bisa dibaca polos.

## Cara kerja DNS

Ketika sebuah mesin ingin mengakses `example.com`:

```text
Client → Resolver (misal 8.8.8.8 atau gateway) : "apa IP example.com?"
Resolver → Client : "93.184.216.34"
```

Query dan response dikirim dalam satu paket UDP. Paket query berisi:

```text
Transaction ID (untuk mencocokkan query dan response)
Flags (apakah ini query atau response, dll)
Question: nama domain + tipe record
```

Paket response berisi:

```text
Transaction ID yang sama
Answer: alamat IP atau data record
Response code (NOERROR, NXDOMAIN, dll)
```

Di tshark, field penting yang sering dipakai:

```text
dns.qry.name          nama yang di-query
dns.qry.type          tipe record (1 = A, 16 = TXT, dll)
dns.flags.response    0 = query, 1 = response
dns.a                 alamat IP hasil resolve
dns.resp.ttl          time to live
dns.flags.rcode       response code (0 = NOERROR, 3 = NXDOMAIN)
```

## Tipe record yang perlu kamu kenali

```text
A        → alamat IPv4
AAAA     → alamat IPv6
CNAME    → alias domain
MX       → mail server
TXT      → teks bebas (sering dipakai verifikasi, bisa disalahgunakan)
NS       → name server
SOA      → otoritas zone
PTR      → reverse DNS (IP → nama)
```

Dalam forensic, **TXT** adalah tipe yang paling sering disalahgunakan untuk menyembunyikan data, karena isinya bebas teks. Tapi yang paling umum untuk exfiltrasi adalah menyembunyikan data di **subdomain** query A.

## Pola DNS mencurigakan

1. **DGA (Domain Generation Algorithm)**: malware menghasilkan banyak domain acak secara berkala. Cirinya: label acak seperti `a1b2c3d4.botnet.net`, banyak query yang menghasilkan NXDOMAIN, dan pola waktu yang teratur.

2. **DNS tunneling / exfiltration**: data dikirim keluar dengan menyembunyikannya di subdomain. Contoh:

```text
666c61677b646e735f... .exfil-server.net
```

Bagian sebelum titik pertama adalah data terenkode (sering hex atau base32). Query semacam ini biasanya banyak, berukuran label panjang, dan menuju domain yang tidak wajar.

3. **Fast flux**: satu domain berganti-ganti IP jawaban dengan sangat cepat untuk menghindari pemblokiran.

4. **Typosquatting**: domain yang mirip dengan domain terkenal (`gooogle.com`) untuk phishing.

## Menganalisis DNS dengan tshark

Daftar semua query DNS:

```bash
tshark -r file.pcap -Y "dns.flags.response == 0" -T fields -e dns.qry.name
```

Perhatikan filter `dns.flags.response == 0`. Ini penting: sebuah query DNS muncul dua kali di capture, sekali sebagai paket query dan sekali di dalam paket response (question section di-echo). Filter ini menghindari duplikasi.

Daftar semua domain yang di-query beserta tipe record:

```bash
tshark -r file.pcap -Y "dns.flags.response == 0" -T fields -e dns.qry.name -e dns.qry.type
```

Lihat response code (NXDOMAIN bisa menandakan DGA):

```bash
tshark -r file.pcap -Y "dns.flags.rcode == 3" -T fields -e dns.qry.name
```

Lihat hasil resolve:

```bash
tshark -r file.pcap -Y "dns.flags.response == 1 && dns.qry.type == 1" -T fields -e dns.qry.name -e dns.a
```

Mencari subdomain panjang yang mencurigakan (calon exfil):

```bash
tshark -r file.pcap -Y "dns.qry.name" -T fields -e dns.qry.name | awk -F. 'length($1) > 20'
```

menampilkan query dengan label pertama lebih dari 20 karakter.

## Mendekode subdomain exfil

Ketika kamu menemukan label hex di subdomain, gabungkan dan decode:

```bash
tshark -r file.pcap -Y "dns.qry.name contains exfil && dns.flags.response == 0" -T fields -e dns.qry.name | sed 's/\..*//' | tr -d '\n' | xxd -r -p
```

Penjelasan per bagian:

```text
sed 's/\..*//'   → ambil bagian sebelum titik pertama (label hex)
tr -d '\n'       → gabungkan semua label jadi satu baris
xxd -r -p        → ubah hex menjadi teks
```

Hasilnya adalah data yang disembunyikan di subdomain. Kalau data memakai base32 atau base64, sesuaikan tool decode-nya.

```
Pola pikir: ketika kamu melihat subdomain yang panjang dan tidak masuk
akal, jangan lewatkan. Di baliknya bisa ada data exfiltrasi atau flag.
```

## DNS cache di host

Query DNS tidak hanya ada di PCAP. Host menyimpan cache-nya sendiri:

- Windows: `ipconfig /displaydns`
- Linux: `systemd-resolve --cache` atau file di `/run/systemd/resolve/`
- Isi `/etc/hosts` untuk mapping statis

Cache DNS bisa menunjukkan domain apa yang pernah diakses meski PCAP tidak tersedia. Ini akan kita dalami di materi Host Network Artifacts.

## Pertanyaan yang harus kamu jawab saat menganalisis DNS

1. Domain apa saja yang di-query?
2. Siapa yang melakukan query (IP sumber)?
3. Kapan query terjadi (timestamp)?
4. Apakah ada domain yang mencurigakan?
5. Apakah ada pola DGA (banyak NXDOMAIN)?
6. Apakah ada label subdomain yang panjang (exfil)?
7. Apakah response IP konsisten antar query?

DNS jarang menjadi satu-satunya jawaban, tetapi ia sering menjadi **pintu masuk** menuju temuan besar.

Sekarang kita praktikkan analisis DNS pada PCAP yang berisi traffic DNS normal dan mencurigakan: [Praktek 4](Praktek%20dan%20Latihan/Praktek%204.md)
