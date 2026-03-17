#programming 

Kali ini kita akan mempelajari menerapkan event handler menggunakan function addEventListener. Pertama saya akan menduplikat lagi file event.html dan mengubah sebagian codenya agar di sesuaikan dengan materi ini.

Method addEventListener() menerima beberapa parameter, tetapi yang perlu kita ketahui sementara adalah parameter pertama dan kedua. Parameter pertama harus diisi dengan tipe event yang digunakan, yang mana akan men-trigger atau memancing kode JavaScript untuk menjalankan sebuah fungsi khusus. Function khusus diletakkan pada parameter kedua yang akan dijalankan ketika tipe event yang didefinisikan terjadi. 

Ada satu aturan yang perlu kita ketahui, yaitu nama event yang kita definisikan tidak seperti sebelumnya menggunakan onload dan onclick (tanpa imbuhan "on"). Namun, kita dapat menuliskannya secara langsung. Sebagai contoh function onload menjadi ‘load’, function onclick menjadi ‘click’. Untuk daftar lengkap event apa saja yang didukung dapat dilihat di sini: https://developer.mozilla.org/en-US/docs/Web/Events.

Okay, kita sudah mengetahui teknis seputar method addEventListener(). Berikutnya kita akan sepenuhnya fokus latihan. Tambahkan kode berikut dibawah komentar yang bercetak tebal.

```js
window.addEventListener('load', welcome);
document.getElementById('incrementButton').addEventListener('click', increment);
```

Mungkin Anda bertanya-tanya, "mengapa event load dipasangkan ke obyek window?". Jawabannya adalah method addEventListener() tidak bisa bekerja pada tag `<body>` sehingga kode akan berbentuk seperti berikut.

```html
<script>
  function increment() {
    document.getElementById('count').innerText++;
       
    if (document.getElementById('count').innerText == 7) {
      const hiddenMessage = document.createElement('h4');
      hiddenMessage.innerText = 'Selamat! Anda menemukan hadiah tersembunyi...';
 
      const image = document.createElement('img');
      image.setAttribute('src', 'https://i.ibb.co/0V49VRZ/catto.jpg');
 
      const contents = document.querySelector('.contents');
      contents.appendChild(hiddenMessage).appendChild(image);
    }
  }
 
  function welcome() {
    alert('Sim salabim muncullah elemen-elemen HTML!');
    const contents = document.querySelector('.contents');
    contents.removeAttribute('hidden');
  }
 
 window.addEventListener('load', welcome);
 document.getElementById('incrementButton').addEventListener('click', increment);
</script>
```

Jalankan kembali berkas HTML di atas, ia pasti akan berfungsi normal kembali! Lantas, jika sama dengan inline event handler, apa keuntungan lebih yang ditawarkan method addEventListener()? Kelebihannya adalah kita bisa menambahkan satu atau lebih fungsi sebagai event handler. Fitur itulah yang tidak dapat dilakukan oleh event handler inline.

```html
<script>
  // contoh penerapan
  element.onclick = fungsiA;
  element.onclick = fungsiB;
</script>
```

Selain itu, terdapat permasalahan lagi jika tidak menggunakan addEventListener. Kode di atas, kita memanggil function onclick dan melakukan assignment dengan fungsiA dan fungsiB. Sayangnya, fungsiA ini akan ter-overwrite alias tertimpa fungsiB. Oleh karena itu, jika elemen di-klik, hanya fungsiB saja yang dijalankan. Bagaimana cara kita menemukan solusi agar fungsiA dan fungsiB dijalankan ketika elemen di-klik? Gunakanlah method addEventListener()!

```html
<script>
  // contoh penerapan
  element.addEventListener('click', fungsiA);
  element.addEventListener('click', fungsiB);
</script>
```

Selain mampu menambahkan multiple event listener dalam satu event, kita juga akan mempelajari penerapan method addEventListener() lebih tepat untuk skenario-skenario tertentu ketimbang menggunakan event handler yang dicontohkan sebelumnya. Method addEventListener() juga mendukung fitur “event bubbling dan capturing” yang akan kita bahas nantinya.