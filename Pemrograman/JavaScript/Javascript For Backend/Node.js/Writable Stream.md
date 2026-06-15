#programming 
Pada materi sebelumnya kita sudah belajar bagaimana membaca berkas menggunakan teknik stream (readable stream). Tapi apakah Anda tahu bahwa teknik stream juga dapat digunakan untuk menulis berkas? Teknik ini disebut _writable stream_.

Untuk membuat writable stream dalam menulis berkas gunakanlah method `createWriteStream()` dari core module `fs`.
```js
import fs from 'fs';
const writableStream = fs.createWriteStream('output.txt');
```

Fungsi ini menerima satu argumen yakni alamat berkas untuk menyimpan hasil data yang dituliskan. Berkas output akan dibuat secara otomatis jika tidak ada, namun bila berkas tersebut sudah ada, maka data sebelumnya akan tertimpa! Anda harus hati-hati yah!

Lalu untuk menuliskan data pada writable stream, gunakan method `write()`.
```js
import fs from 'fs';
const writableStream = fs.createWriteStream('output.txt');
 
writableStream.write('Ini merupakan teks baris pertama!\n');
writableStream.write('Ini merupakan teks baris kedua!\n');
writableStream.end();
```

Method `end()` digunakan untuk menandakan akhir dari writable stream sekaligus bisa digunakan sebagai penulisan writeable terakhir.
```js
import fs from 'fs';
 
const writableStream = fs.createWriteStream('output.txt');
 
writableStream.write('Ini merupakan teks baris pertama!\n');
writableStream.write('Ini merupakan teks baris kedua!\n');
writableStream.end('Akhir dari writable stream!');
```

Kode di atas akan menghasilkan **output.txt** dengan data seperti ini:
```output
Ini merupakan teks baris pertama!
Ini merupakan teks baris kedua!
Akhir dari writable stream!
```