#programming 
Ketika membuat berkas html, tentu kita sudah tidak asing dengan _tag_ html, bukan? Contohnya, seperti _tag_ **`<html>`**, **`<style>`**, **`<p>`**, **`<div>`**, beserta _tag-tag_ lainnya. Nah, jika kita sudah familier dengan gaya penulisan tag dalam sebuah berkas html, menambahkan kode JavaScript ke dalam berkas HTML akan lebih mudah. Mengapa demikian? Karena kita hanya perlu menggunakan tag  sebagai penutup.

Ada dua cara untuk memasukkan kode JavaScript ke dalam berkas HTML kita, yakni secara **internal** dan **external**. _Hmm_, tampaknya terdengar familier? Betul! Hal ini mirip dengan cara menyematkan berkas CSS ke dokumen HTML, bukan? 

Andaikan kita ingin meminta input dari user pada sebuah _box_ yang muncul. Input tersebut berisi nama dari _user_ dan akan kita munculkan kembali nama dari _user_ tersebut pada sebuah _box_. Berikut adalah bentuknya dalam kode JavaScript:

javascript:
```js
const tamu = prompt('Siapakah Anda?');
alert('Selamat datang ' + tamu + '!');
```

HTML:
```html
<!DOCTYPE html>
<html>
  <body>
    <h2 id="pesan">Selamat datang!</h2>
  </body>
</html>
```

Nah, dari kedua kode program di atas, selanjutnya kita mempelajari cara memasukkan kode JavaScript ke dalam berkas HTML. Bagaimana caranya? Perhatikan pembahasan di bawah ini.

### Internal JavaScript 

Pertama, kita akan membahas cara menulis sintaks untuk memasukkan kode JavaScript secara internal terlebih dahulu. Caranya cukup mudah layaknya menulis CSS secara internal pada berkas HTML. Cukup tuliskan kode JavaScript kita diantara tag pembuka dan penutup ().

Contohnya adalah sebagai berikut.
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
  </head>
  <body>
    <h2 id="pesan">Selamat datang!</h2>

    <script>
      const tamu = prompt('Siapakah Anda?');
      alert('Selamat datang, ' + tamu + '!');
    </script>
  </body>
</html>
```

External JavaScript 
Berikutnya kita akan membahas bagaimana memasukkan kode JavaScript ke dalam berkas HTML secara eksternal. Sama seperti memasukkan CSS secara eksternal pada berkas HTML, kita perlu menulis lokasi berkas berekstensi .js (dot js) pada atribut src di dalam tag 
`<script src=""></script>`
contoh penggunaan:

index.html:
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
  </head>
  <body>
    <h2 id="pesan">Selamat datang!</h2>

    <script src="script.js"></script>
  </body>
</html>
```

untuk peletakan nya sangat bebas tidak seperti CSS yang harus berada di dalam tag head. tetapi untuk javascript ini dianjurkan di letakan di paling bawah file html atau sebelum tag penutup html-nya.
