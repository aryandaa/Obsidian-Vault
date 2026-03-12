#programming 
Manipulasi DOM memberikan kemampuan bagi kita untuk membuat elemen-elemen HTML melalui kode JavaScript. Selain itu, melalui DOM kita mampu membuat konten HTML. 

Sekarang mari kita mulai dengan membahas _method_ `createElement()`_._ Dengan method tersebut, kita bisa membuat sebuah elemen HTML yang benar-benar baru tanpa memanipulasi isi konten berkas HTML.

Contohnya, jika kita ingin membuat sebuah elemen HTML dengan _tag_ `<p>`, sintaksnya adalah sebagai berikut:

```js
const newElement = document.createElement('p');
```
tidak cukup jika hanya membuat elemen baru. Bagaimana jika kita menambahkan teks? Caranya adalah kita berikan nilai string yang baru dan berikan pada properti `innerText` _._

kita juga bisa menambahkan attribute pada element tersebut, dengan cara memanggil function `.setAttribute()` Function ini menerima dua parameter, yaitu nama atribut yang ingin ditambahkan dan nilai yang ingin diberikan dalam artribut tersebut.

contoh saya ingin menambahkan attribute src dengan nilainya adalah gambar
```js
newImg.setAttribute('src', 'https://picsum.photos/200/300');
```

Sama halnya jika Anda menyiapkan berbagai bumbu pada piring terpisah. Hidangan tidak akan berubah (menjadi enak) sebelum menuangkan bumbu-bumbu tersebut. Kita akan mempelajari lebih lanjut tentang menambahkan elemen ke dokumen HTML pada materi "Menambahkan Elemen HTML ke DOM".