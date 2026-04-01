#programming 
Pada latihan sebelumnya, Anda sudah berhasil membuat proyek React (contacts-app) secara lokal. Sekarang, kita akan melanjutkan pembuatan aplikasi daftar kontak sesuai rencana awal. Latihan ini bertujuan untuk meningkatkan “jam terbang” Anda dalam menggunakan React.

Kita akan membangun aplikasi secara bertahap. Di akhir dari modul ini setidaknya Anda akan berhasil menampilkan daftar kontak sederhana seperti ini.
![](img/Pasted%20image%2020260322180709.png)

Mengingat Anda sudah banyak berlatihan di materi sebelumnya, seharusnya latihan kali ini akan mudah. Jadi, mari kita mulai!

1. Pertama, silakan unduh dulu beberapa aset gambar yang diperlukan pada aplikasi di tautan berikut: [images.zip](https://github.com/dicodingacademy/a403-react-pemula-labs/raw/099-shared-files/01-materials/images.zip)  

2. Selanjutnya pada proyek contacts-app, buat folder baru bernama _images_ di dalam folder _public_.

3. Kemudian, ekstrak berkas ZIP yang telah diunduh pada langkah pertama. Setelah itu, simpan seluruh gambar di dalam folder public - images.

4. Seperti biasa, sebelum kita mulai menulis kode ada baiknya buatlah sketsa untuk menentukan pemecahan component yang akan dibuat.
![](img/Pasted%20image%2020260322181736.png)
Berikut adalah pemecahan dari component-nya. 
ContactApp (merah) : Sebagai parent yang menampung seluruh UI yang ditampilkan, termasuk lokasi di mana data contacts berada.

ContactList (kuning) : Sebagai container dalam membuat list contact.

ContactItem (hijau) : Sebagai container dalam menampilkan item contact.

ContactItemImage (biru) : Menampilkan gambar contact.

ContactItemBody (ungu) : Menampilkan data nama dan tag sosial media dari kontak.


5. Sebelum membuat component satu per satu, siapkan dulu data yang hendak ditampilkan pada berkas JavaScript terpisah. Buatlah berkas JavaScript baru bernama _data.js_ dan tuliskan kode berikut.
```js
const getData = () => {
 return [
   {
     id: 1,
     name: 'Dimas Saputra',
     tag: 'dimasmds',
     imageUrl: '/images/dimasmds.jpeg',
   },
   {
     id: 2,
     name: 'Arif Faizin',
     tag: 'arifaizin',
     imageUrl: '/images/arifaizin.jpeg',
   },
   {
     id: 3,
     name: 'Rahmat Fajri',
     tag: 'rfajri27',
     imageUrl: '/images/rfajri27.jpeg',
   },
 ];
}
 
export { getData };
```
Proyek kali ini kita akan menerapkan teknik modularisasi. Tujuannya tidak lain untuk memudahkan kita dalam mengelola kode JavaScript. Dengan memisahkan kode ke berkas yang berbeda, diharapkan tak ada lagi kode JavaScript yang panjang dalam satu berkas. Percayalah, teknik modularisasi sangat memudahkan Anda ke depannya.Tak hanya data, teknik modularisasi juga akan diterapkan dalam pembuatan component. Jadi, setiap satu component kita tulis dalam satu berkas JavaScript terpisah.

6. Kita mulai dengan component yang paling sederhana dulu, yakni `ContactItemBody` dan `ContactItemImage`. Mengapa? Karena kedua component tersebut tidak membutuhkan component lain yang harus dibuat terlebih dulu.
```jsx
import React from 'react';
 
function ContactItemBody({ name, tag }) {
 return (
   <div className="contact-item__body">
     <h3 className="contact-item__title">{name}</h3>
     <p className="contact-item__username">@{tag}</p>
   </div>
 );
}
 
export default ContactItemBody;
```
Kita perlu memperhatikan nilai class pada React element karena nantinya class ini akan digunakan sebagai selector ketika menerapkan styling dengan CSS. Dalam memberikan nilai class, kami mencoba mengikuti gaya konvensi BEM (Block Element Modifier). Jika Anda lihat, penamaan class yang diberikan terlihat mudah dipahami dan dibaca bukan?Selain itu, jangan lupa untuk selalu mengekspor component menggunakan export default setiap akhir pembuatan component pada berkas JavaScript. Hal tersebut dilakukan supaya component dapat digunakan dan dikomposisikan oleh component lain di berkas JavaScript yang berbeda.

7. Kita lanjut membuat component yang kedua yaitu `ContactItemImage`.
```jsx
import React from 'react';
 
function ContactItemImage({ imageUrl }) {
 return (
   <div className="contact-item__image">
     <img src={imageUrl} alt="contact avatar"/>
   </div>
 );
}
 
export default ContactItemImage;
```

8. Setelah komponen ContactItemBody dan ContactItemImage selesai, buatlah component ContactItem sebagai induk (parent) dari kedua komponen tersebut. Silakan buat berkas JavaScript bernama ContactItem.jsx di dalam src.

Karena komponen ContactItemBody dan ContactItemImage akan digunakan di dalam komponen ini, pastikan Anda telah menyediakan data untuk kedua komponen tersebut melalui properti.

```jsx
import React from 'react';
import ContactItemBody from './ContactItemBody';
import ContactItemImage from './ContactItemImage';
 
function ContactItem({ imageUrl, name, tag }) {
 return (
   <div className="contact-item">
     <ContactItemImage imageUrl={imageUrl} />
     <ContactItemBody name={name} tag={tag} />
   </div>
 );
}
 
export default ContactItem;
```

9. Sekarang buatlah component ContactList. Di sinilah kita akan melakukan perulangan (menggunakan map) dalam memanggil component ContactItem sebanyak data contacts yang diberikan melalui properti.Silakan buat berkas JavaScript ContactList.jsx di dalam folder src.
```jsx
import React from 'react';
import ContactItem from './ContactItem';
 
function ContactList({ contacts }) {
 return (
   <div className="contact-list">
     {
       contacts.map((contact) => (
         <ContactItem key={contact.id} {...contact} />
       ))
     }
   </div>
 );
}
 
export default ContactList;
```

10. Komponen terakhir yang perlu kita buat adalah ContactApp. Komponen ini menjadi root component atau induk dari induk component yang ada di dalam aplikasi ini. Di komponen ini juga data contacts--yang didapatkan dari fungsi getData--bersemayam.Silakan buat berkas JavaScript bernama ContactApp.jsx di dalam src.
```jsx
import React from 'react';
import ContactList from './ContactList';
import { getData } from './data';
 
function ContactApp() {
 const contacts = getData();
 
 return (
   <div className="contact-app">
     <h1>Daftar Kontak</h1>
     <ContactList contacts={contacts} />
   </div>
 );
}
 
export default ContactApp;
```

Seperti yang Anda lihat pada kode di atas, praktik _unidirectional data flow_ sangat kental di React. Sekali lagi, di React data selalu hidup (berada) di _parent component_. Jika child component membutuhkannya, data akan dikirim secara _drilling_ (menurun) mulai dari komponen `ContactList`, `ContactItem`, `ContactItemImage`, dan `ContactItemBody` yang memanfaatkan properti.

11. Terakhir! Agar apa yang kita kerjakan dapat terlihat pada browser, render-lah component ContactApp pada root. Silakan buka berkas index.jsx dan ubah kode template “Hello, World” menjadi seperti ini.
```jsx
import React from 'react';
import { createRoot } from 'react-dom/client';
import ContactApp from './ContactApp';
 
 
const root = createRoot(document.getElementById('root'));
root.render(<ContactApp />);
```

Simpan seluruh perubahan dan jalankan kembali proyek (jika belum berjalan). Sekarang daftar kontak sudah tampak pada Browser.
![](img/Pasted%20image%2020260322193641.png)

di latihan selanjutnya kami akan menunjukkan bagaimana menggunakan CSS pada proyek React.