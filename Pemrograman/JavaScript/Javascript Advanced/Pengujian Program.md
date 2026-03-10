#programming 
Sebagai seorang pengembang aplikasi JavaScript, mungkin kita sudah familier dengan praktik pengujian. Bahkan, bisa saja kita melakukannya secara tak sadar. Ini menjadi tanggung jawab besar bagi developer agar sistem berjalan tanpa kurang suatu apa pun di tangan end-user. Tentu, hal ini tertanam dalam diri Anda, bukan?

Secara istilah, pengujian adalah proses memastikan keberhasilan suatu sistem untuk mencegah kegagalan saat beroperasi. Ada dua metode yang bisa kita lakukan. Jika tidak secara manual, kita akan lakukan pengujian aplikasi secara otomatis. Ya, bisa otomatis, Anda tidak salah dengar.

Pengujian manual tentu banyak pihak mampu melakukannya. Cukup jalankan program dan perhatikan output yang dikeluarkan. Perbaikan akan dilakukan jika terjadi error. Namun, cara ini sangatlah rentan dilakukan sebab adanya keluputan manusia dan hal yang paling terasa adalah tingkat efisiensi sangat rendah. Tenaga manusia yang akan lebih banyak dibutuhkan di sini selain komputer. Jika memanfaatkan metode otomatis, kita bisa mendelegasikan tugas kepada mesin dan biarlah ia yang bekerja. Tidak mengenal waktu, letih, dan keluputan adalah karakteristik dari mesin.


### Manual Lebih Mudah? Fix The Error

Sebelum belajar membuat kode testing otomatis, mari kita belajar memperbaiki kesalahan program yang mengandung beberapa bug dituntun oleh pengujian manual. Sebelum melanjutkan pembahasan, pastikan Anda sudah paham makna dari bug, ya!

Nah, kali ini, mari kita ambil contoh kasus program kalkulator total harga belanjaan yang perlu dibayar. Programnya sederhana, kok.
```js
// Fungsi untuk menghitung total harga belanjaan
function calculateTotal(shoppingCart) {
  let total = 0;

  // Penghitungan tagihan terjadi di sini…
  for (let i = 0; i <= shoppingCart.length; i += 1) {
    total += shoppingCart[i].price;
  }

  return total;
}

// Contoh data belanjaan
const shoppingCart = [
  { name: 'Apple', price: 300 },
  { name: 'Banana', price: 120 },
  { name: 'Orange', price: 130 },
];

// Memanggil fungsi dan mencetak hasilnya
console.log(`Total belanjaan: Rp ${calculateTotal(shoppingCart)}`);
```

disini saya langsung saja membaca errornya di mana lewat terminal, yaitu
```
    total += shoppingCart[i].price;
                             ^

TypeError: Cannot read properties of undefined (reading 'price')
    at calculateTotal (/home/r3x/Documents/Obsidian Vault/Pemrograman/JavaScript/Javascript Advanced/latihan/testingcode.js:7:30)
    at Object.<anonymous> (/home/r3x/Documents/Obsidian Vault/Pemrograman/JavaScript/Javascript Advanced/latihan/testingcode.js:21:36)
    at Module._compile (node:internal/modules/cjs/loader:1706:14)
    at Object..js (node:internal/modules/cjs/loader:1839:10)
    at Module.load (node:internal/modules/cjs/loader:1441:32)
    at Function._load (node:internal/modules/cjs/loader:1263:12)
    at TracingChannel.traceSync (node:diagnostics_channel:328:14)
    at wrapModuleLoad (node:internal/modules/cjs/loader:237:24)
    at Function.executeUserEntryPoint [as runMain] (node:internal/modules/run_main:171:5)
    at node:internal/main/run_main_module:36:49

Node.js v22.22.0
```

Letak error terjadi pada conditional loop dalam for statement. Alih-alih mendapatkan data belanjaan, kita malah berlebihan dalam mengakses index data. Ini ditandai dengan mengakses `shoppingCart[3]`. Padahal, maksimal angka index array adalah 2. Betul, kan? Seharusnya, kita gunakan simbol perbandingan “<”, bukan “<=”.

Sebetulnya ada cara yang lebih aman dibanding menggunakan for statement. Karena sudah belajar functional programming, kita bisa memanfaatkan `reduce` untuk melakukan iterasi data array. Bahkan, for statement perlu dihindari dalam functional programming, kan? Oleh karena itu, mari sesuaikan kode seperti berikut.

```js
function calculateTotal(shoppingCart) {
  const total = 0;
 
  return shoppingCart.reduce(
    (accumulator, cartItem) => accumulator + cartItem.price,
    total,
  );
}
```

Next problem. Tidak cukup sampai di sini. Kita perlu berikan variasi data yang lebih agar dapat menyaksikan ketahanan program. Bagaimana dengan data belanjaan berikut? Sudah cukup, ya.

```js
const shoppingCart = [
  { name: 'Apple', price: 300 },
  { name: 'Banana', price: 120 },
  { name: 'Orange', price: 130 },
  { name: 'Watermelon', price: '160' },
  { name: 'Pineapple', price: null },
  { name: 'Grape', price: null },
];
```

Ada beberapa tambahan variasi data yang kita miliki di atas, yaitu `price` dengan nilai string dan null. Menjadi pertanyaan besar bahwa mengapa kita perlukan data-data seperti ini?

Sebetulnya, kita tidak memiliki kendali terhadap nilai apa yang akan diberikan ke function. Jika data diambil dari sumber luar seperti API, kita belum tahu apa bentuknya. Tentunya, data-data seperti di atas tidak kita ekspektasikan dan sangat mungkin dialami oleh aplikasi. Aplikasi tetap berjalan sangat baik, tetapi beda cerita dengan adanya bug. Ini perlu segera diatasi.

Oleh karena itu, kita membutuhkan validasi sebelum proses kalkulasi dilanjutkan. Contohnya berikut.

```js
function calculateTotal(shoppingCart) {
  const total = 0;
 
  return shoppingCart.reduce((accumulator, cartItem) => {
    if (typeof cartItem.price === 'number') {
      return accumulator + cartItem.price;
    } else {
      console.error(`Tipe data cartItem.price tidak valid:`, cartItem);
      return accumulator;
    }
  }, total);
}
```

Catatan:
Meskipun ada data yang keliru, jangan lupa berikan return statement juga pada block else.

Perhatikan perubahan kode di atas! Bukan meneruskan ke proses kalkulasi, bila proses validasi tidak lolos, kita alihkan program ke block `else` dan tampilkan pesan error dalam console. Ini terjadi karena ada keanehan dalam data belanjaan.

Jika disimpulkan, berikut adalah hasil akhir dari program.

```js
// Fungsi untuk menghitung total harga belanjaan
function calculateTotal(shoppingCart) {
  const total = 0;

  return shoppingCart.reduce((accumulator, cartItem) => {
    if (typeof cartItem.price === 'number') {
      return accumulator + cartItem.price;
    } else {
      console.error(`Tipe data cartItem.price tidak valid:`, cartItem);
      return accumulator;
    }
  }, total);
}

// Contoh data belanjaan dengan beberapa kasus edge
const shoppingCart = [
  { name: 'Apple', price: 300 },
  { name: 'Banana', price: 120 },
  { name: 'Orange', price: 130 },
  { name: 'Watermelon', price: '160' },
  { name: 'Pineapple', price: null },
  { name: 'Grape', price: null },
];

// Memanggil fungsi dan mencetak hasilnya
console.log(`Total belanjaan: Rp ${calculateTotal(shoppingCart)}`);
```

Selamat! Silakan Anda saksikan hasil program yang terbebas dari bug, ya.

Kini kita menjadi paham bahwa selain memiliki error, program pun berpotensi memiliki bug. Meskipun penyelesaian bug dilakukan manual, kini kita sadar bahwa kehati-hatian dalam pengembangan program itu sangat penting.

Pengalaman kita dalam pengujian ini betul-betul dilakukan manual. Kita jalankan programnya dan perbaiki kesalahan saat ditemukan anomali. Ini tidak akan kita temukan jika sudah bermain dengan teknik otomatis.

### Uji Kode dengan Automated Test

Kita telah mencapai milestone memperbaiki program yang berpotensi terjadi bug. Kita uji dengan berbagai macam sampel data untuk menyaksikan ketahanan program dan akhirnya masalah yang muncul bisa diatasi. Sekali lagi! Manual sebetulnya memiliki efisiensi yang rendah dan bukanlah satu-satunya cara pengujian. Apa solusinya? Pengujian otomatis jawabannya.

Pengujian sebetulnya terbagi menjadi tiga bagian, yaitu unit test, service/integration test, dan UI test. Pengujian otomatis yang kita pelajari dalam materi ini adalah unit testing. Unit test akan menguji bagian terkecil dalam program seperti function. Jika ingin mendalami tipe testing lainnya, silakan simak artikel [Test Pyramid](https://martinfowler.com/bliki/TestPyramid.html).

Untungnya, runtime JavaScript seperti Node.js dan Bun memiliki built-in module (module bawaan) untuk melakukan pengujian secara otomatis. Pengujian ini sepenuhnya didelegasikan kepada mesin dan menampilkan umpan balik kepada kita jika ada keanehan hasil. Umpan balik ini bisa terjadi karena error atau bug yang ditemukan ketika program sedang diuji.

Pengujian otomatis akan memberikan dua kemungkinan hasil, yaitu pass dan fail. Jika pengujian dinyatakan lolos, runtime akan menandainya sebagai pass (biasanya diwarnai hijau), sedangkan runtime memberi hasil fail (biasanya diwarnai merah) saat pernyataan gagal muncul.

Sudah cukup pengantar kita kepada pengujian otomatis. Kita akan berlatih implementasinya pada materi berikutnya. Nah, hal berikutnya yang penting untuk kita pahami adalah apa urgensi dari unit testing dalam pengembangan program? 

- Mendeteksi kemungkinan error sedini mungkin. Sebisa mungkin, kita sebagai developer menemukan bug lebih dahulu sebelum end-user. 
- Aplikasi masih berfungsi dengan baik meskipun terjadi perubahan kode. Biasanya, sebelum dirilis ke publik, aplikasi harus dalam kondisi semua pengujian lolos.
- Proses pengujian dilakukan secara cepat dan efisien walaupun saat berkolaborasi. Makin besar aplikasi maka makin banyak juga yang diuji. Jika dilakukan secara manual, semua akan terasa sulit dan lama.

**Ingat!** Testing otomatis dapat membuat kita terhindar dari kebiasaan pengujian manual: jalankan program → saksikan hasil → perbaiki kode jika hasil aneh. Oke, mari kita sama-sama langsung ke materi berikutnya untuk belajar implementasi testing dalam aplikasi JavaScript.