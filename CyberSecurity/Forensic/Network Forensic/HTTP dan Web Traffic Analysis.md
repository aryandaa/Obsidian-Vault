#cybersecurity 

HTTP adalah protokol yang menggerakkan web, dan dalam dunia forensic ia adalah **harta karun**: karena HTTP biasanya dikirim polos (tanpa enkripsi), seluruh request, header, cookie, bahkan kredensial bisa dibaca langsung dari PCAP. Banyak sekali serangan yang berjalan di atas HTTP, dan banyak juga flag CTF yang bersembunyi di dalamnya.

Di modul ini kita belajar membaca HTTP seperti membaca surat: siapa yang mengirim, ke mana, apa isinya, dan apa balasannya.

## Struktur request HTTP

Sebuah request HTTP terdiri dari:

```text
Request Line
Header
Body (opsional)
```

Contoh:

```text
GET /files/flag.txt HTTP/1.1
Host: web.lab.local
User-Agent: Mozilla/5.0
Cookie: session=abc123
Authorization: Basic Ym9iYnk6c3VwM3Jfc2VjM3J0

```

Baris pertama berisi tiga hal: **method**, **path**, dan **versi HTTP**. Method yang perlu kamu kenali:

```text
GET     → mengambil data
POST    → mengirim data (login, upload, form)
PUT     → menyimpan data ke server
DELETE  → menghapus data
HEAD    → mengambil header saja
```

Path menunjukkan resource yang diminta. Dalam investigasi, kombinasi method + path sering langsung bercerita: `POST /admin/upload.php` jelas berbeda dengan `GET /`.

## Struktur response HTTP

```text
Status Line
Header
Body
```

Contoh:

```text
HTTP/1.1 200 OK
Content-Type: text/plain
Content-Length: 67

flag{...}
```

Status code yang sering muncul:

```text
200  OK
301/302  Redirect
401  Unauthorized (butuh autentikasi)
403  Forbidden
404  Not Found
500  Internal Server Error
```

Dalam investigasi, perhatikan status code untuk menilai apakah sebuah aksi berhasil. `302` setelah login biasanya berarti login berhasil diarahkan ke halaman baru. `200` pada upload berarti file berhasil disimpan.

## Header yang menyimpan bukti

Beberapa header HTTP sangat bernilai untuk forensic:

```text
Host            → nama domain yang dituju
User-Agent      → aplikasi/OS yang dipakai klien
Referer         → halaman sebelumnya (jejak alur pengguna)
Cookie          → session identifier
Authorization   → kredensial (sering dalam bentuk Basic)
Content-Type    → tipe isi body
Content-Length  → ukuran body
Set-Cookie      → server memberi session ke klien
```

### User-Agent

User-Agent bisa menjadi petunjuk penting. `curl/8.5.0` menandakan penggunaan script, `Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.1)` yang aneh bisa menandakan malware yang menyamar. Perhatikan User-Agent yang tidak lazim.

### Authorization dan Basic Auth

Basic auth mengirim kredensial dalam bentuk:

```text
Authorization: Basic base64(user:password)
```

Bagian setelah `Basic` adalah base64 dari `username:password`. Untuk membacanya:

```bash
echo "Ym9iYnk6c3VwM3Jfc2VjM3J0" | base64 -d
```

Hasilnya:

```text
bobby:sup3r_s3cr3t
```

Di tshark, field-nya:

```bash
tshark -r file.pcap -Y "http.authorization" -T fields -e http.authorization
```

```
Kredensial dalam Basic auth adalah plaintext yang dimasukkan ke base64,
bukan enkripsi. Siapa pun yang melihat PCAP bisa membacanya.
```

### Cookie dan session

Cookie `session=abc123` memungkinkan investigator menghubungkan beberapa request ke satu pengguna yang sama. Dalam analisis, cookie membantu membangun alur aktivitas pengguna: dia login, lalu mengakses halaman yang butuh autentikasi.

## Field tshark untuk HTTP

```text
http.request.method      method (GET, POST, ...)
http.request.uri         path yang diminta
http.host                header Host
http.user_agent          User-Agent
http.authorization       header Authorization
http.cookie              header Cookie
http.response.code       status code
http.content_type        Content-Type
http.content_length      Content-Length
http.file_data           isi body
```

Contoh daftar semua request:

```bash
tshark -r file.pcap -Y "http.request" -T fields -e http.request.method -e http.request.uri -e http.host
```

Contoh response beserta status:

```bash
tshark -r file.pcap -Y "http.response" -T fields -e http.response.code -e http.content_type
```

## Mengikuti aliran HTTP lengkap

Untuk membaca percakapan HTTP secara utuh, ekstrak payload TCP pada port 80:

```bash
tshark -r file.pcap -Y "tcp.port == 80" -T fields -e tcp.payload | xxd -r -p
```

Hasilnya seluruh request dan response sebagai teks. Di Wireshark GUI, gunakan "Follow TCP Stream" untuk melihat aliran yang sama dengan lebih nyaman.

## Mengekstrak file dari HTTP

File yang diunduh lewat HTTP bisa diambil dari payload response.

Cara praktis: cari response yang berisi `Content-Disposition` atau `Content-Type` file, lalu ekstrak body-nya.

```bash
tshark -r file.pcap -Y "http.response" -T fields -e tcp.payload | xxd -r -p > response.bin
```

Kemudian pisahkan header dan body, atau gunakan `strings` untuk melihat isi teks:

```bash
strings response.bin
```

Di Wireshark GUI ada fitur "Export Objects" (File → Export Objects → HTTP) yang mengekstrak semua file yang lewat di HTTP secara otomatis.

## HTTP vs HTTPS

HTTPS mengenkripsi seluruh isi komunikasi (TLS). Yang bisa dilihat investigator hanyalah:

```text
Siapa (IP)
Kapan (timestamp)
Ke mana (SNI, sering masih terlihat)
Berapa besar (ukuran data)
```

Isi request dan response tidak terbaca kecuali kamu punya kunci privat server atau keylog file dari klien. Dalam lomba, HTTPS jarang diberikan tanpa kunci karena tidak bisa diselesaikan. HTTP polos adalah yang paling sering diuji.

## Pola HTTP yang perlu diperhatikan

1. **POST ke endpoint upload**: calon upload webshell atau file jahat.
2. **Parameter dengan data terenkode**: `?data=ZmxhZ3...` bisa jadi payload base64.
3. **User-Agent tidak lazim**: penanda script otomatis atau malware.
4. **Basic auth tanpa HTTPS**: kredensial terbuka.
5. **Response besar setelah GET kecil**: download file, bisa jadi payload stage berikutnya.
6. **Cookie yang sama dipakai banyak request**: alur aktivitas satu pengguna.

Sekarang kita praktikkan analisis HTTP pada PCAP yang berisi login, kredensial, dan download file: [Praktek 5](Praktek%20dan%20Latihan/Praktek%205.md)
