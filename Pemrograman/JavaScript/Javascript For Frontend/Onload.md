#programming 
tugas pertama kita adalah memunculkan semua konten HTML setelah semua baris pada berkas HTML diproses oleh browser di mana event onload akan terjadi. Pada bagian tag `<script>,` kita akan menulis kode perintah, yang mana akan dijalankan ketika event onload terjadi pada elemen body. Kode perintah tersebut disebut sebagai event handler dari event onload.

Bagaimana membuat sebuah event handler untuk elemen tertentu? Tenang, kita akan membahas satu per satu dengan dimulai dari membuat sebuah fungsi event handler hingga “mengaitkan” fungsi tersebut supaya berjalan ketika event onload terjadi pada elemen body.

Cobalah buka berkas HTML dan deklarasikan function baru bernama welcome yang akan menghapus atribut hidden pada elemen `<div>` ketika elemen body selesai diproses oleh browser lalu menjalankan event onload. Fungsi tersebut diletakkan di antara tag `<script>`.
```js
function welcome(){
	alert('Sim salabim muncullah elemen-elemen HTML!');
	const konten = document.querySelector('.contents');
	konten.removeAttribute('hidden');
}
```

Pada kode di atas, kita akan memunculkan sebuah dialog box alert. Fungsi dari dialog box adalah memberitahu user bahwa elemen HTML yang sebelumnya bersembunyi akan ditampilkan. Caranya adalah dengan menghilangkan atribut hidden dari elemen `<div>`. Untuk menghilangkan atribut hidden, gunakan method removeAttribute() dari elemen yang dituju.

Mendekati akhir dari penutup tag `</script>`, kita perlu menambah kode event handler untuk event onload dari elemen body. Pada umumnya, menambahkan sebuah event handler pada sebuah event yang berasal dari sebuah elemen HTML tertentu akan menggunakan pendekatan seperti berikut.
```js
elemen.{nama_event} = namaFunction();
```

jika di implementasikan ke dalam code yang sudah dibuat, maka akan seperti ini:
```js
document.body.onload = welcome;
```
Pada kasus menulis event handler onload di sini, kode yang digunakan untuk memberikan event pada elemen body adalah sebagai berikut.

code lengkapnya untuk event onload seperti ini:
```js
<script>
  function welcome() {
    alert('Sim salabim muncullah elemen-elemen HTML!');
    const konten = document.querySelector('.contents');
    konten.removeAttribute('hidden');
  }
  document.body.onload = welcome;
</script>
```

Jika kita jalankan lagi melalui browser, maka akan muncul alert dengan pesan “sim salabim muncullah elemen-elemen HTML”.

