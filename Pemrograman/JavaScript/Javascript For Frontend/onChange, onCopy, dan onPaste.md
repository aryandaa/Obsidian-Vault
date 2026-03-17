#programming 
Sebelumnya, kita telah mempelajari tiga jenis event pada elemen input. Nah, ini berarti 3 sisa event lagi yang akan kita bahas. Beberapa event tersebut adalah onchange, oncopy, dan onpaste. Yuk, kita simak materinya!

### Event onChange

_Event onChange_ memiliki perilaku yang mirip dengan _onInput_, yaitu event yang terjadi jika terdapat perubahan nilai. Namun, terdapat perbedaan yang dimiliki oleh onChange.

Event _onInput_ akan terjadi jika elemen input mengalami perubahan nilai secara langsung, sedangkan event _onChange_ akan terjadi jika elemen input mengalami perubahan nilai dan menjadi blur (user tidak focus pada elemen tersebut). Sederhananya, event onChange seakan-akan merupakan gabungan dari event onInput dan onBlur. Untuk lebih jelasnya, kita akan berlatih pada contoh kasus sebelumnya.

Fitur yang ingin kita tambahkan adalah jika user menulis _captcha_ dengan benar, tombol “Submit Data” aktif. Bagaimana menambahkan _event handler_ _onChange_ pada elemen `<input>` untuk _captcha_? Simak uraiannya di bawah ini.

```js
  document.getElementById('inputCaptcha').addEventListener('change', function () {
    console.log('inputCaptcha: change');
    const inputCaptcha = document.getElementById('inputCaptcha').value;
    const submitButtonStatus = document.getElementById('submitButton');
    if (inputCaptcha === 'PRNU') {
      submitButtonStatus.removeAttribute('disabled');
    } else {
      submitButtonStatus.setAttribute('disabled', '');
    }
  });
```

Kode tersebut akan memeriksa apakah user memasukkan teks yang sesuai dengan captcha-nya. Jika sesuai, tombol “Submit Data” menjadi aktif. Namun, perlu diperhatikan sekali lagi bahwa untuk memicu kode pada event onChange, kita harus **mengubah** **nilai** input dan **mengalihkan** **fokus** dari elemen tersebut ke elemen lain. Kejadian pengalihan fokus ini dinamakan blur.



### Event onCopy
_Event onCopy_ tergolong dalam kelompok _clipboard events._ Event ini terjadi jika kita melakukan operasi pada _clipboard_ seperti _copy, cut,_ dan _paste_. Kita hanya akan membahas dua saja, yaitu _event onCopy_ sebagai operasi _copy_ dan _event onPaste_ sebagai operasi _paste_. Pertama kita akan menggunakan _onCopy_ terlebih dahulu.

Pada berkas HTML di atas, kita sudah memiliki bagian _form_ yang dihiasi dengan kata kunci _“copy”_. Tugas kita kali ini adalah menambahkan _event listener_ untuk _event onCopy_. Sedangkan fungsi _event handler_-nya hanyalah memunculkan sebuah _dialog box alert_ yang berisi pesan “Anda telah men-copy sesuatu...”.

```js
  document.getElementById('inputCopy').addEventListener('copy', function () {
    alert('Anda telah men-copy sesuatu...');
  });
```


### Event onPaste
_Event onPaste_ tergolong dalam kelompok _clipboard events_ seperti yang kita bahas sebelumnya. Event ini akan terjadi ketika melakukan operasi _paste_ pada elemen yang sudah kita beri _event listener_ untuk _event onPaste_.

Pada berkas HTML di atas, kita juga sudah memiliki bagian _form_ yang dihiasi dengan kata kunci _“paste”_. Tugas kali ini mirip dengan apa yang telah kita lakukan pada _event onCopy_. Kita hanya membuat fungsi _event handler_ untuk memunculkan sebuah _dialog box alert_ yang berisi pesan “Anda telah mem-paste sebuah teks...”.

```js
 document.getElementById('inputPaste').addEventListener('paste', function () {
    alert('Anda telah mem-paste sebuah teks...');
  });
```