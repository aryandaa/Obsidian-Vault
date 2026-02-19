#programming 
Pada HTML untuk menampilkan sebuah gambar kita bisa menggunakan tag `<img>`. Berbeda dengan elemen lain, elemen `<img>` tidak menuliskan konten di antara tag pembuka dan tag penutup. Namun, untuk menetapkan gambar yang ditampilkan kita gunakan sebuah atribut.

cara penggunaannya seperti ini:
```html
<img
  src="https://raw.githubusercontent.com/dicodingacademy/a123-webdasar-labs/099-shared-files/shared-media/dicoding-logo.jpg" 
  alt="Dicoding Logo"
>
```
Pada contoh kode di atas, perlu kita perhatikan bahwa elemen <img> merupakan sebuah elemen kosong (tidak memiliki konten sehingga tidak ada _closing tag_). 

Selain itu, hal yang perlu kita perhatikan adalah atribut pada elemen tersebut, terdapat dua **attributes** yang harus kita gunakan ketika menerapkan elemen <img>.

Pertama, atribut _src_. Atribut ini berfungsi sebagai sumber dari gambar yang ditampilkan. Atribut ini dapat bernilai url gambar atau path gambar local dari gambar yang digunakan.

Kedua adalah atribut _alt_. Atribut ini sebenarnya tidak wajib untuk diterapkan, hanya saja atribut ini akan sangat berguna ketika gambar tidak berhasil ditampilkan. Nilai atribut ini merupakan tampilan dari gambar yang ditampilkan dalam bentuk tulisan. Jadi, ketika gambar gagal ditampilkan akan memunculkan teks alternatif yang dapat mewakili arti dari gambar tersebut.

selain src dan alt, ada pula beberapa atribut ini sebagai pendukung untuk gambarnya yaitu
width=""
height=""
untuk mengatur ukuran gambarnya.