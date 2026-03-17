#programming 
Saat selesai mengisi form pada sebuah halaman web, umumnya Anda akan mengarahkan cursor untuk submit semua data yang sudah terisi, bukan? Biasanya tombol tersebut memiliki caption seperti “Submit”, “Save”, atau semisalnya. Tombol tersebut biasanya berfungsi untuk mengirim data-data yang telah diinputkan oleh user pada form kepada proses lain, misalnya seperti mengirim data tersebut ke server untuk memperbarui data profil Anda.

Tapi tahukah Anda bahwa tombol tersebut unik? Unik dalam arti tombol pada form tidak dibuat melalui tag `<button>` (secara default bertipe "button") yang selama ini kita gunakan, melainkan sebuah tag khusus yakni `<input>` yang memiliki atribut type bernilai “submit”. Selain menggunakan tag `<input>`, kita juga bisa menggunakan tag `<button>` yang memiliki atribut type bernilai "submit", bukan "button".

Mungkin Anda berpikir bahwa untuk mengendalikan ter-submitnya form ke server perlu memberikan event submit pada tombol submit. Tentu tidak, kita akan memberikannya pada elemen `<form>` (jika menggunakan method addEventListener).


### Event onSubmit
Baik, cukup dengan teori, bagaimana jika lanjut melalui praktik saja? Pertama mari kita buat sebuah berkas HTML pada folder 'praktek/Form'.

Kita akan menambahkan sebuah fitur unik, yakni munculnya sebuah kalimat di bawah tombol button. Sudah siap, kan?

Kita hanya perlu menambahkan event listener pada elemen form dengan menambahkan kode pada index.js. Silakan tambahkan kode berikut padanya.
```js
const submitAction = document.getElementById('formDataDiri');
 
submitAction.addEventListener('submit', function (event) {
  const inputNama = document.getElementById('inputNama').value;
  const inputDomisili = document.getElementById('inputDomisili').value;
  const hiddenMessage = `Halo, ${inputNama}. Bagaimana cuacanya di ${inputDomisili}?`
 
  document.getElementById('messageAfterSubmit').innerText = hiddenMessage;
  event.preventDefault();
});
```

Kode di atas akan mengambil nilai yang sudah di-input oleh user. Caranya adalah memanggil properti value dari masing-masing elemen input pada form. Lalu, input akan dimasukkan ke sebuah string dengan sebuah format khusus yang akan ditampilkan ke layar.

Ada sebuah kode baru yang belum pernah kita bahas yakni `event.preventDefault()`. Apa fungsi kode tersebut? Ketika kita melakukan proses _submit_ pada _form_, halaman _web_ akan melakukan proses _refresh_. Nah, `event.preventDefault()` akan mencegah proses _refresh_ tersebut.

Melalui form ini, Anda bisa meminta user memasukkan nilai apa pun yang dibutuhkan dan memprosesnya dalam kode JavaScript untuk menghasilkan fungsionalitas yang lebih beragam berdasarkan input dari user.