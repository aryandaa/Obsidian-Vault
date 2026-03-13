#programming 
Kita telah mempelajari **Browser Object Model**_,_ **Document Object Model**, penggunaan **BOM** untuk membangkitkan fungsionalitas khusus dari _browser_, dan cara menggunakan **DOM** untuk memanipulasi atau mengubah konten dari sebuah berkas HTML.

Lalu, bagaimana JavaScript menjalankan serangkaian perintah jika _user_ berinteraksi dengan salah satu elemen HTML pada halaman _web_? Misalnya, menampilkan pesan menggunakan method `alert()` ketika _user_ menekan sebuah tombol pada halaman _web_ atau mengubah tampilan halaman _web_ jika user menekan sebuah _key_ khusus pada _keyboard?_

Solusinya terdapat pada materi ini, mari berkenalan dengan _event!_

Ketika browser selesai menampilkan halaman _web,_ menekan tombol tertentu pada keyboard, atau mungkin meletakkan kursor pada elemen HTML tertentu, itulah yang dinamakan _event_ alias “kejadian”. Hampir apa pun yang berhubungan dengan adanya interaksi dengan berkas HTML bisa kita sebut sebagai _event_. Lalu, apa fungsinya?

Melalui JavaScript, kita bisa menulis kode tertentu yang akan dijalankan ketika merasakan sebuah “kejadian” tertentu. Contohnya jika user menekan sebuah tombol, JavaScript (melalui DOM) akan mengubah tampilan halaman web kita seperti mengubah warna pada elemen tertentu, atau bahkan membawa kita ke bagian tertentu pada halaman web tersebut. Sebagai contoh, ketika elemen button ini ditekan, akan memunculkan _dialog box_ dengan pesan "Halo! Apa Kabar".
```html
<button onClick="alert('Halo! Apa Kabar')">
  Tekan Aku
</button>
```

Keren, bukan?

Untuk materi Event, kita akan membahas mengenai hal-hal berikut.

- Macam-macam Event.
- Membuat kode JavaScript untuk menjalankan kode berdasarkan _event_ tertentu.
- Memberikan kemampuan sebuah elemen HTML untuk membuat sebuah event.
- Memberikan kemampuan sebuah elemen HTML untuk bereaksi terhadap event_._
- Membuat _Custom Event_, yakni event yang sudah dimodifikasi sesuai dengan keperluan kita.

Ketika sudah memahami bagaimana cara menggunakan event dan mengimplementasikannya bersama dengan manipulasi melalui **DOM** dan **BOM**, maka dijamin halaman web Anda sangat interaktif dan tidak terkesan “hambar”. 

