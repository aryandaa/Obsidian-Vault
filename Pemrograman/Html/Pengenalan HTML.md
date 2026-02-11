#programming 
HTML singkatan dari Hypertext Markup Language. HTML tidak dapat dikatakan sebagai bahasa pemrograman karena tidak ada logika di dalamnya. Ia hanya digunakan untuk menyusun tampilan website supaya sesuai dengan yang dispesifikan dan dapat dibuka dengan browser.

Dalam sebuah website biasanya terdapat index.html yang merupakan tampilan default ketika membuka suatu domain. Sebagai contoh, ketika membuka [http://www.google.com](http://www.google.com/), sejatinya Anda masuk ke halaman [http://www.google.com/index.html](http://www.google.com/index.html).

Fungsi utama HTML adalah membuat suatu halaman website menjadi lebih mudah dibaca dan dipahami. Oleh karena itu, di sana terdapat berbagai macam tag yang bisa digunakan untuk memformat teks, seperti heading, paragraf, maupun link.

### Cara Membuat HTML

Untuk membuat sebuah file HTML sangatlah mudah, Anda hanya perlu membuat berkas dengan ekstensi **.html** menggunakan Visual Studio Code atau bahkan Notepad. Setelah membuat berkasnya, Anda dapat langsung membukanya menggunakan browser seperti Chrome, Firefox, Safari, dan lain sebagainya. Bahkan berkas tersebut bisa dibuka tanpa menggunakan server atau akses internet, cukup di lokal saja. Menarik, bukan?  
  
Selain membuat file sendiri, Anda juga dapat menggunakan online compiler seperti pada [HTML Online Editor](https://html-online.com/editor/).

Selanjutnya untuk melakukan formatting, kita perlu memahami penggunaan tag dalam HTML. Format penulisan tag-nya seperti berikut:
`<tagname>Teks yang ingin diformat</tagname>`

Terdapat dua tag untuk memformat suatu teks, yaitu tag pembuka `<tagname>` dan tag penutup `</tagname>`.


Selain melakukan formatting, Anda juga bisa mengatur format dalam suatu dokumen dengan struktur yang lebih lengkap seperti berikut:
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Ini merupakan judul dari dokumen HTML</title>
    </head>
    <body>
        <h1>Header Halaman</h1>
        <p>Ini merupakan contoh sebuah paragraf yang juga diletakan pada sebuah konten body, sehingga konten ini dapat dilihat oleh pengguna pada jendela browser.</p>
        <p>Contoh paragraf lain. Lihat Selengkapnya di <a href="https://www.dicoding.com/"> dicoding.com</a></p>
    </body>
</html>
```

-<html> :Tag paling dasar pada HTML, semua elemen lain harus di dalam tag ini.
-<head> : Tempat untuk menyimpan informasi dari dokumen HTML.
-<title> : Judul yang muncul di tab browser.
-<body> : Representasi dari suatu konten pada sebuah dokumen HTML.
-<h1> : Salah satu jenis dari 6 jenis heading yang paling tinggi.
-<a diikuti attribute href> : Untuk membuat hyperlink ke suatu website.
-<p> : Digunakan untuk membuat paragraf baru.

