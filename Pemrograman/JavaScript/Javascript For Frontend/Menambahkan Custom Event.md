#programming 
Apa yang dimaksud dengan Custom Event? Custom Event pada materi ini merujuk kepada penggunaan class Event() untuk membuat event dengan nama yang sudah kita tentukan sendiri. Misal, sebelumnya kita telah menggunakan nama-nama event yang sudah “dikenal” oleh JavaScript yakni seperti “click” dan “load’. Apakah mungkin jika kita membuat event sendiri? Misalnya, event dengan nama "eventBuatanKita"? Jawabannya, sangat mungkin! Mari kita lihat sintaks berikut.

```js
// membuat custom event
const eventBuatan = new Event('eventBuatanKita');
 
// meletakkannya pada sebuah method addEventListener()
element.addEventListener('eventBuatanKita'); 
```

Kode di atas menunjukkan kepada kita cara membuat custom event dan menerapkannya pada event listener. Jika Anda bertanya-tanya, “Kenapa kita harus mempelajari custom event?" Jawabannya adalah tidak seperti event yang biasanya “dikenali” oleh method addEventListener, custom event memungkinkan kita untuk menjalankan sebuah event handler setelah sebuah event handler lain selesai dipanggil.

silahkan buka file html bernama makeCostumeEvent.html pada folder praktek.

Pada awal isi dari tag `<script>`, buatlah variabel baru dan inisialisasikan dengan custom event yang bernama “changeCaption”.
```js
const changeCaption = new Event('changeCaption');
```

Kemudian tambahkan sebuah event listener untuk custom event dan event listener pada button melalui method addEventListener() ketika tombol tersebut ditekan.

```js
window.addEventListener('load', function() {
  const tombol = document.getElementById('tombol');
  tombol.addEventListener('changeCaption', customEventHandler);
  tombol.addEventListener('click', function() {});
});
```

Pada tahap terakhir kita akan mendeklarasikan function customEventHandler yang dijalankan ketika event changeCaption terjadi.

```js
function customEventHandler(ev) {
  console.log('Event ' + ev.type + ' telah dijalankan');
  const caption = document.getElementById('caption');
  caption.innerText = 'Anda telah membangkitkan custom event';
}
```

Fungsi dari customEventHandler memiliki 1 parameter yang bernama “ev”. Apa itu “ev”? Secara otomatis, parameter “ev” berisi obyek event (“ev” merupakan singkatan dari “event”). Dengan obyek ini, kita dapat memeroleh banyak informasi mengenai elemen yang terkait. Semua ini akan dilakukan secara otomatis oleh JavaScript.

 tidak ada efek apa pun yang dihasilkan dari perubahan apa pun ketika tombol ditekan, bukan? Hal tersebut terjadi karena kita belum membuat fungsi untuk eventHandler pada event “click” pada tombol tersebut. Mari lengkapi kode kita pada materi berikutnya!
