#programming 
Sejauh ini, kita telah mengetahui bagaimana ._createElement()_ dan JSX dapat membantu kita dalam membuat React element yang ditampilkan pada Browser dengan bantuan React DOM. Selain React element, fitur utama lainnya yang sangat membantu kita dalam membangun UI adalah React Component. Fitur ini adalah kunci jika Anda ingin membangun UI yang reusable dan terisolasi.

Mudahnya, React component merupakan fungsi JavaScript yang mengembalikan React element. Alasan mengapa kita membuat React component sama dengan kapan kita harus membuat sebuah fungsi. Namun, alih-alih mengembalikan data, React component mengembalikan UI dalam bentuk React element.

Terdapat 2 alasan mengapa Anda perlu membuat component.

1. Pembuatan UI (React element) membutuhkan logika yang tidak sederhana, serta Anda ingin proses pembuatan UI tersebut terisolasi. Dengan begitu, kode dalam membuat UI tersebut tidak mengganggu kode lainnya.
2. Anda ingin membuat UI yang bersifat reusable. Artinya, hanya dengan satu kode UI namun dapat digunakan sebanyak apa pun dengan banyak varian data.

“_Components let you split the UI into independent, reusable pieces, and think about each piece in isolation._”  
- React Team

Konsep component sangat ciamik karena kita dapat memecah (break down) UI ke bagian-bagian kecil. Bagian-bagian kecil dari UI tersebut memiliki tanggung jawab yang jelas dan properti yang sudah terdefinisikan. Hal ini sangat penting ketika membangun aplikasi yang besar karena kita dapat bekerja fokus pada bagian terkecil dari aplikasi tanpa mengganggu keseluruhan kode yang ada.

Cara paling sederhana dalam membuat React component adalah menulis fungsi yang mengembalikan React element (dapat menggunakan JSX atau createElement).
```jsx
function SayHello() {
  // Sebelum mengembalikan React element, Anda bisa menuliskan banyak kode JavaScript di sini.
  // Biasanya kode yang dituliskan seputar persiapan data untuk ditampilkan pada React element.
 
  return <p>Hello, World!</p>
}
```

>**Catatan**: Konvensi dalam penamaan React component selalu diawali dengan huruf kapital. Hal ini bertujuan agar dapat membedakan antara built-in HTML element dan component yang Anda (atau pihak lain) buat sendiri.

React component dapat digunakan dengan cara yang berbeda dari fungsi biasa, yakni menggunakan sintaksis JSX seperti ini.
```jsx
<SayHello /> // akan menampilkan ui <p>Hello, World!</p>
```

Layaknya sebuah fungsi, ia dapat digunakan sebanyak yang Anda mau.
```jsx
<SayHello /> // akan menampilkan ui <p>Hello, World!</p>
<SayHello /> // akan menampilkan ui <p>Hello, World!</p>
<SayHello /> // akan menampilkan ui <p>Hello, World!</p>
<SayHello /> // akan menampilkan ui <p>Hello, World!</p>
```

**PERINGATAN**  
Perlu kalian ingat! Meskipun React component adalah fungsi JavaScript, tetapi ia harus diperlakukan (digunakan) layaknya sebuah component. Sebuah fungsi yang mengembalikan React element belum bisa dikatakan component bila Anda memanggilnya seperti ini.

```jsx
SayHello(); // wrong practice!!
```
