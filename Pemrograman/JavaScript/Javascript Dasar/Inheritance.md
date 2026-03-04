#programming 

Pilar yang akan kita bahas pertama adalah _inheritance_. Inheritance jika diterjemahkan ke dalam bahasa Indonesia artinya adalah pewarisan. Sesuai dengan namanya, kita bisa mewariskan ~~harta~~ property dan method dari sebuah class ke class lain. Umumnya, properti dan method yang diwariskan berasal dari class (induk) dan digunakan oleh class baru (anak). Sama halnya di kehidupan sehari-hari, sedikit banyaknya sebagai anak, kita memperoleh sifat dan perilaku dari orang tua.

Di OOP, inheritance memungkinkan class untuk mewarisi property dan method yang dimilikinya sehingga membantu mengurangi penulisan kode secara berulang (mengurangi redundancy kode). Misalnya, ketika kita membuat sebuah class dengan property dan method, keduanya dapat digunakan kembali oleh class lainnya melalui inheritance. Berikut adalah contohnya.

```js
class SuperClass { }
 
class SubClass extends SuperClass { }
```

Istilah _SuperClass_ dan _SubClass_ akan sering kita dengar ketika bahas inheritance di OOP. Class yang mewariskan property dan method-nya disebut dengan _SuperClass_, Induk, Base, atau _Parent Class_. Class yang mewarisi property dan method dari class lain disebut dengan SubClass dan Children Class (Anak).

Misalnya, Anda memiliki smartphones dengan jenis Android dan iOS, setiap smartphones tersebut pasti memiliki property color, brand, model, dan method-nya adalah charging. Dengan paradigma OOP, property dan method yang memiliki kesamaan bisa kita abstraksikan menjadi sebuah class baru bernama Smartphones. Kemudian kita bisa membuat dua class baru, yaitu Android dan iOS.

![](img/inheritance.png)

Android dan iOS akan mewariskan property dan method dari class Smartphones seperti yang ada pada gambar di atas. Dengan begitu, class Android dan iOS akan memiliki property color, brand, model dan method charging. Selain itu, di masing-masing class kita dapat menambahkan property yang hanya ada pada dirinya. Misalkan, class Android memungkinkan untuk memiliki method split screen, sedangkan class iOS memungkinkan untuk memiliki method AirDrop.
![](img/inheritance2.png)

Jika contoh di atas kita terapkan pada kode JavaScript, kodenya akan menjadi seperti berikut ini.

```js
class SmartPhones {
  constructor(color, brand, model) {
    this.color = color;
    this.brand = brand;
    this.model = model;
  }

  charging() {
    console.log(`Charging ${this.model}`);
  }
}

class iOS extends SmartPhones {
  airDrop() {
    console.log('iOS have a behavior AirDrop');
  }
}

class Android extends SmartPhones {
  splitScreen() {
    console.log('Android have a Split Screen');
  }
}

const ios = new iOS('black', 'A', '12 Pro Max');
const android = new Android('white', 'B', 'Galaxy S21');

ios.charging(); // Output: Charging 12 Pro Max
ios.airDrop(); // Output: iOS have a behavior AirDrop

android.charging(); // Output: Charging Galaxy S21
android.splitScreen(); // Output: Android have a Split Screen
```

Di implementasi kode, SubClass (`Android`, `iOS`) hanya mendefinisikan method yang hanya ada pada dirinya. Selain itu, kita tetap dapat mengakses property dan method yang ada pada SuperClass (`color`, `brand`, `model`, `charging`) sehingga mengurangi penulisan kode yang berulang.

