#programming 

**Export** adalah keyword yang kita gunakan untuk melabeli suatu function/method/variable agar dapat diakses dari luar modul saat ini. Export terdiri dari dua jenis, yaitu **default export** dan **named export**. Perhatikan contoh named export berikut ini.
```js
export const name = 'John';
export const email = 'john@gmail.com';
export const age = 25;
```
Cara tersebut merupakan cara export sebelum deklarasi dilakukan. 

Cara lainnya adalah export setelah deklarasi dilakukan seperti berikut ini.
```js
const name = 'John';
const email = 'john@gmail.com';
const age = 25;
 
export { name, email, age };
```
Hasilnya akan tetap sama. Variable yang sudah diekspor (name, email, dan age) dapat digunakan di module lainnya.

Cara mengimpor named export adalah dengan menuliskan nilainya di dalam sebuah kurung kurawal. Perhatikan contoh berikut ini.
```js
import { name, email, age } from './user.mjs';
 
console.log(name, email, age);
```
Variable name, email, dan age akan diimpor dengan named import (yang sudah kita bahas di materi sebelumnya) sebelum digunakan. 

Terakhir, ada teknik yang disebut dengan **default export**. Default export adalah cara kita untuk mengekspor minimal satu function/method/variable di sebuah modul. Dengan menggunakan default export, modul lain yang ingin menggunakan nilainya tidak perlu tahu spesifik namanya karena secara default sudah ada function/method/variable yang diekspor. Perhatikan contoh berikut ini.

anotherfile.mjs:
```js
export default function goodMorning () {
  console.log('Good morning!')
}
```
main.mjs:
```js
import goodMorning from './anotherfile.mjs';
import anotherName from './anotherfile.mjs';

goodMorning();
anotherName();
```
Output:
```output
Good morning! 
Good morning!
```

