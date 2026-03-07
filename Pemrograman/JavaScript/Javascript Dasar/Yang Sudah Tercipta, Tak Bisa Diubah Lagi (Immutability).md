#programming 

Kita sudah mengetahui bahwa banyak benefit yang didapatkan ketika bisa menjaga kesucian sebuah fungsi (_pure function_). Menghasilkan efek samping, seperti mengubah sebuah data yang bersumber dari luar bisa menyebabkan fungsi menjadi impure. Untuk selalu menjaga bahwa fungsi selalu pure, dalam FP juga terdapat sebuah konsep bahwa segala yang sudah dibuat, tidak bisa diubah nilainya. Konsep ini disebut sebagai immutability.

Walau terdengar sedikit menyeramkan bagi kita yang sudah terbiasa mengubah data sesuka hati, sebenarnya konsep ini memiliki tujuan yang baik. Tujuannya adalah memastikan sebuah nilai tidak dapat diubah dengan mudah (atau bahkan tidak bisa). Tujuannya tentu untuk menghindari segala perubahan yang tidak terduga dan biasanya menjadi akar permasalahan, seperti bug.

Dalam JavaScript, kita dapat menerapkan prinsip immutability dengan menggunakan fungsi yang mengembalikan salinan baru, alih-alih mengubah data asli. Biasanya ini dilakukan ketika kita perlu mengubah data dari objek ataupun array. Namun, sebelum mengetahui berbagai fungsi yang dapat mendukung prinsip immutability, kita perlu tahu dulu fungsi-fungsi “bahaya” yang perlu diperhatikan kembali.  
  

### Fungsi yang Mengubah Data (Mutator Function)

Secara umum, perubahan data secara tidak sadar terjadi karena penggunaan beberapa fungsi bawaan JavaScript yang bersifat mengubah atau biasa disebut mutator function. Berikut adalah beberapa fungsi yang sering kita gunakan dan harus diperhatikan kembali ketika menerapkan prinsip immutability.

1. [Array.push](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push): menambahkan elemen di akhir dari sebuah array.
2. [Array.pop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/pop): menghapus elemen terakhir dari sebuah array.
3. [Array.shift](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/shift): menghapus elemen pertama dari sebuah array.
4. [Array.unshift](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/unshift): menambahkan elemen di awal dari sebuah array.
5. [Array.splice](https://developer.mozilla.org/id/docs/Web/JavaScript/Reference/Global_Objects/Array/splice): menambahkan atau menghapus elemen di posisi tertentu dari sebuah array.
6. [Array.reverse](https://developer.mozilla.org/id/docs/Web/JavaScript/Reference/Global_Objects/Array/reverse): membalikkan urutan elemen dari sebuah array.
7. [Array.sort](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort): mengurutkan elemen dari sebuah array.
8. [Object.assign](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign): memodifikasi properti dari object.

Daftar fungsi di atas bersifat mutate, alias mengubah langsung data array asli. Tentu penggunaan method tersebut di dalam fungsi akan membuat fungsi menghasilkan efek samping.

Perhatikan contoh kode di bawah ini.
```js
function max(arrayOfNumbers) {
  return arrayOfNumbers
    .sort((a, b) => a - b)
    .pop();
}

const numbers = [10, 23, 24, 7, 42, 18];
const largest = max(numbers);

console.log(largest); // Output: 42
console.log(numbers); // Output: [ 7, 10, 18, 23, 24 ]
```

Fungsi `max` adalah fungsi yang mengembalikan elemen bernilai terbesar dari array yang dikirimkan melalui argumen. Sepintas, fungsi `max` terlihat pure karena tidak mengakses nilai selain dalam argumennya. Namun, karena dalam implementasinya kita menggunakan fungsi `sort` dan `pop`, fungsi max jadi memiliki efek samping, yaitu mengubah nilai array `numbers` yang diberikan melalui argumen. Efek samping ini mungkin saja tidak terduga karena tujuan fungsi tersebut hanya mengembalikan elemen yang paling besar.

Selain pada array, perubahan data juga banyak terjadi dalam object. Salah satunya adalah penggunaan fungsi `Object.assign` yang dapat mengubah nilai pada sebuah objek yang sudah terbentuk sebelumnya.

```js
function registerEmail(person, email) {
  return Object.assign(person, { email });
}

const person = {
  name: 'John',
  username: 'johndoe',
};

const personWithEmail = registerEmail(person, 'john@dicoding.com');

console.log(person); // Output: { name: 'John', username: 'johndoe', email: 'john@dicoding.com' }
console.log(personWithEmail); // Output: { name: 'John', username: 'johndoe', email: 'john@dicoding.com' }
```

Anda bisa lihat bahwa fungsi `registerEmail` menambahkan properti email, baik pada `personWithEmail` maupun person.


#### Duplikasi alih-alih Mengubah Aslinya

Lalu, solusinya seperti apa? Untuk membuat kedua fungsi di atas kembali pure, kita tidak boleh memodifikasi nilai yang diberikan melalui argumen. Umumnya, hal ini dilakukan dengan menduplikasi nilai array atau objek dan menambahkan data baru, lalu kembalikan fungsi menggunakan nilai baru tersebut.

Secara umum, proses duplikasi data dapat dilakukan dengan mudah menggunakan sintaksis spread operator. Berikut adalah versi perbaikan dari fungsi `max` dan `registerEmail` agar bersifat immutate.
```js
function max(arrayOfNumbers) {
  // menggunakan spread operator untuk menduplikasi nilai arrayOfNumbers
  return [...arrayOfNumbers]
    .sort((a, b) => a - b)
    .pop();
}

function registerEmail(person, email) {
  // menggunakan spread operator untuk menduplikasi nilai person
  return { ...person, email };
}

const numbers = [10, 23, 24, 7, 42, 18];
const largest = max(numbers);

console.log(largest); // Output: 42
console.log(numbers); // Output: [ 10, 23, 24, 7, 42, 18 ]

const person = {
  name: 'John',
  username: 'johndoe',
};

const personWithEmail = registerEmail(person, 'john@dicoding.com');

console.log(person); // Output: { name: 'John', username: 'johndoe' }
console.log(personWithEmail); // Output: { name: 'John', username: 'johndoe', email: 'john@dicoding.com' }
```

### Immutable Array Methods

JavaScript telah menyediakan banyak fungsi bawaan yang dapat digunakan dan bersifat immutable. Untuk kasus umum, seperti pengelolaan data array, Anda dapat memanfaatkan beberapa fungsi berikut dan menjamin bahwa tidak timbul efek samping.

#### Array Map
Fungsi `Array.map()` adalah bawaan dari array yang sangat berguna dan banyak sekali digunakan. Fungsi ini dapat dipanggil dari sebuah data bertipe array dan menerima satu buah callback function.

```js
['Harry', 'Ron', 'Jeff', 'Thomas'].map(() => { });
```
Callback function tersebut akan dipanggil sebanyak jumlah panjang array dan akan memiliki akses pada index array sesuai dengan iterasinya.

Fungsi map akan mengembalikan array baru. Nilai tiap item pada array yang dikembalikan dihasilkan dari kembalian callback function-nya.
```js
const oldArray = ['Harry', 'Ron', 'Jeff', 'Thomas']
const newArray = oldArray.map((name) => `${name}!`);

console.log(newArray); // Output: [ 'Harry!', 'Ron!', 'Jeff!', 'Thomas!' ]
console.log(oldArray); // Output: [ 'Harry', 'Ron', 'Jeff', 'Thomas' ]
```

#### Array Filter

Fungsi ini sangat berguna untuk melakukan proses penyaringan (_filtering_) terhadap nilai array yang ada. Bila Anda memiliki kasus ingin menghilangkan beberapa item dalam array berdasarkan spesifikasi tertentu, fungsi ini sangatlah cocok digunakan.

Cara kerja fungsi ini mirip seperti `Array.map()`. Namun, callback function dari fungsi ini harus mengembalikan boolean. Nilai boolean ini digunakan untuk menentukan item array lolos saring atau tidak.

Sama seperti fungsi `map()`, fungsi `filter()` juga akan mengembalikan array yang telah disaring dalam bentuk array baru.

Inilah contoh penggunaan ketika Anda ingin menghilangkan seluruh nilai false pada array sebagai berikut.

```js
const truthyArray = [1, '', 'Halo', 0, null, 'Harry', 14]
  .filter((item) => Boolean(item));

console.log(truthyArray); // Output: [ 1, 'Halo', 'Harry', 14 ]
```

Contoh lain, penggunaan filter untuk menyaring array dari objek siswa yang layak mendapatkan beasiswa berdasarkan nilai skor yang didapat.

```js
const students = [
  {
    name: 'Harry',
    score: 60,
  },
  {
    name: 'James',
    score: 88,
  },
  {
    name: 'Ron',
    score: 90,
  },
  {
    name: 'Bethy',
    score: 75,
  }
];

const eligibleForScholarshipStudents = students.filter((student) => student.score > 85);

console.log(eligibleForScholarshipStudents);

/**
 * Output:
 * [ { name: 'James', score: 88 }, { name: 'Ron', score: 90 } ]
 * 
 */
```

#### Array Reduce

Array.reduce digunakan untuk mengeksekusi fungsi reducer pada setiap elemen array dan hanya mengembalikan output satu nilai saja. Berikut adalah struktur dari penggunaan fungsi `Array.reduce`.

```js
array.reduce(callback(accumulator, currentValue, [currentIndex], [array]), [initialValue])
 
// [...] adalah opsional parameter
```

Callback function dari fungsi ini dapat diolah untuk manipulasi data `currentValue` dan menyimpannya pada `accumulator`. Selain itu, fungsi reduce juga memiliki nilai awal yang dapat didefinisikan pada bagian `initialValue`.

Inilah contoh penggunaan ketika kita ingin menjumlahkan total nilai siswa seperti di bawah ini.

```js
const students = [
  {
    name: 'Harry',
    score: 60,
  },
  {
    name: 'James',
    score: 88,
  },
  {
    name: 'Ron',
    score: 90,
  },
  {
    name: 'Bethy',
    score: 75,
  }
];

const totalScore = students.reduce((acc, student) => acc + student.score, 0);

console.log(totalScore); // Output: 313
```

### Immutable Object

JavaScript menyediakan fungsi `Object.freeze` untuk membekukan objek sehingga tidak dapat diubah setelah dibuat. Melalui fungsi ini, kita bisa memastikan bahwa tidak ada perubahan yang dapat dilakukan pada objek tersebut.
```js
const user = {
  name: 'John',
  email: 'john@dicoding.com',
};

// Membekukan objek user
Object.freeze(user);

// Mencoba mengubah properti dari objek yang dibekukan
user.email = 'doe@dicoding.com';
console.log(user); // Output: { name: 'John', email: 'john@dicoding.com' }
```

Pada contoh di atas, kita menggunakan `Object.freeze` untuk membekukan objek user. Setelah objek dibekukan, setiap upaya untuk mengubah properti akan diabaikan (atau menghasilkan error jika mengaktifkan mode strict). Dengan demikian, kita dapat memastikan bahwa objek tidak akan bisa diubah secara tidak sengaja.

Namun, perlu diingat bahwa `Object.freeze` hanya membekukan tingkat pertama dari objek. Jika objek tersebut memiliki properti yang merupakan objek lain, properti tersebut masih dapat diubah. Untuk membuat objek benar-benar immutable, kita perlu membekukan setiap objek yang menjadi properti secara rekursi.
```js
function deepFreeze(object) {
  Object.keys(object).forEach((name) => {
    const prop = object[name];
    if (typeof prop == 'object' && prop !== null) {
      deepFreeze(prop);
    }
  });

  return Object.freeze(object);
}

const complexUser = {
  name: 'Bob',
  email: 'bob@dicoding.com',
  preferences: {
    newsletter: true,
    notifications: 'weekly',
    address: {
      city: 'New York',
      zip: '10001'
    }
  }
};

deepFreeze(complexUser);

// Diabaikan
complexUser.preferences.address.city = 'Los Angeles';

console.log(complexUser.preferences.address.city); // Output: 'New York'
```

