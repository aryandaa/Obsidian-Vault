#programming 
Dari sekian banyak event pada formulir, kita akan mulai dengan tiga event pertama, yaitu Kita akan mulai dengan event onInput, onFocus,

### Event onInput
Event onInput akan dijalankan setiap kali kita menulis atau menghapus apa pun pada sebuah field input yang memiliki event listener tersebut. Berkas HTML yang telah ditunjukkan di materi sebelumnya, field untuk mengisi nama panggilan (tag input dengan id inputNama) memiliki batas 15 karakter. Kita ingin membuat sebuah event handler, yang mana ketika menulis nama, akan ditampilkan sisa karakter yang dapat dituliskan oleh user.

Kita akan menggunakan event onInput untuk memeriksa setiap kali menulis atau menghapus karakter. Ingat ya, karena nanti kita menggunakan method addEventListener(), maka versi string event onInput untuk dimasukkan ke parameter pertama method tersebut adalah “input”.

Untuk mengimplementasi fitur tersebut, kita harus menambahkan event listener pada input yang memiliki id dengan nilai “inputNama” dan memperbarui teks setiap kali kita menulis atau menghapus karakter baru.

Tambahkan kode yang dicetak tebal berikut ke dalam berkas index.js.
```js
 document.addEventListener('DOMContentLoaded', function () {
    const inputMaxLengthOnLoad = document.getElementById('inputNama').maxLength;
    document.getElementById('sisaKarakter').innerText = inputMaxLengthOnLoad;
    
    document.getElementById('inputNama').addEventListener('input', function () {
      const jumlahKarakterDiketik = document.getElementById('inputNama').value.length;
      const jumlahKarakterMaksimal = document.getElementById('inputNama').maxLength;
      
      console.log('jumlahKarakterDiketik: ', jumlahKarakterDiketik);
      console.log('jumlahKarakterMaksimal: ', jumlahKarakterMaksimal);
      const sisaKarakterUpdate = jumlahKarakterMaksimal - jumlahKarakterDiketik;
      document.getElementById('sisaKarakter').innerText = sisaKarakterUpdate.toString();
      
      if (sisaKarakterUpdate === 0) {
        document.getElementById('sisaKarakter').innerText = 'Batas maksimal tercapai!';
      } else if (sisaKarakterUpdate <= 5) {
        document.getElementById('notifikasiSisaKarakter').style.color = 'red';
      } else {
        document.getElementById('notifikasiSisaKarakter').style.color = 'black';
      }
    });
  });
```

Kode di atas akan memeriksa jumlah karakter yang diperbolehkan dan didapatkan dari pengurangan atribut maxLength pada elemen `<input>` dengan jumlah karakter pada atribut value milik elemen `<input>` itu sendiri.

Jumlah karakter akan terus diperbarui selama kita mengetik atau menghapus karakter baru. Kondisi if dengan else if dibuat sekadar untuk memberikan variasi terhadap pesan jumlah karakter sisa yang ingin ditampilkan.

### Event onFocus
_Event onFocus_ akan dijalankan ketika melakukan klik di sebuah elemen _input_. Kita akan mencoba untuk menampilkan tulisan berupa notifikasi jumlah karakter yang masih diperbolehkan. Untuk dapat melakukan hal tersebut, kita harus menambahkan sebuah _event handler_ pada elemen _input_ yang menerima penulisan nama panggilan untuk _event onFocus_.

```js
document.getElementById('inputNama').addEventListener('focus', function () {
	console.log('inputNama: focus');
	document.getElementById('notifikasiSisaKarakter').style.visibility =
	 'visible';
});
```

Mantap, bukan? Walau form kita sudah bekerja sesuai dengan permintaan, tapi masih ada kejanggalan. Kejanggalannya terjadi ketika mengisi data pada elemen `<input>` lain atau tidak lagi fokus pada elemen tersebut, pesan sisa karakter tetap tampil dan tidak hilang. Hal tersebut dapat kita atasi dengan menambahkan event handler ketika event onBlur terjadi untuk elemen `<input>` tersebut.


### Event onBlur
_Event onBlur_ akan dijalankan ketika pada kondisi yang terbalik dengan _event onFocus_, yakni jika kita “pergi” dari elemen yang memiliki _event handler_ untuk _event onFocus._ Apa maksud dari “pergi”? Maksudnya adalah kita tidak lagi berinteraksi secara langsung dengan elemen tersebut seperti kita telah melakukan klik pada elemen lain.

```js
 document.getElementById('inputNama').addEventListener('blur', function () {
      console.log('inputNama: blur');
      document.getElementById('notifikasiSisaKarakter').style.visibility = 
      'hidden';
    });
```

Kode yang ditambahkan tersebut hanyalah melakukan kebalikan dari _event handler_ untuk _event_ onFocus yang kita terapkan sebelumnya. Kode tersebut akan “menyembunyikan” kembali pesan notifikasi jumlah sisa karakter yang diperbolehkan. Proses tersebut terjadi ketika kita klik elemen lain alias elemen `<input>` yang membuat nama panggilan sudah tidak menjadi fokus utama lagi.

