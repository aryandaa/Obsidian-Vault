#programming 

Sepandai-pandainya tupai melompat, akan jatuh juga. Sebaik apa pun kita menulis program, suatu saat akan terjadi error. Error yang terjadi bisa berasal dari expected error (error yang terduga) dan unexpected error (error yang tidak terduga). 

Error yang dibiarkan dan tidak ditangani akan menyebabkan crash pada program yang dibangun. JavaScript memiliki cara untuk menangani error tersebut yang disebut dengan error handling. Error handling dapat mencegah crash pada program ketika terjadi error yang disebabkan oleh kesalahan syntax atau error lainnya.

### Throwing Error

Saat terjadi error, sinyal yang disebut dengan exception akan bangkit. Cara lain untuk membuat exception adalah menggunakan keyword throw untuk _generate_ sebuah error. Sintaks dasarnya adalah seperti berikut.
```js
throw <objek error>
```

JavaScript memiliki built-in constructor untuk standar error meliputi Error, SyntaxError, dan sebagainya.  Perhatikan contoh berikut ini.

```js
const error = new Error('Terjadi error');
console.error(error);
```
```output
Error: 
Terjadi error at Object.<anonymous> 
(/home/glot/main.js:1:15) at Module._compile (node:internal/modules/cjs/loader:1358:14) at Module._extensions..js (node:internal/modules/cjs/loader:1416:10) at Module.load (node:internal/modules/cjs/loader:1208:32) at Module._load (node:internal/modules/cjs/loader:1024:12) at Function.executeUserEntryPoint [as runMain] (node:internal/modules/run_main:174:12) at node:internal/main/run_main_module:28:49
```
Pada contoh di atas, kita menggunakan built-in constructor milik JavaScript, _Error_. Kenapa kita perlu membangkitkan exception secara sengaja? Jawabannya adalah karena kita ingin program yang dibangun tidak mengalami crash ketika terjadi sesuatu di luar dugaan.

Misalnya, kita memiliki program yang menerima inputan pembayaran dari pembeli. Normalnya adalah jumlah yang dibayarkan harus lebih besar dari harga barang. Lalu, ada sebuah kasus dimana pembeli membayar lebih kecil dari harga barang. Hal ini akan menyebabkan error di program milik kita. Oleh karena itu, kita perlu throw error ketika pembayaran kurang dari harga barang seperti contoh berikut.
```js
const price = 100;
const paid = 80;

if (paid < price) {
  throw new Error('Pembayaran kurang');
}
```
Contoh di atas akan membangkitkan error. Lalu, bagaimana caranya untuk menangani error yang telah dibangkitkan? Caranya adalah menggunakan konsep Catching Error.

### Catching Error

Sebelumnya, Anda sudah tahu cara untuk membangkitkan error. Kini, saatnya Anda mengetahui cara untuk menangkap error yang dihasilkan oleh program JavaScript yang Anda tulis.

#### Try-Catch
Try-catch merupakan cara yang dimiliki JavaScript untuk menangani error. Try-catch memiliki dua blok utama yaitu try dan catch. Try merupakan blok kode yang akan menangani error, sedangkan catch merupakan blok kode yang dibangkitkan ketika terjadi error di dalam blok try. Perhatikan struktur dari try-catch berikut.
```js
try {
 
  // code...
 
} catch (err) {
 
  // error handling
 
}
```

Blok kode catch akan diabaikan ketika tidak ada error yang terjadi di dalam blok try. Oleh karena itu, tulislah kode yang berpotensi error di dalam blok try. Perhatikan contoh berikut ini.
```js
try {
  console.log('Memulai program');
  throw new Error('Error: Program berhenti');
  console.log('Mengakhiri program');
} catch (err) {
  console.log('Karena ada error, blok ini akan dieksekusi');
}
```

**Catatan**  
Ketika error dibangkitkan, kode yang ada di bawahnya tidak akan tereksekusi. Pada kasus ini, program akan langsung lompat ke blok catch.

![](img/try%20catch.png)

#### Finally
Finally adalah blok kode yang berada di akhir try-catch. Bilamana catch dieksekusi hanya ketika ada error di dalam blok try, blok yang ada di finally akan selalu dieksekusi. Simak contoh di bawah ini.
```js
try {
  console.log('Ini try block');
} catch (err) {
  console.log('Ini catch block');
} finally {
  console.log('Ini finally block');
}
```

Ketika dijalankan, akan tampil di terminal/console yang mencetak tulisan “Ini try block“ dan “Ini finally block”. Dengan menggunakan finally, ia tidak peduli apakah blok try memiliki error atau tidak. 

