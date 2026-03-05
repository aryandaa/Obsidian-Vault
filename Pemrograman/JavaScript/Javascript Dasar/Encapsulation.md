#programming 

Encapsulation berasal dari kata Capsul yang artinya membungkus, Encapsulation adalah proses untuk membungkus data di suatu wadah yang disebut dengan class. Menyembunyikan data adalah bagian kunci dari encapsulation.

Desain OOP yang baik adalah object hanya akan menampilkan data yang dibutuhkan oleh object lain. Data akan diisolasi dan tidak dapat diakses langsung dari luar. Secara sederhana, encapsulation adalah membuat data yang ada di class sebagai private.

Di dunia nyata, kita bisa lihat contohnya pada mesin kopi. Mesin kopi memiliki data dan method yang bersifat private seperti pengatur suhu, pemanas, dan method memanaskan air. Data dan method tersebut tidak bisa diakses oleh pihak luar (kita sebagai pengguna).

### Properti dan Method
Seperti yang Anda ketahui, di dalam sebuah class kita dapat mendefinisikan dua hal, yaitu property dan method. Karena kita menerapkan encapsulation, kita harus mengatur akses dari keduanya. Secara umum, property yang ada di dalam instance class bersifat mutable (dapat diubah). Perhatikan contoh berikut ini.

```js
class CoffeMachine {
  constructor(waterAmount) {
    this.waterAmount = waterAmount;
    this.temperature = 90;
  }

  makeCoffe() {
    console.log('Membuat kopi dengan suhu', this.temperature);
  }
}

const coffee = new CoffeMachine(100);
coffee.temperature = 60;

coffee.makeCoffe(); // Output: Membuat kopi dengan suhu 60
```

Pada contoh di atas, kita menetapkan _temperature_ mesin kopi 90 derajat Celcius, tetapi ada pengguna yang iseng mengubahnya menjadi 60. Mengubah nilai tersebut bisa saja mengakibatkan mesin kopi rusak. Meskipun kita sudah menetapkan nilai `temperature`, nilainya tetap dapat diubah. Hal ini tidaklah baik. Untuk mencegah hal itu terjadi lagi, kita dapat menerapkan getter dan setter.

Getter terdiri dari method get. get adalah cara untuk mendapatkan nilai dari property, sedangkan setter terdiri dari method set. set adalah method untuk menetapkan nilai property. Dengan begitu, kita dapat mengatur akses ke property yang dimiliki oleh object. Perhatikan contoh berikut ini.

```js
class CoffeeMachine {
  constructor(waterAmount) {
    this.waterAmount = waterAmount;
    this._temperature = 90
  }

  set temperature(temperature) {
    console.log('you are not allowed to change the temperature');
  }

  get temperature() {
    return this._temperature;
  }
}

const coffee = new CoffeeMachine(10);
console.log('Sebelum diubah: ', coffee.temperature);
coffee.temperature = 100;
console.log('Setelah diubah: ', coffee.temperature);
```

Penambahan underscore (`_`) di variable temperature untuk menandakan bahwa nilai temperature tidak dapat diubah. Namun, sebenarnya penggunaan tanda underscore tidak benar-benar membuat property temperature tidak dapat diubah, ia masih dapat diubah. Penggunaan underscore hanyalah _code convention_ yang disepakati oleh komunitas JavaScript.

Untuk membuat nilainya benar-benar tidak dapat diubah, Anda dapat melakukannya dengan cara berikut.

```js
class CoffeeMachine {
  #temperature = 90;

  constructor(waterAmount) {
    this.waterAmount = waterAmount;
    this.#temperature = this.#defaultTemperature();
  }

  set temperature(temperature) {
    console.log('you are not allowed to change the temperature');
  }

  get temperature() {
    return this.#temperature;
  }

  #defaultTemperature() {
    return 90;
  }
}
```

Sejak JavaScript versi ES2022, kita dapat menggunakan tanda hashtag (#) untuk membuat hak akses private pada property dan method. Pada contoh di atas, kita menambahkan tanda hashtag di variable dan method yang bersifat private. Selain itu, kita mendeklarasikan property yang bersifat private di enclosing class seperti berikut.

```js
class CoffeeMachine {
  #temperature = 90; // enclosing class
 
  constructor(waterAmount) {
    this.waterAmount = waterAmount;
    this.#temperature = this.#defaultTemperature();
  }
 
  // Kode lainnya disembunyikan
}
```

Jika mencoba mengakses property yang bersifat private, Anda akan mendapatkan pesan error seperti berikut ini.
![](img/Encapsulation.png)

Seperti itulah konsep encapsulation, membatasi bagian kode yang dapat diakses. Secara default buatlah bagian kode menjadi tidak dapat diakses, jika tidak diperlukan.

