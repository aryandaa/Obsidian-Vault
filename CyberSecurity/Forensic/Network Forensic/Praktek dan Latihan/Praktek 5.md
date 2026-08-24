#latihan 

Praktik ini fokus pada **analisis HTTP**: menemukan kredensial, membaca header, dan mengambil file yang diunduh. File `praktek5_http.pcap` berisi tiga sesi HTTP ke `web.lab.local`.

```text
Files/praktek5_http.pcap
```

## Langkah 1: Daftar semua request HTTP

```bash
cd "Network Forensic/Files"
```

```bash
tshark -r praktek5_http.pcap -Y "http.request" -T fields -e http.request.method -e http.request.uri
```

Kamu akan melihat tiga request: `GET /login`, `GET /admin`, dan `GET /files/flag.txt`. Perhatikan alurnya: sepertinya pengguna login, masuk ke admin, lalu mengunduh file.

## Langkah 2: Lihat response pertama

```bash
tshark -r praktek5_http.pcap -Y "http.response" -T fields -e http.response.code -e http.response.phrase
```

Response pertama adalah `401 Unauthorized`. Server meminta autentikasi.

## Langkah 3: Temukan kredensial

Request kedua membawa header `Authorization`. Ekstrak:

```bash
tshark -r praktek5_http.pcap -Y "http.authorization" -T fields -e http.authorization
```

Kamu akan mendapat sesuatu seperti:

```text
Basic Ym9iYnk6c3VwM3Jfc2VjM3J0
```

Bagian setelah kata `Basic` adalah base64 dari `username:password`. Decode:

```bash
echo "Ym9iYnk6c3VwM3Jfc2VjM3J0" | base64 -d
```

(ganti dengan nilai yang kamu dapatkan)

Tulis username dan password yang kamu temukan.

## Langkah 4: Lihat cookie

Periksa header cookie pada request kedua dan ketiga:

```bash
tshark -r praktek5_http.pcap -Y "http.cookie" -T fields -e http.cookie
```

Cookie apa yang dipakai? Mengapa cookie penting dalam investigasi (petunjuk: menghubungkan beberapa request ke satu pengguna)?

## Langkah 5: Ekstrak file yang diunduh

Request ketiga mengambil `/files/flag.txt`. Ekstrak seluruh payload TCP pada port 80:

```bash
tshark -r praktek5_http.pcap -Y "tcp.port == 80" -T fields -e tcp.payload | xxd -r -p
```

Di bagian akhir output, kamu akan melihat response yang berisi flag. Tulis flag-nya.

Alternatif: cari flag langsung dengan strings:

```bash
strings praktek5_http.pcap | grep -o "flag{[^}]*}"
```

## Jawab

1. Sebutkan alur tiga request HTTP yang terjadi.
2. Tulis kredensial yang bocor (username:password).
3. Sebutkan cookie session yang dipakai.
4. Tulis flag yang diunduh.
5. Mengapa HTTP polos berbahaya untuk autentikasi?

## Pembahasan singkat

Basic auth mengirim kredensial dalam base64, yang bisa dibaca siapa saja yang punya akses ke PCAP. Cookie memungkinkan investigator mengikuti aktivitas satu pengguna. Dan file yang diunduh lewat HTTP bisa diekstrak langsung dari payload. Semua ini tidak mungkin jika memakai HTTPS. Di praktik berikutnya, kamu menganalisis pola C2 yang jauh lebih tersembunyi.
