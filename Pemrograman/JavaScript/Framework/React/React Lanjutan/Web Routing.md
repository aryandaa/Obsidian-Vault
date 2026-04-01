#programming 
Kebanyakan dari aplikasi web yang ada saat ini memiliki lebih dari satu halaman. Setiap halaman website biasanya diakses dengan URL yang berbeda. Melalui URL, kita bisa lebih mudah untuk membagikan halaman secara spesifik ke pengguna. Sebagai web developer, apakah Anda tahu bagaimana cara kerja website ketika menampilkan halaman yang berbeda?

Sejatinya website bekerja dengan pola seperti ini.
![](Pemrograman/JavaScript/Framework/React/React%20Lanjutan/img/4.png)

1. Ketika pengguna mengunjungi website dengan URL http://www.dicoding.com/, browser akan membuat _request_ ke server Dicoding.
2. Kemudian server Dicoding merespons dengan menghasilkan berkas HTML yang digunakan untuk menampilkan halaman / (index).
3. Lalu, bila pengguna berpindah halaman contoh _/about_, browser akan kembali membuat request ke server Dicoding dengan URL http://www.dicoding.com/about.
4. Server Dicoding akan merespons dengan berkas HTML baru yang digunakan untuk menampilkan halaman _/about_.

Setiap kali pengguna berpindah halaman, siklus tersebut akan terus berulang. Yang jelas, browser akan terus berkomunikasi dengan server untuk meminta berkas HTML dalam menampilkan halaman baru. Inilah cara alami bagaimana browser dapat menampilkan halaman yang berbeda.

Ketika menggunakan JavaScript di browser dalam membuat dan menampilkan antarmuka pengguna, banyak yang mengatakan bahwa kita membuat Single-Page Application (SPA). Hal tersebut memang benar. Namun, membangun SPA bukan berarti hanya bisa menampilkan satu halaman saja.

Single-Page Application memiliki mekanisme yang berbeda dalam menampilkan dan menavigasi halaman. Ia tidak perlu berkomunikasi dengan server terus menerus untuk menampilkan halaman yang berbeda, melainkan Single-Page Application akan mengunduh seluruh konten website sekaligus dan menampilkannya berdasarkan permintaan pengguna dengan kontrol JavaScript. Maka dari itu, di SPA setiap kali berpindah halaman, browser tidak perlu memuat ulang (_reload_). Hal ini akan menghasilkan pengalaman yang sama ketika kita menggunakan aplikasi native.

**Catatan:** Meskipun SPA mengunduh seluruh konten website sekaligus, tetapi biasanya konten yang diunduh hanya konten statis yang esensial dalam menampilkan UI. Untuk konten yang bersifat dinamis, biasanya diunduh secara _asynchronous_ dengan metode AJAX. Dengan begitu, tidak ada masalah performa yang signifikan.