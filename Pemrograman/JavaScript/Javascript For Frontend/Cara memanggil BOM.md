#programming 
Ketika kalian ingat akan peraturan sintaks JavaScript, bukankah memanggil properti atau sebuah _method_ dari suatu objek perlu menyertakan nama objek dan diikuti oleh nama properti atau functionnya? Hal ini benar dan berlaku untuk BOM yang diwakili oleh object `window` pada _environment browser_. Supaya lebih tergambarkan, perhatikan dua baris kode ini.
```js
// Cara pertama
window.alert('Hello World');
 
// Cara kedua
alert('Hello World');
```

Kedua cara di atas tidak memiliki perbedaan dan valid, yang mana cara pertama secara eksplisit memerintah kode JavaScript untuk memanggil method `alert()` milik objek _window_. Namun, cara yang kedua tidak menyebutkan objek window untuk menampilkan alert. Lalu, mengapa cara kedua tetap bisa dilakukan? Hal ini karena properti dan method yang dimiliki `window` bersifat global.

Walau cara kedua terkesan lebih singkat, kita harus tetap hati-hati karena jika pada _scope_ sebuah berkas .js terdapat nama fungsi yang sama, maka pesan pada pop-up tidak akan muncul. Contohnya berikut.

```js
function alert(nama) {
  console.log('Hati-hati, ' + nama);
}
 
alert('Chewbacca'); // Output: Hati-hati, Chewbacca
// Output di atas akan tercetak ke console browser
 
window.alert('Chewbacca'); // Output: Hati-hati, Chewbacca
// Output di atas akan tetap tercetak pada console browser
```

> **Catatan:**  
> Sebetulnya, interactive code di atas akan memunculkan alert browser jika menjalankan `window.alert()`. Padahal, seharusnya tidak ada alert browser muncul karena tergantikan dengan function alert yang terbuat. Oleh karena itu, Anda dapat mencobanya secara mandiri di browser untuk membuktikannya dengan benar.

Jadi, harap hati-hati jika kita mendefinisikan sebuah _method_ dengan nama yang sama dengan _method_ milik `window`.