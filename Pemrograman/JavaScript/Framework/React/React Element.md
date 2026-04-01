#programming 
Seluruh antarmuka pengguna (UI) aplikasi React dibangun menggunakan React element. Sama seperti DOM element, React element dapat berupa paragraf, heading, atau gambar. React element merepresentasikan apa yang Anda lihat di layar.
![](img/reactelement.png)

Walaupun serupa dengan DOM element, React element dan DOM element browser tidaklah identik. React element hanyalah objek JavaScript polos, ringan, dan sangat mudah untuk dibuat. Cara paling sederhana dalam membuat React element adalah menggunakan fungsi berikut.
```js
React.createElement(
	/* type */, 
	/* property */, 
	/* content */)
	;
```
Fungsi createElement menerima 3 parameter, seperti: 

type yang merupakan tipe elemen, 
property merupakan properti dari elemen, dan
content merupakan konten dari elemen.
Fungsi createElement mengembalikan React element sesuai dengan tipe yang ditetapkan pada parameter. Contoh, bila Anda ingin membuat elemen paragraf “Hello React”, gunakanlah fungsi createElement seperti ini.

```js
const element = React.createElement(
	'p', 
	null, 
	'Hello, React!'
	);
```
Jika Anda telaah nilai kembaliannya (element), React element hanyalah objek JavaScript biasa, seperti ketika kita menuliskan begini:
```js
{
  type: 'p',
  props: {
    children: 'Hello, React!',
  },
}
```
Nilai dari parameter type mendeskripsikan tipe dari React elemen yang akan dikembalikan. React menggunakan referensi [HTML tags](https://developer.mozilla.org/en-US/docs/Web/HTML/Element) untuk menentukan tipe elemen. Jadi, nilai p berarti paragraf, h1 berarti _heading_ tingkat 1, img berati gambar, dan seterusnya.

Lalu, bagaimana bila kita ingin menetapkan properti pada elemen? Pertanyaan bagus! Untuk melakukannya, Anda bisa memanfaatkan parameter kedua (property) dengan memberikan nilai berupa objek yang mendeskripsikan properti elemen yang ingin ditetapkan beserta nilainya. Contoh, bila Anda ingin menetapkan nilai pada properti className atau id, lakukanlah dengan cara seperti di bawah ini.

```js
const element = React.createElement(
  'p',
  {
    id: 'myParagraph',
    className: 'red-paragraph'
  },
  'Hello, React!'
);
```
> **Catatan:** React menggunakan [Element Properties](https://developer.mozilla.org/en-US/docs/Web/API/Element#properties) dalam menetapkan properti pada React element. Itulah mengapa dalam menetapkan class, kita menggunakan className dibandingkan dengan class.  
	  Penting untuk Anda ingat bahwa Element Properties dengan [HTML Attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes) itu berbeda meskipun beberapa nilai properti merepresentasikan nilai dari HTML atribut. React selalu menggunakan Element Properties sebagai referensi.


### Nested React Element
Nilai children pada React element dapat diisi dengan tipe data apa pun, termasuk React element lain. Hal ini sangat wajar dan sering digunakan untuk membangun elemen secara nested.

Jika Anda sudah terbiasa membuat web, tentu Anda sering membuat struktur HTML nested seperti mengelompokkan beberapa element di dalam div.
```html
<div class="container">
  <h1>React</h1>
  <p>The <strong>best tool</strong> for building UI</p>
</div>
```
Ketika menggunakan React, praktik tersebut lazim dan dapat dibuat dengan cara menetapkan nilai parameter child secara nested. Jika child memiliki lebih dari satu nilai, Anda bisa mengelompokkan nilainya di dalam array.
```js
import React from 'react';

const heading = React.createElement('h1', null, 'React');
const strong = React.createElement('strong', null, 'best tool');
const paragraph = React.createElement('p', null, ['The ', strong, ' for building UI']);
const divContainer = React.createElement('div', { className: 'container' }, [heading, paragraph]);

// abaikan kode di bawah ini
export default divContainer;
```

Lihat cara kami menetapkan children untuk elemen paragraph dan divContainer pada kode di atas! Anda bisa lihat bahwa nilai children merupakan array yang berisi beberapa nilai termasuk React element.



