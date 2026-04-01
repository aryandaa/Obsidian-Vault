#programming 
“Kok membuat React elemen lebih sulit ya dibandingkan membuat HTML biasa?” - Anda mungkin berpikir demikian setelah melihat kode yang ada di materi _Nested React Element_ yang kami berikan. _Yup_! Memang tidak salah. Membuat React element terasa sulit bila menggunakan fungsi createElement, terlebih bila elemen yang kita buat _nested_ seperti contoh sebelumnya. React sendiri menganut konsep deklaratif, tetapi penggunaan createElement terasa sangat imperatif, hampir tak ada bedanya dengan fungsi standar _document.createElement_.

Tenang, React punya solusinya. Selain menggunakan fungsi createElement, Anda juga bisa membuat element dengan sintaksis JSX. Dengan JSX, pembuatan elemen jauh lebih mudah dan bersifat deklaratif.

Berikut adalah contoh dari sintaksis JSX:
```jsx
const element = <p>Hello, React!</p>;
```

Sintaksis “unik” di atas bukanlah string ataupun HTML [4]. Sintaksis tersebut dinamakan JSX karena extensions (penambahan) dari kemampuan standar JavaScript yang diberikan oleh React. Intinya, ketika menggunakan React, Anda bisa menuliskan sintaksis unik tersebut di JavaScript.

Sintaksis JSX mengembalikan React element sesuai dengan yang Anda deklarasikan. Sintaksis JSX mirip seperti HTML karena memanfaatkan tag--khas gaya markup--dalam mendeklarasikan elemen. Dengan menggunakan JSX, Anda bisa terbebas dari menggunakan fungsi createElement dalam membuat element.

begini jika menggunakan JSX:
```jsx
const element = <p className="red-paragraph">Hello, React!</p>;
```
lebih simple dan deklaratif daripada createElement native yang seperti ini
```js
const element = React.createElement(
  'p',
  {
    className: 'red-paragraph',
  },
  'Hello, React!',
);
```

> **Catatan:** Properti elemen pada JSX dituliskan mirip atribut pada HTML. Namun, referensinya tetap mengacu pada standar Element Properties, bukan HTML Attributes.

Kami bilang JSX mirip HTML bukan berarti keduanya adalah sama. Perbedaannya adalah di JSX, Anda bisa menuliskan _JavaScript expression_ ketika membuat elemen. Karena JSX memang dituliskan pada lingkup JavaScript. Caranya, tuliskan expression di antara tanda kurung kurawal { }. 

Berikut contoh penulisan expression di JSX.
```jsx
const name = 'Dicoding';
const element = <p>Hello, {name}</p>;
```

Variabel element akan bernilai sama dengan:
```js
{
  type: 'p',
  props: {
    children: ['Hello, ', 'Dicoding']
  }
}
```

Terakhir, JSX menyapu kerumitan pembuatan _nested_ _element_ yang dilakukan dengan fungsi **createElement**. Pasalnya, dengan gaya deklaratif yang ia miliki, kita bisa lebih mudah melakukan nested element layaknya menuliskan sintaksis HTML biasa.

Lihat perbedaan antara JSX dan createElement.
```jsx
const divContainer = (
  <div className="container">
    <h1>React</h1>
    <p>The <strong>best tool</strong> for building UI</p>
  </div>
);
```
>**Catatan:** Penggunaan tanda kurung () yang menghimpit sintaksis JSX **tidak berarti apa-apa**. Hal itu hanyalah _convention_ ketika Anda menuliskan sintaksis JSX pada baris baru. Tujuannya, agar sintaksis JSX lebih rapi dan mudah dibaca.

sedangkan createElement:
```js
const heading = React.createElement('h1', null, 'React');
const strong = React.createElement('strong', null, 'best tool');
const paragraph = React.createElement('p', null, ['The ', strong, ' for building UI'])
const divContainer = React.createElement('div', { className: 'container' }, [heading, paragraph]);
```


### JSX hanya mengembalikan satu element

Ketika menuliskan JSX, pastikan ia hanya mengembalikan satu elemen. Meskipun React element bisa _nested_, tapi pastikan **hanya ada satu root element** yang membungkus seluruh element di dalamnya.
```jsx
const element = (
  <div className="container">
    <h1>React</h1>
    <p>
      The <strong>best tool</strong> for building UI
    </p>
  </div>
);
```

Lihat kode JSX di atas! Ia hanya mengembalikan satu root elemen yaitu `<div>`, walaupun di dalamnya kami menuliskan lebih dari satu elemen. Inilah **cara yang benar** jika Anda ingin membuat banyak element menggunakan JSX. Agar lebih jelas lagi, berikut adalah contoh **praktik yang salah** dalam penggunaan JSX.

```jsx
const element = (
  <h1>React</h1>
  <p>The <strong>best tool</strong> for building UI</p>
);
```

Pada contoh di atas, kami menuliskan dua root element yaitu `<h1>` dan `<p>`. Sintaksis JSX seperti ini tidak benar dan dianggap sebagai syntax error.

Karena Anda sudah mengetahui penggunaan fungsi createElement() maka aturan ini tentu masuk akal. Karena fungsi createElement() pun hanya menerima satu tag (dalam bentuk string) pada parameter pertama.

  
### Ekstensi .jsx pada berkas JavaScript

Ketika kita menulis kode JSX pada berkas JavaScript, kami sarankan gunakanlah ekstensi **.jsx** alih-alih **.js**. Tujuannya agar Anda dapat lebih mudah dalam membedakan berkas yang ditulis dengan kode JavaScript standar dan berkas yang memanfaatkan sintaks JSX.

Meskipun sintaks JSX dapat ditulis dalam berkas berekstensi .js, tetapi penggunaan ekstensi .jsx memiliki beberapa keuntungan, antara lain:

1. Beberapa IDE atau teks editor akan membantu memvalidasi sintaks JSX.
2. Alat transpilasi kode seperti Babel akan bekerja lebih optimal dalam menerjemahkan sintaks JSX ketika Anda menggunakan ekstensi .jsx dalam penamaan berkas JavaScript.

**Ingat!** Ekstensi .jsx hanya digunakan ketika pada berkas tersebut terdapat sintaks JSX. Tetap gunakan ekstensi .js jika hanya menulis sintaks JavaScript standar.

Simak bahan bacaan lebih lanjut terkait JSX pada: 

- [Mengenal JSX](https://reactjs.org/docs/introducing-jsx.html) (Dokumentasi lama).
- [Menulis Markup dengan JSX](https://react.dev/learn/writing-markup-with-jsx) (Dokumentasi baru).