#programming 
Di sini kita akan membangkitkan custom event yang sudah dibuat pada materi sebelumnya. Dalam praktik ini, kita tidak perlu menambahkan banyak kode, melainkan hanya fungsi yang berisi proses dispatch atau pemanggilan custom event handler. 

kita akan memanggil function dispatchEvent() untuk trigger custom event yang telah dideklarasikan dan dipasangkan, yaitu changeCaption. Caranya adalah masukkan argument pada function dispactEvent() dengan variabel changeCaption. Jadi, hasilnya adalah sebagai berikut.

```js
tombol.addEventListener('click', function () {
  tombol.dispatchEvent(changeCaption);
});
```

Dengan demikian, kode JavaScript dalam tag `<script>` secara keseluruhan menjadi seperti berikut.

```html
<script>
      const changeCaption = new Event('changeCaption');

      window.addEventListener('load', function () {
        const tombol = document.getElementById('tombol');

        tombol.addEventListener('changeCaption', customEventHandler);
        tombol.addEventListener('click', function () {});
      });

      function customEventHandler(ev) {
        console.log('Event ' + ev.type + ' telah dijalankan');
        const caption = document.getElementById('caption');
        caption.innerText = 'Anda telah membangkitkan custom event';
      }
</script>
```

Simpan berkas HTML dan buka kembali. Jika tombol yang muncul ditekan, teks di atas tombol akan berubah. Selain itu, console.log() juga dijalankan dan muncul log pada console browser.

Sama halnya dengan event listener pada umumnya. Jika tidak menampilkan event melalui elemen lain yang tidak sama dengan elemen yang memiliki event listener, function customEventHandler tidak akan dijalankan (invoked). Sebagai contoh jika kita memanggil fungsi event handler melalui elemen lain, event handler tidak akan memproses event-nya.

Tidak jauh berbeda dengan menerapkan event yang sudah “dikenal” oleh JavaScript seperti onclick dan onload, bukan?