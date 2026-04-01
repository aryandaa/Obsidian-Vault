#programming 
Ada dua pendekatan berbeda dalam melampirkan berkas styling di proyek React. Sama seperti gambar, kita bisa memperlakukannya seperti berkas statis dengan menyimpannya di dalam folder _public_ atau kita bisa memperlakukannya sebagai module yang diimpor di dalam kode JavaScript. Di latihan kali ini, kita akan mencoba kedua pendekatan tersebut sehingga Anda bisa mengetahui perbedaannya.

> **Catatan:** Latihan ini fokus terhadap tujuan “Bagaimana melampirkan/menggunakan berkas CSS pada proyek React”, bukan pada sintaksis CSS-nya. Jadi, kami tidak akan menjelaskan kode CSS yang kami berikan karena seharusnya Anda sudah mempelajarinya sebelum mengikuti kelas ini.

1. Kita akan coba cara pertama yaitu memperlakukan berkas CSS sebagai berkas statis. Silakan buat berkas CSS baru bernama _style.css_ di dalam folder _public_.

2. Kemudian tuliskan kode CSS berikut.
```css
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}
 
body {
  font-family: 'Inter', sans-serif;
  background-color: whitesmoke;
}
 
img {
  width: 100%;
}
 
.contact-app {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
 
}
 
.contact-app  h1 {
  font-weight: normal;
  font-size: 48px;
  margin-bottom: 32px;
}
 
.contact-item {
  display: flex;
  align-items: center;
  margin: 24px 0;
  border: 1px dashed black;
  padding: 16px;
  border-radius: 8px;
}
 
.contact-item__image img {
  width: 64px;
  border-radius: 50%;
}
 
.contact-item__body {
  margin-left: 8px;
  padding-left: 8px;
  border-left: 1px solid #aaa;
  flex: 1;
}
 
.contact-item__title {
  padding: 4px 0;
}
 
.contact-item__username {
  font-weight: lighter;
}
 
.contact-item__delete {
  padding: 8px;
  font-size: 18px;
  background-color: orangered;
  color: white;
  border: 0;
  border-radius: 4px;
  cursor: pointer;
}
 
.contact-input {
  border: 1px dashed black;
  padding: 16px;
  margin: 14px 0;
  border-radius: 8px;
  margin-bottom: 32px;
}
 
.contact-input input {
  display: block;
  width: 100%;
  padding: 8px;
  margin: 8px 0;
  font-family: 'Inter', sans-serif;
}
 
.contact-input button {
  width: 100%;
  padding: 8px;
  font-family: 'Inter', sans-serif;
}
```

3. Kemudian buka berkas index.html dan tambahkan elemen link di dalam elemen head untuk menghubungkan berkas CSS dengan HTML.
```html
<link rel="stylesheet" href="style.css">
```

Anda juga bisa menambahkan external CSS (sebelum style.css), misalnya dari Google Font karena di proyek ini kami menggunakan font “Inter” yang tersedia di Google Font.

```html
 <!-- START: Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin> 
<link href="https://fonts.googleapis.com/css2family=Inter:wght@300;400;700&display=swap" rel="stylesheet">
<!-- END: Google Font -->
```

4. Simpan seluruh perubahan dan lihat kembali Browser Anda. Seharusnya aplikasi sudah berhasil menerapkan styling.

5. Sekarang mari kita coba cara yang kedua yaitu memperlakukn berkas CSS sebagai module di berkas JavaScript.

Agar dapat diimpor oleh berkas JavaScript, silakan pindahkan berkas style.css ke dalam folder src.

6. Kemudian hapus juga penggunaan elemen link yang menghubungkan style.css pada index.html karena sudah tidak relevan lagi (tidak berada di folder public lagi).

7. Coba simpan dulu seluruh perubahan dan pastikan aplikasi kembali menampilkan UI tanpa _styling_.

8. Kemudian, buka berkas _index.jsx_ dan impor berkas _style.css_ seperti ini.
```jsx
import React from 'react';
import { createRoot } from 'react-dom/client';
import ContactApp from './ContactApp';
 
// styling
import './style.css';
 
const root = createRoot(document.getElementById('root'));
root.render(<ContactApp />);
```

Simpan perubahan kode dan lihat kembali hasilnya pada Browser. Seharusnya styling berhasil diterapkan kembali.

Selamat! Anda berhasil menerapkan styling dengan teknik modularisasi. Teknik ini cocok ketika Anda ingin memisahkan styling menjadi beberapa berkas css terpisah dan mengimpornya pada component yang spesifik. Dengan begitu, berkas styling dapat lebih mudah dikelola, terlebih bila proyek yang Anda buat semakin besar nantinya.

9. Karena sekarang di dalam folder src sudah mulai banyak berkas, Anda bisa mulai mengelompokkan berkas-berkas berdasarkan jenisnya. Misal, jika seluruh berkas JavaScript yang merupakan component, simpanlah di folder baru bernama components. Anda juga bisa mengelompokkan berkas CSS (walaupun saat ini hanya satu) pada folder terpisah, misalnya styles.
![](img/Pasted%20image%2020260322195011.png)

Bila sudah dikelompokkan pada folder terpisah, jangan lupa juga untuk memperbaiki beberapa path (alamat berkas) yang berubah pada saat melakukan impor di berkas index.jsx dan ContactApp.js.

tapi dengan react versi terbaru, kita tidak perlu lagi mengubah path nya secara manual, jika kita memindah file ke folder tertentu, nama import nya juga akan mengikuti letak file itu.