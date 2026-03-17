#programming 
Tipe storage yang pertama adalah local storage yang digunakan untuk menyimpan data tanpa ada batasan waktu. Data yang disimpan tidak akan hilang bila browser atau tabs browser ditutup kecuali jika kita menghapusnya.

Untuk menggunakan local storage, kita harus mengaksesnya melalui objek yang bernama "localStorage". Kemudian untuk menyimpan datanya, kita harus menggunakan method setItem() dari objek tersebut.

Method setItem() membutuhkan 2 parameter, di mana parameter pertama adalah key dan kedua adalah value yang ingin kita simpan. Kemudian, untuk mengaksesnya, kita memerlukan method getItem() yang membutuhkan 1 parameter, yaitu nilai key yang kita gunakan untuk menyimpan data. Sebagaimana disebutkan sebelumnya, data pada local storage bisa dihapus dengan method removeItem() yang menerima 1 parameter, yakni nilai key yang kita gunakan untuk menyimpan sebuah objek.

Berikut adalah penerapan dari local storage.

Index.html:
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Web Storage World</title>

    <link rel="stylesheet" href="styles.css">
  </head>
  <body>
    <main class="contents" align="center">
      <h1>Local Storage</h1>

      <button id="incrementButton">Tambah nilai</button>
      <button id="clear">Hapus storage</button>

      <h3>Kamu sudah menekan tombol di atas sebanyak:</h3>
      <h2 id="count">0</h2>
    </main>

    <script src="index.js"></script>
  </body>
</html>
```

Styles.css:
```css
.contents {
  border: 2px solid black;
  padding: 15px;

  position: fixed;
  top: 50%;
  left: 50%;

  transform: translate(-50%, -50%);
}

#generateButton {
  margin-top: 5px;
  margin-bottom: 15px;
}
```

index.js:
```js
const localStorageKey = 'PRESS_FREQUENCY';

// Pengecekan: apakah data localStorage dengan key count tersedia atau belum
if (typeof Storage !== 'undefined') {
  if (localStorage.getItem(localStorageKey) === null) {
    // Jika item pada local storage belum ada, data akan diberi nilai awal, yakni 0
    localStorage.setItem(localStorageKey, 0);
  }
  const incrementButton = document.querySelector('#incrementButton');
  const clearButton = document.querySelector('#clear');
  const countDisplay = document.querySelector('#count');

  // Memberikan nilai item dari local storage
  countDisplay.innerText = localStorage.getItem(localStorageKey);

  // Update nilai dari item local storage jika tombol ditekan
  incrementButton.addEventListener('click', function () {
    let count = localStorage.getItem(localStorageKey);
    count++;
    localStorage.setItem(localStorageKey, count);
    countDisplay.innerText = localStorage.getItem(localStorageKey);
  });

  // Memberikan nilai 0 ke tampilan karena di-reset dan menghapus item
  clearButton.addEventListener('click', function () {
    localStorage.removeItem(localStorageKey);
    countDisplay.innerText = 0;
  });
} else {
  alert('Browser yang Anda gunakan tidak mendukung Web Storage');
}
```

kita bisa mengetahui bahwa data yang disimpan pada local storage akan bertahan walaupun jendela browser atau tab browser ditutup. Untuk menghapus datanya, tekan tombol "Hapus Storage" di mana tombol tersebut akan memanggil method `localStorage.removeItem()`.