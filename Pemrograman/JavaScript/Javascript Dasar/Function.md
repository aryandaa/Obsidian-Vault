#programming 

Fungsi atau function merupakan bagian penting dalam bahasa pemrograman. Tanpa sadar, sebenarnya kita sudah menggunakan sebuah fungsi pada contoh kode yang ada sebelumnya. Seperti, console.log() merupakan function yang berguna untuk menampilkan data pada konsol dan juga fungsi typeof yang digunakan untuk memeriksa tipe data variabel. 

Namun, apa sebenarnya function itu? Bagaimana ia bisa bekerja? Mari kita lihat contoh kodenya.
```Js
function Greeting(){
	Console.log("hello world");
}

Greeting();
```

Kode di atas merupakan sebuah fungsi di JavaScript, fungsi ini berguna untuk menampilkan pesan hello world pada konsol.

diatas itu contoh function statis, yang artinya data yang berada di dalam function tidak bisa kita modifikasi, nah bagaimana caranya membuat agar function bersifat dinamis? tambahkan parameter di dalam kurung function tersebut.

```js
function greeting(greet) {
   console.log("Selamat " + greet + "!");
}

greeting('malam'); // Selamat malam!
greeting('pagi'); // Selamat pagi!
```

Dengan begini, ketika fungsi dipanggil dengan teks “malam”, ia akan mencetak teks “Selamat Malam”. Begitu juga bila kita memanggil dengan memberikan nilai “pagi”, maka ia akan mencetak teks “Selamat Pagi”.

Kita juga bisa memberikan lebih dari satu parameter fungsi bila memang dibutuhkan. Misalkan, pada fungsi greeting, selain parameter greet, kita bisa menambahkan parameter name agar fungsi dapat menyapa nama kita.

```js
function greeting(greet, name) {
   console.log("Selamat " + greet + ", " + name + "!");
}

greeting("sore", "Dimas"); // Selamat sore, Dimas!
greeting("pagi", "Yasmin"); // Selamat pagi, Yasmin!
```


Kemudian, parameter fungsi di JavaScript juga bisa diberikan nilai default. Nilai default merupakan nilai yang digunakan bila parameter fungsi tidak diberi nilai ketika dipanggil.

Misal, saat ini fungsi greeting dapat menerima dua parameter, yang pertama greet dan yang kedua name.

```js
function greeting(greet, name = "Bapak/Ibu") {
  console.log("Selamat " + greet + ", " + name + "!");
}
 
greeting("sore", "Dimas"); // Selamat sore, Dimas!
greeting("pagi"); // Selamat pagi, Bapak/Ibu!
```
Nah, dengan begitu, bila kita hanya memberikan nilai parameter greet tanpa name, fungsi greeting akan mencetak “Selamat Malam, Bapak/Ibu”.

Hal ini dikarenakan kita memberikan teks “Bapak/Ibu” sebagai nilai default.


Berikut beberapa tips dalam membuat sebuah fungsi di JavaScript.

- **Hindari membuat parameter yang banyak**  
    Memberikan batasan pada jumlah parameter fungsi merupakan hal yang sangat penting. Fungsi dengan parameter yang terlalu banyak akan sulit untuk diuji ataupun digunakan. Karena kita perlu banyak sekali nilai untuk menggunakan sebuah fungsi.  
      
    Satu atau dua argumen merupakan jumlah yang ideal. Bagaimana dengan tiga? Sebaiknya hindari jika memungkinkan. Jika lebih dari itu? Tentu perlu dikonsolidasikan. Biasanya jika fungsi memiliki lebih dari dua parameter, pasti fungsi tersebut terlalu rumit. Namun, bagaimana jika fungsi tersebut simpel, namun tetap membutuhkan argumen yang banyak?  
      
    Alih-alih membuat parameter fungsi yang banyak, manfaatkanlah objek sebagai parameter. Ketahuilah bahwa di JavaScript kita dapat membuat sebuah objek dengan mudah. Kita tidak akan membahas objek di sini, namun bila Anda mendalami JavaScript nantinya, Anda akan mengetahui apa itu objek.  
     
- **Melakukan satu hal**  
    Hal inilah yang paling penting untuk diperhatikan bila membuat sebuah fungsi. Jika fungsi yang kita buat melakukan banyak hal, maka fungsi tersebut akan sulit untuk disusun dan diuji. Fungsi yang melakukan banyak hal juga pasti tidak memiliki tujuan yang jelas.  
      
    Ketika membuat fungsi yang melakukan lebih dari satu hal, cobalah untuk memecah fungsinya. Hingga tiap fungsi benar-benar melakukan satu hal. Tentu ini juga membuat kode pada fungsi jauh lebih bersih dan mudah dibaca.  
    
- **Nama fungsi harus merepresentasikan tujuannya**  
    Tak hanya variabel, kita juga perlu memperhatikan penamaan pada fungsi. Pastikan nama yang diberikan merepresentasi tujuan atau tugas dari fungsi tersebut. Hal ini juga bisa membantu developer lain mudah untuk mengetahui tujuan dari fungsi yang Anda buat.  
    
- **Buatlah fungsi untuk menghindari duplikasi kode**  
    Bila Anda merasa sering menuliskan kode yang berulang-ulang. Sebaiknya perhatikan kode tersebut. Karena kode yang berulang menjadi kandidat kuat untuk dibuatkan sebuah fungsi. Tujuannya tidak lain agar kode tersebut dapat digunakan ulang, hanya dengan memanggil sebuah fungsi.