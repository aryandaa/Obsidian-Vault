#programming 
Sebelumnya, kita sudah mempelajari props yang dapat mengirimkan data kepada child component dari parent component. Perlu kami tekankan bahwa props adalah “read-only” data yang immutable alias tidak untuk diubah nilainya.

UI dari sebuah aplikasi bersifat dinamis dan seringkali berubah seiring terjadinya interaksi oleh pengguna. Contoh paling sederhana adalah ketika Anda memberikan rating pada aplikasi toko online. Data rating diharapkan selalu berubah ketika terdapat interaksi dari pengguna. 

Data di dalam komponen yang bertugas untuk menampung perubahan bukanlah props, melainkan state. Di modul ini, Anda akan belajar bagaimana membuat dan mengelola state agar UI yang dihasilkan oleh component dapat bersifat reaktif ketika terjadi perubahan data.

Tujuan dari modul ini adalah sebagai berikut.

Membuat React component menggunakan sintaksis class (class component).
Membuat dan mengelola state di dalam class component.
Menangani sebuah event pada React component.
Memahami Controlled Element dalam membuat form input.
Melengkapi fungsionalitas dari aplikasi “Buku Kontak”.