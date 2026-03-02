#programming 
Sebelumnya, kita sudah tahu konsep modularisasi di JavaScript. Anda mungkin sudah tahu juga cara menggunakan impor atau ekspor. Di materi ini, kita akan coba menggunakan module di JavaScript.

### Mengekspor Variable
Misalnya, ada suatu module yang ditulis di berkas module.mjs. Di dalam berkas tersebut, kita akan menulis satu variabel yang akan kita ekspor. Untuk mengekspornya dapat dilakukan seperti berikut.
```js
export const name = 'Dicoding';
```
Selain mengekspor variable yang bertipe string, kita juga dapat mengekspor variable yang bertipe array.
```js
export const favoriteFood = ['pizza', 'pasta', 'sushi'];
```

### Mengekspor Function
Cara untuk mengekspor function tak berbeda jauh dengan cara mengekspor variable.
```js
export function sayHi(name) {
  console.log(`Hi, ${name}!`);
}
```
Agar tidak perlu menulis kata kunci export di setiap nilai yang ingin diekspor, Anda dapat mengekspor di akhir berkas seperti berikut.
```js
const name = 'John';
const favoriteFood = ['pizza', 'pasta', 'sushi'];
 
function sayHi(name) {
  console.log(`Hi, ${name}!`);
}
 
export { name, favoriteFood, sayHi };
```
Nilai yang telah diekspor tersebut siap digunakan di mana pun.


### Mengimpor Variable
Tadi kita sudah mengekspor beberapa nilai dan function di berkas module.mjs. Sekarang, tambahkan berkas baru bernama index.mjs yang akan kita gunakan untuk mengimpor dan menggunakan variable dan function yang telah diekspor sebelumnya.
```js
import { name, favoriteFood } from './module.mjs';
```
Setelah itu, kita dapat mencetak nilainya di Terminal.
```js
console.log(name);
console.log(favoriteFood);
```
Selain mengimpor dengan named import, kita juga dapat mengimpornya menggunakan import alias. Tenang saja, hasilnya akan tetap sama.
```js
import { name, favoriteFood as food } from './module.mjs';
 
console.log(name);
console.log(food);
```

### Mengimpor Function
Untuk mengimpor function dapat dilakukan dengan cara berikut ini.

```js
import { name, favoriteFood as food, sayHi } from './module.mjs';
 
console.log(name);
console.log(food);
sayHi(name);
```
Karena kita mengimpor seluruh nilai yang ada di module tersebut, gunakanlah keyword * agar lebih ringkas.

```js
import * as user from './module.mjs';
 
console.log(user.name);
console.log(user.favoriteFood);
user.sayHi(user.name);
```
Memahami konsep modularisasi dapat membantu Anda untuk membuat program JavaScript yang lebih modular, terstruktur, dan modern. 