#programming 
Sebelumnya kita telah mengimplementasikan event handler onload pada elemen body. Namun, mengapa ketika menekan tombol “Tekan Aku :)” tidak terjadi apa-apa? Hal ini dikarenakan kita belum memberikan event handler. 

Pada praktik ini, kita akan mengubah angka dalam teks untuk menampilkan berapa kali user menekan tombol. Caranya adalah memberikan event listener kepada button. Selain itu, kita juga akan memberikan kejutan lucu ketika user sudah menekan tombol hingga 7 kali. Penasaran? Mari kita langsung ngoding!

Buka berkas HTML yang sebelumnya sudah dibuat. Pada tag `<script>`, deklarasikan function increment() yang akan melakukan proses increment atau kenaikan angka sebagai jumlah berapa kali user menekan tombol. Ini dilakukan melalui event onclick. Silakan tambahkan kode seperti berikut.

```js
function increment() {
  document.getElementById('count').innerText++;
}
```

Pada kode di atas, kita memerintahkan agar teks melakukan proses increment (++) pada elemen yang memiliki atribut id dengan value count. Silakan tambahkan event handler pada elemen button seperti berikut.

```js
document.getElementById('incrementButton').onclick = increment;
```

Sekarang setiap kali tombol ditekan angka "0" semakin bertambah.