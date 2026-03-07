#programming 
Kita sudah memahami bahwa fungsi dalam JavaScript bersifat first-class citizen (Konsep di mana function dalam JavaScript dapat diperlakukan seperti nilai atau objek lain, dapat disimpan dalam variabel, dikirimkan sebagai argument, atau dikembalikan dari function lain.). Fungsi dapat diperlakukan sebagai expression yang dapat disimpan dalam sebuah variabel atau dikirim sebagai argumen fungsi lain. Hal ini membuka banyak potensi menarik karena kita bisa menggunakan fungsi secara leluasa.

Ada konsep dalam FP yang sangat mengandalkan kemampuan function expression. Konsep tersebut adalah high-order function (selanjutnya akan disingkat menjadi HOF). HOF adalah fungsi yang menerima fungsi lainnya sebagai argumen dan/atau mengembalikan sebuah fungsi lain. Umumnya, teknik HOF digunakan untuk berbagai hal berikut.

- Mengabstraksi fungsi aksi dari sebuah proses asynchronous (kita akan belajar asynchronous dalam modul selanjutnya) dalam bentuk callback.
- Membuat utility function, yaitu fungsi Array.map, Array.filter, Array.reduce, dan sebagainya.
- Menerapkan teknik matematika, seperti [currying](https://en.wikipedia.org/wiki/Currying) dan [function composition](https://en.wikipedia.org/wiki/Function_composition).

HOF memungkinkan kita untuk membuat fungsi yang fleksibel. Misalnya, kita bisa membuat fungsi `apply` yang menerima fungsi `operation` sebagai argumen untuk melakukan sebuah operasi pada dua nilai argumen lain.

```js
function apply(operation, ...args) {
  // kita bisa menambahkan kode lain sebelum operation dijalankan.
  
  return operation(...args)
}

function sum(a, b, c) {
  return a + b + c;
}

function discount(disc, value) {
  return value - ((disc / 100) * value);
}

const productPrice = apply(sum, 100, 100, 200);
const withDiscount = apply(discount, 25, productPrice);

console.log('Product price:', productPrice); // Output: Product price: 400
console.log('With discount 25%:', withDiscount); // Output: With discount 25%: 300
```

Dengan HOF, kita bisa dengan mudah mengubah logika operasi tanpa harus mengubah struktur fungsi apply. Selain itu, kita juga bisa menambahkan kode lain di dalam fungsi apply sebelum sebuah operasi dipanggil jika dibutuhkan.

implementasi _memoization pure function_ juga dilakukan dengan teknik HOF. Caranya adalah fungsi memoize menerima fungsi pure function sebagai argumen dan menyimpan hasil dari pemanggilan pure function untuk digunakan ketika terjadi pemanggilan ulang dengan argumen yang sama. Jadi, jika terjadi pemanggilan dengan argumen yang sama, cukup mengembalikan nilai dari yang sudah tersimpan.
```js
// menerima argumen sebuah fungsi
function memoize(fn) {
  const cache = new Map();

  // mengembalikan nilai berupa fungsi
  return function(...args) {
    const key = JSON.stringify(args);

    if (cache.has(key)) {
      return cache.get(key);
    }

    const result = fn(...args);
    cache.set(key, result);

    return result;
  };
}


function sumArray(arr) {
  if (arr.length === 0) return 0;
  return arr[0] + sumArray(arr.slice(1));
}


const memoizedSumArray = memoize(sumArray);
const largeArray = Array.from({ length: 5000 }, (_, i) => i + 1);

console.time('Memoized Sum First Call');
console.log('Total:', memoizedSumArray(largeArray));
console.timeEnd('Memoized Sum First Call');

console.time('Memoized Sum Second Call (Cached)');
console.log('Total:', memoizedSumArray(largeArray));
console.timeEnd('Memoized Sum Second Call (Cached)');
```

Anda bisa jalankan kode di atas. Lihat perbedaan yang sangat signifikan dari waktu yang dibutuhkan untuk memanggil fungsi `memoizedSumArray` pertama kali dan kedua kalinya. Berikut adalah salah satu contoh output dari menjalankan kode di atas.
```
Total: 12502500
Memoized Sum First Call: 127.57ms
 
Total: 12502500
Memoized Sum Second Call (Cached): 0.357ms
```

Hal lain yang umum dilakukan dengan HOF adalah membuat fungsi yang menerapkan teknik currying. Dengan teknik currying, sebuah fungsi biasanya tidak mengambil semua argumen secara langsung. Ia mengambil satu argumen dulu, lalu mengembalikan sebuah fungsi baru yang menerima argumen kedua, begitu seterusnya hingga seluruh argumen dimanfaatkan dan melakukan operasi secara utuh.

Berikut adalah contoh teknik currying pada fungsi `adjectivfy` dan `multipleBy`.

```js
function adjectivfy(adjective) {
  return function (noun) {
    return `${noun} ${adjective}.`;
  }
}

function multipleBy(x) {
  return function(y) {
    return x * y;
  }
}

const coolifier = adjectivfy('keren');
const funnifier = adjectivfy('seru');

const multipleByFive = multipleBy(5);

console.log(coolifier('Dicoding')); // Output: Dicoding keren.
console.log(funnifier('JavaScript')); // Output: JavaScript seru.
console.log(multipleByFive(7)); // Output: 35
console.log(multipleByFive(10)); // Output: 50
```
HOF juga bisa digunakan untuk komposisi fungsi, yaitu kita menggabungkan beberapa fungsi kecil menjadi satu fungsi yang lebih kompleks. Berikut adalah contoh praktik dari komposisi fungsi.

```js
function addOne(x) {
  return x + 1;
}

function square(x) {
  return x * x;
}

function compose(f, g) {
  return (x) => {
    return f(g(x));
  }
}

const addOneAndSquare = compose(square, addOne);

console.log(addOneAndSquare(2)); // output: 9
```

Contoh di atas menunjukkan bahwa compose adalah HOF yang menggabungkan dua fungsi menjadi satu fungsi baru yang menjalankan `g` terlebih dahulu dan kemudian `f`.

Sudah paham dengan HOF?

Secara tidak sadar, mungkin Anda juga sebetulnya sudah pernah memanfaatkan teknik HOF, tetapi belum mengenal namanya saja. Beberapa contoh HOF yang umum digunakan dalam JavaScript adalah penggunaan fungsi `Array.map`. Fungsi `Array.map` menerima sebuah fungsi sebagai argumen yang digunakan untuk memproses setiap elemen array. Fungsi `Array.map` mengembalikan array baru yang hasilnya adalah nilai dari pemanggilan fungsi pada setiap elemen array asli.

```js
const numbers = [1, 2, 3, 4];

const doubled = numbers.map((num) => num * 2);

console.log(doubled); // [2, 4, 6, 8]
```