#programming #webdev
Berkomunikasi dengan komputer tidak dapat menggunakan bahasa manusia, melainkan menggunakan bahasa pemrograman. Instruksi yang kita berikan akan diproses oleh CPU _(Central Processing Unit)_ yang ada pada komputer. Lalu, bagaimana kode yang kita buat bisa dipahami oleh komputer?

Ketika seorang pengembang software menulis dan menjalankan sebuah kode, maka terjadilah proses konversi. Proses tersebut dibedakan menjadi dua yaitu **Compile** dan **Interpret**.
![](Pemrograman/Rancangan%20Software/image/2.png)

Bayangkan Anda membuat sebuah aplikasi sederhana di komputer milik Anda sendiri. Kemudian Anda juga ingin menjalankan aplikasi tersebut di komputer teman Anda. Metode pertama kita menggunakan compile.
![](Pemrograman/Rancangan%20Software/image/3.png)

Jika membahas tentang metode compile, kita akan berteman dengan _compiler_. Compiler merupakan sebuah aplikasi yang bertugas untuk mengonversi source code yang kita buat menjadi bahasa mesin. Apabila terdapat penulisan kode yang salah, maka compiler akan mengirimkan pesan eror kepada kita dan harus diperbaiki. Jika tidak, maka akan menghasilkan berkas executable, contohnya seperti .exe. 

Setelah proses compile di komputer Anda selesai, berikanlah berkas .exe tersebut kepada teman Anda. Lalu, apa yang terjadi? Aplikasi dapat dijalankan di komputer teman Anda, tetapi ia tidak mengetahui source code atau bahasa pemrograman apa yang digunakan. Sehingga, source code-nya masih berada di komputer Anda.
![](Pemrograman/Rancangan%20Software/image/4.png)

Metode interpret sama dengan compile yaitu mengonversi bahasa pemrograman supaya bisa dipahami oleh mesin dengan bantuan interpreter. Perbedaannya adalah ketika kita menggunakan compiler, source code akan dikonversi menjadi machine code (membuat berkas executable) sebelum aplikasi tersebut dijalankan. Sedangkan interpreter mengonversi source code menjadi machine code secara langsung ketika aplikasi dijalankan.

Salah satu bahasa pemrograman yang dapat diinterpretasikan adalah JavaScript. Bayangkan Anda membuat aplikasi sederhana menggunakan JavaScript. Kemudian bagikan source code tersebut ke teman Anda. Untuk menjalankan JavaScript tersebut, teman Anda bisa menggunakan web browser. Web browser terdapat interpreter di dalamnya sehingga berkas JavaScript tersebut bisa diinterpretasikan secara langsung.

berikut adalah perbedaan antara Compiler dan Interpret

|Kategori|Compiler|Interpreter|
|---|---|---|
|Penggunaan|- Source code telah dikonversi menjadi machine code.<br>- Waktu eksekusi program lebih singkat.|- Lebih mudah digunakan untuk pemula yang baru belajar.|
|Hasil keluaran|Menghasilkan aplikasi atau program luaran berupa berkas executable (.exe)|Tidak menghasilkan aplikasi atau program luaran berupa berkas executable.|
|Efektifitas|Hasil kompilasi dari source code akan berjalan lebih cepat.|Berjalan lebih lambat ketika dieksekusi.|
|Platform|Spesifik ke platform tertentu (misal .exe tidak dapat dibuka di Mac)|Cross platform (asalkan memiliki interpreter yang sesuai)|
|Alur pembacaan|- Compiler menampilkan pesan eror ketika terjadi kesalahan kode.<br>- Program tidak berjalan atau tidak menghasilkan berkas executable apabila kesalahan kodenya belum diperbaiki.<br>- Misal ada kode yang salah di baris ke-5, maka harus diperbaiki dulu.|- Membaca satu per satu baris kode yang ada. <br>- Jika terdapat kode yang salah, interpreter menampilkan pesan eror dan harus diperbaiki untuk melanjutkan eksekusi baris selanjutnya.<br>- Misalnya terdapat eror di baris ke-5, program masih bisa berjalan karena baris pertama sampai keempat tidak ada eror.|
|Bahasa Pemrograman|C, C++, C#, Swift, Java|JavaScript, Python, PHP, Ruby.|

### Konsep Jalannya Program secara Sekuensial
Apakah Anda pernah memikirkan bagaimana suatu program dieksekusi? Misalnya ketika Anda mengunjungi suatu website dan mencoba melakukan proses login. Ketika Anda memasukkan informasi email dan password serta menekan tombol login, apa saja yang sebenarnya terjadi di sana? Mari kita bahas bagaimana suatu program mengeksekusi perintah-perintahnya.

Suatu program pada dasarnya adalah kumpulan instruksi yang memiliki tujuan tertentu. Kumpulan instruksi tersebut perlu kita susun secara berurutan agar berjalan dengan semestinya. Penyusunan instruksi tersebut adalah tugas seorang pengembang software.

Kenapa harus secara berurutan? Karena ketika suatu program dieksekusi, sistem akan membaca kumpulan instruksinya dari atas ke bawah satu per satu. Sehingga, ketika ada instruksi yang posisinya tidak pas, program menjadi eror.

Konsep berurutan ini ada banyak contohnya di kehidupan nyata, contohnya ketika mengendarai mobil. Untuk mengendarai mobil, seorang supir perlu mengetahui instruksi-instruksi tertentu untuk membuat mobil melaju normal. Sederhananya, proses mengendarai mobil dimulai dari memasukkan kunci terlebih dahulu, hidupkan mesin mobilnya dengan kunci tersebut, menaikkan giginya menjadi 1, lalu injak gasnya hingga mobil mulai melaju.

Instruksi dalam menjalankan mobil memang sudah didesain sedemikian rupa agar mobil dapat melaju dengan aman tanpa terjadi kesalahan-kesalahan yang berakibat fatal. Coba bayangkan jika ada mobil yang bisa melaju dengan menginjak gasnya saja tanpa harus memasukkan kunci, tentu bisa memiliki potensi yang berbahaya bagi orang yang tidak berhati-hati.

Kembali lagi ke pembahasan inti, bagaimana website melakukan proses login? Yang bisa menjawab ini tentunya adalah si pembuat program login-nya, yaitu pengembang software. 

Pada praktiknya seorang pengembang software harus tahu instruksi-instruksi untuk melakukan login yang baik dan benar. Biasanya proses login dimulai dari pengecekan apakah kolom email dan password sudah diisi, kemudian pengecekan apakah emailnya sudah valid. Jika kedua data sudah ada, barulah proses request ke server dilakukan dengan mengirimkan informasi email dan password. Lalu, tunggu balasan dari server apakah loginnya berhasil atau tidak.

Bergantung dari program yang kita buat, jumlah instruksi yang harus kita tulis tentunya akan semakin banyak sesuai dengan kompleksitas programnya. Oleh karena itu pastikan sebelum mulai membuat program, pecah instruksi-instruksi menjadi bagian-bagian kecil dan susun instruksi tersebut sesuai alur yang tepat. Dengan demikian Anda dapat mulai membuat program dengan lebih mudah dan terhindar dari kemungkinan eror.