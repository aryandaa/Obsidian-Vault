#programming 

Setelah memahami bahwa program adalah sekumpulan instruksi untuk menyelesaikan masalah menggunakan komputer, sekarang kita masuk ke pertanyaan berikutnya: **siapa yang membuat instruksi tersebut?**

Jawabannya adalah programmer.

Namun, kalau programmer hanya didefinisikan sebagai "orang yang menulis kode", definisi itu terlalu dangkal. Menulis kode hanyalah salah satu aktivitas yang dilakukan programmer. Bahkan dalam pekerjaan nyata, menulis kode sering kali bukan bagian yang paling sulit.

Seorang programmer sebenarnya bertugas **menerjemahkan masalah menjadi solusi yang dapat dijalankan oleh komputer**.

Misalnya seseorang berkata:
> "Saya ingin membuat sistem login."

Kalimat tersebut belum merupakan program. Bahkan belum merupakan algoritma. Itu baru sebuah **kebutuhan**.

Programmer harus memecahnya menjadi pertanyaan yang lebih konkret.
```text
Apa yang harus dimasukkan user?

→ Username
→ Password

Apa yang harus dilakukan sistem?

→ Mencari username
→ Memeriksa password
→ Membandingkan data
→ Menentukan apakah login valid

Apa hasilnya?

→ Login berhasil
atau
→ Login gagal
```

Setelah memahami masalah tersebut, programmer menyusun algoritma, kemudian menerjemahkannya menjadi kode.

Jadi proses berpikir seorang programmer kurang lebih seperti ini:
```text
Masalah
   ↓
Memahami masalah
   ↓
Menganalisis kebutuhan
   ↓
Mencari solusi
   ↓
Menyusun algoritma
   ↓
Menulis program
   ↓
Testing
   ↓
Debugging
   ↓
Program selesai
```

Inilah alasan mengapa kemampuan programming tidak sama dengan kemampuan mengetik kode.

---
# Programmer Bukan Sekadar Penulis Kode

Bayangkan ada dua orang.

Orang pertama sangat hafal JavaScript. Dia tahu berbagai syntax, method array, function, class, asynchronous programming, dan sebagainya.

Tetapi ketika diberikan masalah
> "Buat sistem untuk menghitung total belanja setelah diskon."

Dia bingung harus mulai dari mana.

Orang kedua hanya mengetahui JavaScript dasar, tetapi ketika diberikan masalah tersebut dia mulai berpikir:
```text
Data apa yang dibutuhkan?

→ Harga barang
→ Jumlah barang
→ Persentase diskon

Apa yang harus dihitung?

→ Subtotal
→ Diskon
→ Total akhir

Apa outputnya?

→ Total yang harus dibayar
```

Kemudian dia membuat algoritma.

Walaupun kemampuan syntax orang kedua lebih sedikit, cara berpikirnya lebih dekat dengan kemampuan programming yang sebenarnya.

Karena itu, ketika belajar programming, jangan terlalu terobsesi dengan:
> "Aku harus hafal semua syntax."

Syntax bisa dicari, Dokumentasi bisa dibuka, IDE bisa memberikan autocomplete,
AI bahkan sekarang bisa menghasilkan kode dalam beberapa detik. Dunia memang memutuskan bahwa manusia harus mempunyai masalah baru setelah komputer berhasil membuat kode.

Tetapi kemampuan untuk **memahami masalah dan menentukan solusi** tetap menjadi kemampuan fundamental.

---
# Programmer dan Problem Solving

Salah satu kemampuan paling penting seorang programmer adalah **problem solving**.

Problem solving berarti kemampuan untuk mengambil sebuah masalah yang masih umum atau berantakan, kemudian mengubahnya menjadi masalah yang lebih kecil dan dapat diselesaikan.

Misalnya:
> "Saya ingin membuat website toko online."

Ini masalah yang sangat besar, Programmer tidak langsung membuka VS Code dan membuat:
```text
index.html
```

Kemudian berharap semesta memberikan solusi.

Masalah tersebut perlu dipecah.
```text
E-Commerce
│
├── User
│   ├── Register
│   ├── Login
│   └── Profile
│
├── Product
│   ├── List
│   ├── Detail
│   └── Search
│
├── Cart
│   ├── Add product
│   ├── Remove product
│   └── Update quantity
│
├── Checkout
│   ├── Address
│   ├── Shipping
│   └── Payment
│
└── Order
    ├── History
    └── Status
```

Sekarang masalah yang awalnya:
```text
"buat toko online"
```

telah berubah menjadi sekumpulan masalah yang jauh lebih kecil.
Inilah salah satu kemampuan fundamental programmer.

---
# Programmer Berpikir dalam Bentuk Data dan Proses

Ketika melihat sebuah masalah, programmer biasanya mencoba memahami dua hal utama:

**Data apa yang tersedia?**

dan

**Apa yang harus dilakukan terhadap data tersebut?**

Misalnya sistem perpustakaan.

Data:
```text
Buku
Anggota
Peminjaman
Pengembalian
Tanggal
```

Proses:
```text
Menambahkan buku
Mendaftarkan anggota
Meminjam buku
Mengembalikan buku
Menghitung keterlambatan
Menghitung denda
```

Output:
```text
Daftar buku
Status peminjaman
Informasi anggota
Jumlah denda
```

Kalau kita sederhanakan:
```text
DATA
 ↓
PROCESS
 ↓
RESULT
```

Cara berpikir seperti ini nantinya akan sangat membantu ketika kamu belajar database, backend, API, object-oriented programming, bahkan cybersecurity.

---
# Programmer Harus Bisa Memberikan Instruksi yang Jelas

Komputer sangat literal, Kalau manusia mengatakan:
> "Tolong tampilkan data user."

Manusia lain mungkin bisa memahami maksudnya, Tetapi komputer membutuhkan instruksi yang jauh lebih spesifik.

Misalnya:
```text
Ambil user dengan ID 15
↓
Cari data user pada database
↓
Periksa apakah user ditemukan
↓
Jika ditemukan:
    ambil nama dan email
↓
Jika tidak ditemukan:
    tampilkan error
↓
Kirim hasil dalam format JSON
```

Semakin kompleks programnya, semakin banyak detail yang harus didefinisikan, Ini menjadi salah satu alasan mengapa **algoritma** sangat penting.

Programmer tidak hanya bertanya:
> "Apa yang ingin saya buat?"

Tetapi juga:
> "Langkah tepat apa yang harus dilakukan komputer untuk menghasilkan hal tersebut?"

---
# Programmer Tidak Harus Mengetahui Semua Hal

Ini juga penting untuk dipahami sejak awal.
Programmer bukan manusia yang menghafal semua syntax, semua framework, semua library, semua command Linux, semua API, dan semua error message di dunia.

Itu tidak realistis, Bahkan programmer berpengalaman masih membuka dokumentasi.

Misalnya programmer JavaScript lupa syntax tertentu, Dia bisa membuka dokumentasi.

Programmer PHP lupa fungsi tertentu, Dia mencari dokumentasi.

Programmer menemukan error database, Dia membaca error message dan mencari penyebabnya.

Kemampuan pentingnya bukan:
> "Saya hafal semuanya."

Tetapi:
> **"Saya tahu bagaimana mencari tahu sesuatu yang belum saya ketahui."**

Inilah yang sering disebut sebagai **learning ability** atau kemampuan belajar secara mandiri.

---
# Programmer Harus Bisa Membaca Kode

Menulis kode hanyalah satu sisi programming, Kemampuan membaca kode sama pentingnya.

Misalnya kamu menemukan:
```javascript
const total = products
		.filter(product => product.active)
		.reduce((sum, product) => sum + product.price, 0);
```

Kalau masih belajar dasar, kode tersebut mungkin terlihat seperti bahasa alien.

Tetapi programmer tidak boleh langsung berpikir:
> "Aku tidak mengerti, berarti kodenya jelek."

Programmer harus membongkarnya.
```text
products
   ↓
filter()
   ↓
hanya product.active
   ↓
reduce()
   ↓
jumlahkan price
   ↓
total
```

Dengan begitu kode yang awalnya kompleks bisa dipahami sebagai proses sederhana.
Kemampuan membaca kode akan semakin penting ketika kamu bekerja dengan project orang lain.
Karena dalam dunia kerja, kamu sering kali tidak memulai project dari nol.

Kamu akan mendapatkan:
```text
Repository
↓
Ribuan file
↓
Puluhan ribu baris kode
↓
"Fix bug ini."
```

Dan ya, begitulah manusia menemukan cara baru untuk menghabiskan hari Senin.

---
# Programmer Harus Bisa Melakukan Debugging

Programmer juga harus mampu menemukan kesalahan.

Misalnya kita membuat:
```javascript
const price = 10000;
const quantity = 3;

const total = price + quantity;

console.log(total);
```

Program tersebut mungkin berjalan tanpa error.

Tetapi hasilnya:
```text
10003
```

Padahal seharusnya:
```text
30000
```

Ini menarik karena program **tidak mengalami syntax error** dan Komputer menjalankan instruksinya dengan benar, Masalahnya ada pada **logika programmer**.

Seharusnya:
```javascript
const total = price * quantity;
```

Kesalahan seperti ini disebut **logical error**.

Nanti kita akan membahas berbagai jenis error secara khusus.

Tetapi sejak sekarang pahami bahwa programmer harus memiliki kebiasaan:
```text
Program tidak bekerja
       ↓
Jangan panik
       ↓
Cari tahu apa yang sebenarnya terjadi
       ↓
Periksa input
       ↓
Periksa proses
       ↓
Periksa output
       ↓
Temukan penyebab
       ↓
Perbaiki
```

Debugging bukan aktivitas tambahan, Debugging adalah bagian normal dari programming.

---
# Programmer Tidak Hanya Menulis Program

Dalam project nyata, pekerjaan programmer dapat mencakup:
```text
Memahami requirement
Menganalisis masalah
Mendesain solusi
Menentukan struktur data
Membuat algoritma
Menulis kode
Membaca kode
Testing
Debugging
Refactoring
Menggunakan Git & Github (Untuk Deployment)
Membaca dokumentasi
Melakukan code review
Memelihara aplikasi
```

Semakin tinggi level programmer, semakin banyak aktivitas yang berada **di luar sekadar menulis syntax**.

Programmer junior mungkin lebih banyak fokus pada:
```text
"Bagaimana cara menulis kode ini?"
```

Programmer yang lebih berpengalaman mulai bertanya:
```text
"Bagaimana cara menyelesaikan masalah ini?"
```

Sedangkan programmer yang jauh lebih berpengalaman mulai bertanya:
```text
"Apakah masalah ini sebaiknya diselesaikan dengan cara ini?"
```

Itulah perkembangan cara berpikir yang nantinya akan kamu alami.

---
# Programmer dan Bahasa Pemrograman

Ada kesalahpahaman yang cukup umum
> "Kalau saya programmer PHP, berarti saya harus selalu menggunakan PHP."

Tidak.

PHP adalah **alat**.
JavaScript adalah alat.
Python adalah alat.
Go adalah alat.
Rust adalah alat.

Bahasa pemrograman hanyalah media untuk mengimplementasikan solusi.

Misalnya kita memiliki algoritma:
```text
Ambil dua angka
↓
Jumlahkan
↓
Tampilkan hasil
```

Kita dapat menulisnya menggunakan PHP:
```php
$a = 10;
$b = 20;

$result = $a + $b;

echo $result;
```

JavaScript:
```javascript
const a = 10;
const b = 20;

const result = a + b;

console.log(result);
```

Python
```python
a = 10
b = 20

result = a + b

print(result)
```

Syntax berbeda, Tetapi logikanya sama.

Karena itu ketika kamu nanti belajar banyak bahasa, jangan mempelajarinya sebagai dunia yang benar-benar berbeda.

Coba cari konsep yang sama:
```text
Variable
Condition
Loop
Function
Data Structure
Object
Error Handling
Module
```

Kemudian lihat bagaimana masing-masing bahasa mengimplementasikannya.

---
# Programmer dan Abstraksi

Programmer juga belajar menyederhanakan sesuatu yang kompleks.

Misalnya ketika kamu menggunakan:
```javascript
fetch("/api/users");
```

Kamu tidak perlu memahami setiap detail bagaimana TCP bekerja, bagaimana HTTP packet dikirim, bagaimana DNS mencari server, bagaimana TLS melakukan encryption, dan bagaimana network stack memproses packet setiap kali kamu memanggil `fetch()`.

Semua detail tersebut disembunyikan di balik abstraksi.

Kamu cukup menggunakan:
```javascript
fetch(...)
```

Tetapi sebagai programmer, semakin tinggi levelmu, semakin penting untuk memahami **abstraksi yang berada di bawahnya**.

Misalnya:
```text
React
↓
JavaScript
↓
Runtime
↓
Operating System
↓
Network Stack
↓
TCP/IP
↓
Network Hardware
```

Kamu tidak harus memahami semuanya sekaligus.

Tetapi secara bertahap kamu akan membuka lapisan tersebut.

Ini juga alasan mengapa fundamental programming penting. Kalau fondasinya kuat, kamu lebih mudah turun atau naik antar-level abstraksi.

---
# Programmer sebagai Problem Solver

Kalau seluruh pembahasan ini diringkas, seorang programmer adalah seseorang yang menggunakan komputer dan software sebagai alat untuk **memecahkan masalah**.

Bukan sekadar:
```text
Menulis kode
```

Tetapi:
```text
Problem
   ↓
Understanding
   ↓
Analysis
   ↓
Solution
   ↓
Algorithm
   ↓
Implementation
   ↓
Testing
   ↓
Debugging
   ↓
Maintenance
```

Dan proses tersebut bisa berulang.

Misalnya setelah aplikasi selesai:
```text
Aplikasi
↓
User menemukan bug
↓
Problem baru
↓
Analisis
↓
Solusi
↓
Coding
↓
Testing
↓
Deploy
```

Jadi programming sebenarnya merupakan proses **problem solving yang berulang menggunakan komputer sebagai alat**.

---
# Inti yang Harus Kamu Bawa

Setelah mempelajari materi ini, kamu tidak perlu menghafal definisi panjang.

Yang harus tertanam adalah beberapa konsep inti.

**Programmer bukan sekadar orang yang menulis kode.**

Programmer adalah orang yang memahami masalah, menyusun solusi, kemudian menerjemahkan solusi tersebut menjadi instruksi yang dapat dijalankan komputer.

Programmer menggunakan bahasa pemrograman sebagai **alat**, bukan sebagai tujuan akhir.

Programmer juga harus mampu membaca kode, menganalisis masalah, melakukan debugging, memahami data dan proses, serta mencari informasi ketika menemukan sesuatu yang belum diketahui.

Dan yang paling penting:
> **Programming adalah aktivitas problem solving. Coding adalah salah satu cara untuk mengimplementasikan solusi tersebut.**

Kalau kamu memahami perbedaan ini sejak awal, cara belajarmu nanti akan jauh lebih sehat. Kamu tidak akan terlalu terjebak dalam pola "hafal syntax → lupa syntax → panik → buka Google", melainkan mulai membangun kemampuan berpikir yang bisa dibawa dari PHP ke JavaScript, Python, Go, atau bahasa apa pun.

---