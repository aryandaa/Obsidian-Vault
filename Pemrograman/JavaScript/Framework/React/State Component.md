#programming 
Data merupakan hal yang membuat React component menjadi hidup. Bayangkan saja jika pada proyek contact-app tidak ada array yang menampung data contacts, tentu aplikasi menjadi tidak berguna karena tidak dapat menampilkan apa pun. Selain itu, data di dalam komponen diharapkan dapat berubah. Perubahan biasanya terjadi ketika ada interaksi atau input yang dilakukan pengguna. Interaksi bisa seperti menekan tombol tambah atau hapus kontak.

Untuk memahami pengelolaan data di dalam komponen React, yuk simak gambar di bawah ini.
![](img/Pasted%20image%2020260323171303.png)

Alat di atas (mari kita sebut counter) sering Anda temukan ketika hendak masuk ke gerbang wisata, karena memang counter digunakan untuk menghitung pengunjung yang datang. Menariknya, cara kerja komponen React dengan alat tersebut dapat dibilang mirip. Mengapa bisa demikian?

Counter menampilkan data berupa angka jumlah pengunjung yang datang pada saat itu. Biasanya tombol putih ditekan bila ada pengunjung baru, kemudian layar counter secara reaktif akan memperbarui tampilannya dengan data terbaru (jumlah sebelumnya +1). Di akhir hari (misalnya), petugas selalu memutar knob hitam untuk me-reset datanya agar dapat digunakan kembali di hari berikutnya. Ingat! Data pada counter tidak akan berubah bila tidak ada aksi yang dilakukan pengguna (seperti menekan tombol tambah atau reset).

React component memiliki cara kerja yang sama seperti counter dalam mengelola data. Di dalam React component, kita bisa menyimpan sebuah data yang bila berubah bisa memicu perubahan pada tampilan UI. Syaratnya, data tersebut perlu disimpan pada tempat khusus dinamakan state.

Meskipun state dan props dapat menyimpan data, tetapi keduanya hal yang berbeda. Data di dalam props berasal dari luar komponen dan diharapkan tidak berubah, sedangkan data di dalam state perlu diinisialisasi di dalam komponen itu sendiri dan datanya boleh berubah.

Di materi sebelumnya, Anda sudah tahu bahwa untuk memanfaatkan state, kita harus membuat class component. State di dalam class component dapat diakses melalui properti this.state dan datanya diinisialisasi di dalam constructor.

```jsx
import React from 'react';
 
class Counter extends React.Component {
  constructor(props) {
    super(props);
 
    // inisialisasi data dalam state
    this.state = {
      count: 0
    };
  }
 
  render() {
    return (
      <div>
        {/* menampilkan data count */}
        <p>{this.state.count}</p>
      </div>
    );
  }
}
```
Perubahan data yang disimpan di dalam this.state akan memicu pemanggilan fungsi render() pada class component, itulah kunci mengapa UI selalu menampilkan data terbaru. Namun, untuk mencapai tujuan tersebut, data di dalam state harus diubah melalui fungsi this.setState(), bukan melalui properti this.state secara langsung.
```jsx
this.setState((previousState) => {
  return {
    count: previousState.count + 1,
  }
});
```

ini adalah cara yang salah:
```jsx
this.state.count = this.state.count + 1;
```

Mari kita bahas fungsi setState() lebih dalam.

this.setState() atau setState() merupakan fungsi yang digunakan khusus untuk mengubah nilai state di dalam class component. Fungsi inilah yang sebenarnya memicu pemanggilan fungsi render() ketika data di dalam state berubah. Fungsi setState() dapat menerima dua tipe parameter, yaitu objek dan fungsi yang mengembalikan objek.

contoh parameter object
```jsx
this.setState({
  count: 0
});
```

contoh parameter fungsi:
```jsx
this.setState((previousState) => {
  return {
    count: previousState.count + 1
  }
});
```

Nilai yang objek diberikan_--__atau yang dikembalikan oleh fungsi__--_akan menjadi nilai **state** yang baru untuk menggantikan objek state lama. Namun, dalam memperbarui state yang baru, fungsi `this.setState()` menggunakan teknik "**menggabungkan**" bukan mengganti keseluruhan nilai state.

> Catatan: Jika komponen memiliki state **{ name: 'john',  surname: 'doe' }**, ketika Anda mengubah state dengan **this.setState({ name: 'jane' })**, nilai state `surname` tidak akan hilang dan tetap bernilai 'doe'.

Anda bisa memberikan parameter berupa objek (cara pertama) ketika ingin menetapkan nilai state tanpa memperhatikan nilai state yang ada sebelumnya. Contoh pada kasus counter, penggunaan ini dapat diimplementasikan ketika Anda ingin mereset nilai dari data `count`. Ketika mereset tentu kita tidak perlu memperhatikan atau mengetahui data sebelumnya ‘kan? Cukup berikan nilai baru, yakni 0.

Untuk parameter berupa fungsi (cara kedua), penggunaan ini cocok ketika Anda ingin menetapkan nilai state yang bergantung pada nilai state sebelumnya. Contohnya, ketika ingin menambahkan 1 nilai pada data counter, tentu Anda membutuhkan nilai yang sebelumnya, bukan? Anda bisa memanfaatkan `previousState` untuk melakukan hal itu.

Walaupun cara pertama terkesan lebih ringkas, tetapi secara pribadi penulis lebih suka menggunakan cara kedua dalam memanggil fungsi `setState()`. Mengapa demikian? Karena cara kedua dapat diterapkan pada kasus apa pun. Jika Anda tidak butuh nilai `previousState`, sebenarnya Anda tidak perlu menuliskan parameter tersebut 'kan?

Namun, sebenarnya pemilihan tersebut kembali lagi ke preferensi pribadi. Jika Anda merasa nyaman menggunakan cara pertama, go ahead! Kedua cara tersebut sama saja dan tidak ada pengaruhnya terhadap performa atau menyebabkan bug pada aplikasi. Aman!

### Rekap

Dengan membuat komponen yang mengelola _state_ di dalamnya, setiap kali ada perubahan pada state tersebut, React akan mengetahui dan secara otomatis membuat pembaruan pada UI. Ini adalah keuntungan besar ketika menggunakan React untuk membangun UI. Ketika kita perlu memperbarui tampilan, cukup perbarui _state_ saja. Kita tidak perlu melacak secara presisi bagian mana yang perlu di-_update_, biarkan React yang melakukannya berdasarkan state terbaru. Sederhana, bukan?

> **Catatan:** Proses menentukan apa yang telah berubah di output baru dari output sebelumnya dinamakan dengan [Reconciliation](https://reactjs.org/docs/reconciliation.html).

Lalu, kapan dan di mana kita harus memanggil fungsi _setState()_ untuk memperbarui _state_? Jawabannya ketika terjadi interaksi dari pengguna. Untuk menangkap interaksi pengguna pada React component, Anda perlu belajar dulu bagaimana cara Event Handling bekerja pada React. Kita akan bahas mengenai itu di materi selanjutnya.