#programming 

Sebelum belajar `if`, `for`, `function`, class, framework, atau segala macam ritual pemanggilan API yang nanti akan membuat hidup kita lebih menarik, kita perlu memahami satu hal paling dasar terlebih dahulu: **apa sebenarnya yang dimaksud dengan program?**

Banyak orang ketika mendengar kata _program_ langsung membayangkan kode seperti ini:
```php
<?php

$name = "Yanda";

echo "Hello " . $name;
```

Padahal kode tersebut hanyalah **cara manusia menuliskan sebuah program**. Programnya sendiri bukan sekadar kumpulan tulisan seperti `echo`, `$name`, atau tanda `{}`. Di balik kode tersebut terdapat sebuah **instruksi yang memberitahu komputer apa yang harus dilakukan**.

Jadi, definisi paling sederhananya adalah:

> **Program adalah sekumpulan instruksi yang disusun untuk memberi tahu komputer bagaimana melakukan suatu pekerjaan atau menyelesaikan suatu masalah.**

Kata kuncinya adalah **instruksi**.

Komputer pada dasarnya tidak memiliki kemampuan untuk menebak apa yang kita inginkan. Kalau kita mengatakan kepada manusia, "hitung total harga barang", manusia mungkin langsung memahami maksudnya. Komputer tidak demikian. Kita harus menjelaskan prosesnya dengan cukup jelas sehingga komputer dapat menjalankannya.

Misalnya kita ingin membuat program sederhana untuk menghitung total harga.

Kita memiliki harga barang sebesar Rp10.000 dan jumlah barang sebanyak 3. Secara manusia kita bisa langsung berpikir:

```text
10.000 × 3 = 30.000
```

Tetapi komputer membutuhkan instruksi:

```text
1. Ambil harga barang.
2. Ambil jumlah barang.
3. Kalikan harga dengan jumlah.
4. Simpan hasilnya.
5. Tampilkan hasilnya.
```

Nah, rangkaian langkah tersebut sudah merupakan bentuk sederhana dari sebuah **program**.

Bahasa pemrograman seperti PHP, JavaScript, Python, Java, C++, dan sebagainya hanyalah alat yang digunakan untuk menerjemahkan instruksi tersebut ke dalam bentuk yang dapat dipahami oleh komputer.

---
## Program adalah Instruksi, Bukan Sekadar Kode

Ini adalah konsep yang penting untuk ditanamkan sejak awal, Ketika kamu melihat kode:

```javascript
const price = 10000;
const quantity = 3;

const total = price * quantity;

console.log(total);
```

jangan hanya melihatnya sebagai beberapa baris syntax JavaScript.

Cobalah membacanya sebagai instruksi:

```text
Simpan angka 10000 sebagai harga.

Simpan angka 3 sebagai jumlah.

Kalikan harga dengan jumlah.

Simpan hasil perkalian sebagai total.

Tampilkan total.
```

Dengan cara berpikir seperti ini, kamu mulai melihat **logika program**, bukan sekadar syntax, Ini nantinya sangat berguna ketika kamu berpindah bahasa.

Misalnya dalam Python:
```python
price = 10000
quantity = 3

total = price * quantity

print(total)
```

Secara syntax memang berbeda.

JavaScript menggunakan:
```javascript
console.log(total);
```

Python menggunakan:
```python
print(total)
```

Tetapi programnya sama.

Keduanya melakukan:
```text
harga → jumlah → perkalian → total → tampilkan
```

Jadi sebenarnya yang kamu pelajari bukanlah `console.log()` atau `print()`. Kamu sedang mempelajari **cara menyelesaikan masalah menggunakan instruksi yang bisa dijalankan komputer**.

---
# Program dan Masalah

Program hampir selalu dibuat karena ada **masalah yang ingin diselesaikan**.
Misalnya sebuah toko ingin menghitung total belanja pelanggan secara otomatis.

Tanpa program, pegawai mungkin harus melakukan:
```text
Harga barang 1
+ Harga barang 2
+ Harga barang 3
+ ...
= Total
```

Kalau hanya dua atau tiga barang, tidak masalah, Tetapi bayangkan ada 500 transaksi setiap hari, Kemudian ditambahkan diskon, pajak, ongkos kirim, metode pembayaran, laporan penjualan, dan sebagainya, Manusia mulai lelah.

Program kemudian dibuat untuk mengotomatisasi pekerjaan tersebut.

Misalnya:
```text
Input
↓
Data barang
↓
Hitung subtotal
↓
Hitung diskon
↓
Hitung pajak
↓
Hitung total
↓
Output
```

Itulah salah satu alasan utama program dibuat: **mengubah proses manual menjadi proses yang dapat dilakukan komputer secara otomatis.**

---
# Program sebagai Solusi

Ada konsep lain yang harus kamu pahami: **Program bukan tujuan akhir. Program adalah alat untuk menghasilkan solusi.**

Misalnya seseorang berkata:
> "Saya ingin membuat program untuk menghitung nilai mahasiswa."

Sebenarnya itu belum menjelaskan masalah dengan cukup jelas.

Kita harus memahami:
```text
Apa inputnya?
Apa yang harus dilakukan?
Apa outputnya?
```

Misalnya:
```text
Input:
Nilai tugas
Nilai UTS
Nilai UAS

Process:
Hitung nilai akhir

Output:
Nilai akhir mahasiswa
```

Kemudian kita bisa membuat aturan:
```text
Nilai akhir =
30% tugas +
30% UTS +
40% UAS
```

Barulah kita bisa menerjemahkannya menjadi program.

Misalnya:
```javascript
const tugas = 80;
const uts = 75;
const uas = 90;

const nilaiAkhir =
    (tugas * 0.3) +
    (uts * 0.3) +
    (uas * 0.4);

console.log(nilaiAkhir);
```

Perhatikan alurnya:
```text
Masalah
   ↓
Pahami masalah
   ↓
Tentukan solusi
   ↓
Susun langkah
   ↓
Tuliskan instruksi
   ↓
Program
   ↓
Komputer menjalankan
   ↓
Hasil
```

Inilah pola yang nantinya akan terus kamu gunakan dalam programming.

---
# Program Memiliki Input, Process, dan Output

Salah satu konsep paling fundamental dalam pemrograman adalah:

**Input → Process → Output**

Konsep ini sangat sederhana, tetapi hampir semua program bisa dijelaskan menggunakan pola tersebut.

Misalnya program kalkulator.

Input:
```text
Angka pertama = 10
Angka kedua = 5
Operator = +
```

Process:
```text
10 + 5
```

Output:
```text
15
```

Secara sederhana:
```text
       INPUT
         ↓
   ┌─────────────┐
   │   PROCESS   │
   └─────────────┘
         ↓
       OUTPUT
```

Contoh lain adalah login.

Input:
```text
Username
Password
```

Process:
```text
Cari username
↓
Periksa password
↓
Apakah cocok?
```

Output:
```text
Login berhasil
```

atau:
```text
Username atau password salah
```

Program yang lebih kompleks tetap bisa dilihat dengan pola yang sama, hanya saja prosesnya jauh lebih panjang.

Misalnya aplikasi e-commerce:
```text
INPUT
↓
User memilih produk
↓
PROCESS
↓
Hitung harga
↓
Hitung diskon
↓
Hitung pajak
↓
Hitung ongkir
↓
Validasi pembayaran
↓
Simpan transaksi
↓
OUTPUT
↓
Pesanan berhasil dibuat
```

Jadi ketika nanti kamu melihat aplikasi yang sangat kompleks, jangan langsung menganggapnya sebagai sesuatu yang ajaib.

Di balik kompleksitas tersebut tetap ada proses input, pengolahan data, dan output.

---
# Program Tidak Selalu Memiliki Input dari User

Ini juga perlu diluruskan, Input bukan berarti **harus ada orang mengetik sesuatu**, 
Input berarti **data yang digunakan oleh program untuk melakukan proses**.

Contohnya aplikasi cuaca.

User tidak harus mengetik suhu secara manual. Aplikasi bisa mendapatkan data dari API.
```text
API Weather
    ↓
Data suhu
    ↓
Program
    ↓
Pengolahan
    ↓
Tampilan cuaca
```

Dalam kasus tersebut, input program berasal dari API.

Contoh lainnya database:
```text
Database
    ↓
Data user
    ↓
Program
    ↓
Process
    ↓
Halaman profile
```

Jadi sumber input bisa bermacam-macam:
```text
User
File
Database
API
Sensor
Network
Environment
Program lain
```

Ini akan menjadi sangat penting ketika nanti kamu belajar backend, networking, cybersecurity, dan sistem terdistribusi.

---
# Program Bekerja Berdasarkan Instruksi

Komputer tidak menjalankan program berdasarkan "niat" programmer, Komputer menjalankan instruksi yang diberikan.

Misalnya kita membuat program:
```javascript
let x = 10;
let y = 20;

let result = x + y;

console.log(result);
```

Secara konsep komputer melakukan sesuatu seperti:
```text
Simpan 10
Simpan 20
Ambil 10
Ambil 20
Lakukan operasi penjumlahan
Simpan hasil
Tampilkan hasil
```

Programmer kemudian menggunakan bahasa pemrograman untuk menuliskan instruksi tersebut dalam bentuk yang lebih mudah dibuat dan dipahami manusia.

---
# Bahasa Pemrograman

Komputer sebenarnya bekerja pada level yang jauh lebih rendah daripada PHP, JavaScript, atau Python.

Pada level mesin, komputer pada akhirnya bekerja dengan instruksi yang direpresentasikan menggunakan bit:
```text
0
1
```

Manusia tentu tidak ingin menulis aplikasi menggunakan deretan `0` dan `1`.

Bayangkan harus membuat aplikasi login seperti:
```text
01001000 01100101 01101100 ...
```

Belum selesai satu halaman, programmer sudah berubah menjadi legenda urban.

Karena itu manusia membuat berbagai **bahasa pemrograman**.

Contohnya:
```text
Python
JavaScript
PHP
Java
C
C++
C#
Go
Rust
Kotlin
Swift
```

Bahasa-bahasa tersebut memberikan cara yang lebih mudah bagi manusia untuk menulis instruksi.

Misalnya:
```python
print("Hello World")
```

Lebih mudah dipahami manusia daripada instruksi mesin. Kemudian bahasa pemrograman tersebut diproses oleh compiler, interpreter, atau mekanisme runtime tertentu sehingga dapat dijalankan oleh komputer.

Untuk saat ini kamu tidak perlu terlalu dalam mempelajari compiler dan interpreter. Itu akan kita bahas nanti pada bagian **Cara Kerja Program**.

Yang penting sekarang pahami hubungan ini:
```text
Manusia
   ↓
Bahasa Pemrograman
   ↓
Program
   ↓
Compiler / Interpreter / Runtime
   ↓
Instruksi Mesin
   ↓
CPU
   ↓
Hasil
   ↓
Manusia
```

---
# Program dan Algorithm

Program juga sangat erat hubungannya dengan **algoritma**, Algoritma adalah langkah-langkah logis untuk menyelesaikan suatu masalah.

Program adalah implementasi dari langkah-langkah tersebut dalam bentuk yang dapat dijalankan komputer.

Misalnya masalahnya:
> Menghitung luas persegi panjang.

Algoritmanya:
```text
1. Ambil panjang.
2. Ambil lebar.
3. Kalikan panjang dengan lebar.
4. Tampilkan hasil.
```

Programnya:
```javascript
const panjang = 10;
const lebar = 5;

const luas = panjang * lebar;

console.log(luas);
```

Jadi:
```text
Algorithm
    ↓
"Bagaimana cara menyelesaikan masalah?"
    ↓
Program
    ↓
"Bagaimana cara menuliskan solusi tersebut agar komputer bisa menjalankannya?"
```

Ini merupakan perbedaan yang sangat penting.

Kamu tidak ingin menjadi programmer yang hanya bisa menulis:
```javascript
if (...)
```

tetapi ketika diberi masalah tidak tahu harus melakukan apa. sebagai Programmer yang baik biasanya berpikir:
```text
Masalahnya apa?
↓
Data apa yang tersedia?
↓
Output yang diinginkan apa?
↓
Aturannya apa?
↓
Langkah penyelesaiannya bagaimana?
↓
Baru tulis kode.
```

---
# Program Sederhana dalam Kehidupan Sehari-hari

Supaya konsepnya benar-benar masuk, kita bisa melihat aktivitas sehari-hari sebagai program.

Misalnya membuat kopi.

Input:
```text
Air
Kopi
Gula
Gelas
```

Process:
```text
1. Panaskan air.
2. Masukkan kopi.
3. Masukkan gula.
4. Tuangkan air.
5. Aduk. 
```

Output:
```text
Kopi siap diminum.
```

Secara sederhana:
```text
INPUT
Air + Kopi + Gula
       ↓
PROCESS
Langkah pembuatan
       ↓
OUTPUT
Kopi
```

Tentu manusia memiliki kemampuan untuk menyesuaikan proses berdasarkan situasi.

Komputer tidak sefleksibel itu kecuali kita memang memberikan aturan untuk menangani kondisi tersebut.

Misalnya:
```text
Jika gula habis:
    jangan masukkan gula

Jika air belum panas:
    panaskan air

Jika kopi habis:
    tampilkan "kopi tidak tersedia"
```

Sekarang kita sudah mulai masuk ke konsep **conditional logic**.

Nanti ini berkembang menjadi:
```javascript
if (...)
```

dan kemudian menjadi struktur program yang jauh lebih kompleks.

---
# Program yang Baik

Program yang bisa dijalankan belum tentu merupakan program yang baik.

Misalnya kita ingin menghitung luas persegi panjang.

Kita bisa membuat kode yang sangat berantakan:
```javascript
let a = 10;
let b = 20;
let c = a * b;
console.log(c);
```

Program ini benar.

Tetapi orang lain mungkin tidak langsung tahu bahwa `a` adalah panjang dan `b` adalah lebar.

Kita bisa membuatnya lebih jelas:
```javascript
const panjang = 10;
const lebar = 20;

const luas = panjang * lebar;

console.log(luas);
```

Hasilnya sama, Tetapi program kedua lebih mudah dipahami.

Ini memperkenalkan sebuah konsep penting:
> **Program tidak hanya harus benar untuk komputer, tetapi juga harus mudah dipahami manusia.**

Karena dalam dunia nyata, program akan dibaca, diperbaiki, dikembangkan, dan diwariskan kepada programmer lain.

Bahkan sering kali programmer yang menulis kode enam bulan lalu adalah dirinya sendiri, Dan enam bulan kemudian dia akan melihat:
```javascript
let x = ...
let y = ...
let z = ...
```

lalu bertanya:
> "Siapa manusia yang membuat kekacauan ini?"

Ternyata dirinya sendiri.

---
# Program Bukan Hanya Aplikasi

Istilah "program" sering dianggap sama dengan aplikasi, Sebenarnya lebih luas.

Aplikasi seperti:
```text
WhatsApp
Browser
Game
VS Code
Photoshop
```

semuanya menggunakan program, Tetapi program juga bisa berupa sesuatu yang sangat sederhana.

Contohnya:
```javascript
console.log("Hello");
```
Itu adalah program sederhana.

Script untuk memindahkan file:
```text
Program
```

Script untuk melakukan backup database:
```text
Program
```

Script untuk melakukan scanning keamanan:
```text
Program
```

Backend API:
```text
Program
```

Operating system:
```text
kumpulan program
```

Bahkan sistem yang sangat kompleks pada akhirnya tersusun dari banyak program dan komponen software yang bekerja bersama.

---
# Program, Software, dan Application

Ketiga istilah ini sering digunakan secara bergantian, padahal ada perbedaan konteks.

**Program** adalah sekumpulan instruksi yang dapat dijalankan komputer.

**Software** adalah istilah yang lebih luas untuk perangkat lunak, termasuk program, library, konfigurasi, dan komponen lain yang membentuk suatu sistem perangkat lunak.

**Application** biasanya merujuk pada software yang dibuat untuk melakukan kebutuhan tertentu bagi pengguna.

Contohnya:

```text
Software
└── Web Browser
    ├── Program
    ├── Library
    ├── Configuration
    └── Resource
```

Untuk tahap fundamental, tidak perlu terlalu memikirkan perbedaan terminologi ini secara kaku. Yang penting kamu memahami bahwa **program adalah sekumpulan instruksi yang membuat komputer melakukan sesuatu**.

---
# Kesimpulan Bab

Sampai titik ini, konsep paling penting yang harus kamu pegang adalah:
> **Program adalah sekumpulan instruksi yang dibuat untuk menyelesaikan suatu masalah atau melakukan suatu pekerjaan menggunakan komputer.**

Program tidak dimulai dari syntax, Program dimulai dari **masalah**.

Urutannya secara konseptual adalah:
```text
MASALAH
   ↓
Pahami masalah
   ↓
Tentukan solusi
   ↓
Susun algoritma
   ↓
Terjemahkan ke bahasa pemrograman
   ↓
Program
   ↓
Komputer menjalankan
   ↓
HASIL
```

Dan hampir setiap program dapat kita lihat melalui pola:
```text
INPUT
  ↓
PROCESS
  ↓
OUTPUT
```

Hal yang paling penting dari bab ini bukan menghafal definisi "program". Kalau kamu hanya menghafalnya, besok kemungkinan besar otak manusia akan melakukan pekerjaan favoritnya: membuang informasi yang dianggap tidak mendesak.

Yang perlu kamu pahami adalah **cara melihat sebuah program**.

Ketika melihat kode, jangan hanya bertanya:
> "Syntax ini artinya apa?"

Biasakan juga bertanya:
> "Program ini sedang menyelesaikan masalah apa?"

> "Data apa yang masuk?"

> "Apa yang dilakukan terhadap data tersebut?"

> "Apa hasil akhirnya?"

Kalau kamu mulai berpikir seperti itu, kamu sudah mulai berpindah dari **belajar syntax** menuju **belajar programming**.