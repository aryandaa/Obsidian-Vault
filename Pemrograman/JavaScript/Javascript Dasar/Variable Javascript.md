#programming 
Variabel di JavaScript dapat dibuat dengan menggunakan keyword **let** dan **const**.
```Javascript
let name = "Dicoding";   
```
Kode ini merupakan cara mendeklarasikan variabel, atau disebut dengan declaration statement.
di dalam variable nama tersebut berisi data "Dicoding", yang bisa kita panggil nanti dengan cara:
```Js
let name = "Dicoding";
console.log(name);
```
ketahuilah bahwa variabel yang dibuat menggunakan keyword let, dapat diubah nilainya. Contoh, saya akan mengubah nilai name ini menjadi “Dicoding Academy”. Caranya dengan memberikan nilai baru pada variabel name.
```js
let name = "Dicoding";
name = "Dicoding Academy";
console.log(name);
```


Dan ini hal yang tidak bisa dilakukan ketika Anda membuat variabel dengan menggunakan const. Variabel yang dibuat dengan keyword const bersifat konstan atau tidak bisa diubah nilainya.

```js
const score = 1000;
console.log(score);
```

Sejauh ini, variabel terlihat normal. Namun, bila kita mengubah nilai score, maka akan terjadi error.

```js
const score = 1000;
score = 500; 
console.log(score);
```


Ada hal lain yang penting untuk Anda ketahui ketika membuat sebuah nama variabel:
- Hindari penamaan variabel dengan istilah umum contohnya data. Penamaan data tidak menjelaskan apa pun. Nama tersebut akan membuat Anda bingung kelak. Sebaiknya gunakan nama yang dapat mendeskripsikan nilai dari variabel itu sendiri.
- Variabel di JavaScript hanya dapat dimulai dengan huruf atau tanda underscore. Anda tidak bisa membuat variabel dengan awalan angka atau menggunakan simbol selain underscore.
- Nama variabel tidak boleh mengandung spasi. Jika nama variabel memiliki lebih dari dua kata, maka gunakan format camelCase seperti ini:  
    firstName, lastName, catName.
- Tidak boleh mengandung karakter spesial (!.,/\+*= dan lainnya).