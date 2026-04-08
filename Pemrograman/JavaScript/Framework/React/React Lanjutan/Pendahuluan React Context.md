#programming 
Dalam pengembangan aplikasi interaktif, kita harus bisa menjaga sinkronisasi antara perubahan data dengan UI. Untunglah, proses sinkronisasi menggunakan React terasa lebih mudah karena memanfaatkan state. Anda sudah tahu bahwa di React, untuk mengirimkan data dari komponen yang berada di level atas ke bawah, praktiknya dapat menggunakan teknik _props drilling_ yang dilakukan secara searah (dari parent ke child).

Props drilling merupakan praktik alami pada React karena sifat _unidirectional data flow_ yang dimilikinya. Namun, seiring kompleksnya hierarki aplikasi, tak jarang praktik ini menjadi momok yang menakutkan. Adakah cara efektif untuk berbagi data “global” ketika menggunakan React? Ada!  
  
Di modul ini, kita akan membahas React Context yang merupakan salah satu fitur untuk memudahkan Anda dalam mengelola state atau data ketika menggunakan React. Berikut adalah poin pembahasannya.

- Mengenal dan mengetahui fungsi dari React Context.
- Mengenal dan mengetahui fungsi  komponen Provider serta Consumer yang terdapat di dalam React Context.
- Mencoba React Context dengan membangun fitur mode gelap menggunakan React.
- Mengimplementasikan React Context pada proyek studi kasus aplikasi kontak.