#programming 
Sejauh ini Anda sudah berhasil membuat class component dan memanfaatkan state dalam menyimpan data. Sekarang saatnya kita lanjutkan kembali proyek aplikasi daftar kontak yang sudah dibuat pada modul sebelumnya.

Setelah mempelajari state dan event handling, Anda mampu membuat data di dalam komponen dapat lebih hidup. Sekarang saatnya kita menambahkan fitur baru guna mengimplementasikan apa yang sudah Anda pelajari. Fitur yang akan dibangun adalah **hapus kontak**. Dengan hadirnya fitur ini, diharapkan aplikasi dapat menghapus kontak yang ditampilkan.

1. Buat 1.  berkas JavaScript baru bernama **DeleteButton.jsx** pada folder **src -> components**.
2. Di dalamnya, tuliskan kode untuk membuat component **DeleteButton**
```jsx
import React from 'react';
 
function DeleteButton({ id, onDelete }) {
  return <button className='contact-item__delete' onClick={() => onDelete(id)}>X</button>
}
 
export default DeleteButton;
```
Component **DeleteButton** menerima dua properti, yakni `id` dan `onDelete`. Properti id digunakan sebagai referensi id kontak yang hendak dihapus, sedangkan _onDelete_ merupakan handler yang akan dikirim secara _drilling_ sebagai aksi dalam menghapus kontak.  
      
Lihat juga bagaimana kami memanggil handler `onDelete` pada event `onClick`. Di sana pemanggilan fungsi _onDelete_ diberikan nilai id dan dibungkus dengan [anonymous function](https://en.wikipedia.org/wiki/Anonymous_function). Inilah cara ketika Anda hendak memberikan nilai argumen pada fungsi event handler ketika dipanggil.

**Catatan**: Mengapa terdapat “on”? Kata “on” pada penamaan _delete_ sebenarnya digunakan untuk menghindari [JavaScript reserved word](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#reserved_keywords_as_of_ecmascript_2015). Kita tidak bisa membuat variabel/properti bernama _delete_.

3. Selanjutnya, gunakan component **DeleteButton** di dalam component **ContactItem**. Jangan lupa tambahkan dan berikan juga props `id` dan `onDelete` karena component **DeleteButton** membutuhkannya.
```jsx
import React from 'react';
import ContactItemBody from './ContactItemBody';
import ContactItemImage from './ContactItemImage';
import DeleteButton from './DeleteButton';
 
function ContactItem({ imageUrl, name, tag, id, onDelete }) {
 return (
   <div className="contact-item">
     <ContactItemImage imageUrl={imageUrl} />
     <ContactItemBody name={name} tag={tag} />
     <DeleteButton id={id} onDelete={onDelete} />
   </div>
 );
}
 
export default ContactItem;
```

4. Karena sekarang component ContactItem membutuhkan properti id dan onDelete, kita perlu menyediakan nilai dari kedua properti tersebut pada component yang menggunakannya, yaitu ContactList. Silakan buka berkas ContactList.jsx dan ubah kodenya menjadi seperti ini.
```jsx
import React from 'react';
import ContactItem from './ContactItem';
 
function ContactList({ contacts, onDelete }) {
  return (
    <div className="contact-list">
      {
        contacts.map((contact) => (
          <ContactItem 
          key={contact.id}
          id={contact.id}
          onDelete={onDelete}
          {...contact} />
        ))
      }
    </div>
  );
}
 
export default ContactList;
```
Untuk properti onDelete, kita masih melakukan drilling karena nilai handler sebenarnya ada pada component ContactApp selaku pemilik data contacts.

5. Selanjutnya, kita ubah pembuatan component ContactApp menjadi class component. Jangan lupa saat ini kita perlu menyimpan data contacts di dalam this.state agar perubahan datanya memicu render UI. Kemudian buat juga method onDeleteEventHandler untuk menangani event ketika tombol hapus diklik.

Silakan buka berkas ContactApp.jsx dan ubah kode di dalamnya menjadi seperti ini.
```jsx
import React from 'react';
import ContactItem from './ContactItem';
 
function ContactList({ contacts, onDelete }) {
  return (
    <div className="contact-list">
      {
        contacts.map((contact) => (
          <ContactItem 
          key={contact.id}
          id={contact.id}
          onDelete={onDelete}
          {...contact} />
        ))
      }
    </div>
  );
}
 
export default ContactList;
```

Simpan seluruh perubahan dan coba kembali aplikasi pada Browser. Seharusnya tombol hapus sudah berfungsi dengan baik.