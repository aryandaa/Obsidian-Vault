#programming 
Pada HTML terdapat tiga tipe list.
1. _Unordered lists_: daftar yang ditampilkan tidak memiliki urutan. 
2. _Ordered lists_: daftar yang ditampilkan secara terurut.
3. _Description lists_: daftar yang terbuat dari beberapa istilah diikuti dengan deskripsi dari istilah tersebut.

### Unordered List
Seperti namanya, unordered list merupakan daftar yang tidak mementingkan urutan. Standarnya, unordered list menampilkan bullet pada tiap item list-nya (tetapi kita bisa mengubahnya dengan styling).

Untuk menetapkan konten sebagai unordered list kita gunakan `<ul></ul>`
kemudian di dalam elemen tersebut kita gunakan tags `<li></li>` untuk menetapkan item pada list tersebut. Contoh penerapannya sebagai berikut.
```html
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
  <li>Item 4</li>
</ul>
```
dan nanti outputnya akan seperti ini:
- Item 1
- Item 2
- Item 3
- Item 4

Di antara tag elemen `<li>`, kita dapat mengisikan konten apa pun termasuk elemen HTML lain. Contohnya, kita dapat memasukkan sebuah _heading_ atau paragraf pada item.
```html
<ul>
  <li><h1>Sebuah Heading sebagai item list</h1></li>
  <li><h2>Sebuah Heading level 2 sebagai item list</h2></li>
  <li><p>Sebuah paragraf sebagai item list</p></li>
</ul>
```

Kita juga bisa menambahkan elemen `<ul>` lagi dalam _list item_ untuk membuat _nested list_.
```html
<ul>
  <li>List item 1</li>
  <li>List item 2</li>
  <li>
    List item 3
    <ul>
      <li>List item 3.1</li>
      <li>List item 3.2</li>
      <li>List item 3.3</li>
    </ul>
  </li>
  <li>List item 4</li>
</ul>
```
outputnya:
- List item 1
- List item 2
- List item 3
    - List item 3.1
    - List item 3.2
    - List item 3.3
- List item 4

### Ordered List

_Ordered list_ digunakan untuk membuat list yang mementingkan urutan. Contohnya, membuat daftar instruksi langkah demi langkah sehingga dibutuhkan urutan yang sesuai. Ordered list bekerja seperti unordered list, tetapi perbedaannya adalah pada tiap item menampilkan angka bukan sebuah _bullet_. Angka yang ditampilkan, otomatis berurut tiap item-nya sehingga kita tidak perlu menuliskan secara kasar urutan nomornya. Hal ini tentu mempermudah kita untuk mengorganisasi tiap itemnya.

Untuk menetapkan konten sebagai ordered list kita gunakan `<ol></ol>`. Sama seperti unordered list, tiap item dalam list ditetapkan dengan menggunakan tags `<li></li>`.
```html
<ol>
  <li>Langkah pertama</li>
  <li>Langkah kedua</li>
  <li>Langkah ketiga</li>
  <li>Langkah selanjutnya</li>
</ol>
```
outputnya akan seperti ini:
1. Langkah pertama
2. Langkah kedua
3. Langkah ketiga
4. Langkah selanjutnya

Pada ordered list, tipe urutan angkanya dapat kita atur melalui sebuah atribut _type_. Contohnya, selain nomor, urutan angka dapat diganti dengan alfabet ataupun angka romawi.
```html
<ol type="I">
  <li>Langkah pertama</li>
  <li>Langkah kedua</li>
  <li>Langkah ketiga</li>
  <li>Langkah selanjutnya</li>
</ol>
 
<ol type="A">
  <li>Langkah pertama</li>
  <li>Langkah kedua</li>
  <li>Langkah ketiga</li>
  <li>Langkah selanjutnya</li>
</ol>
```

Berikut adalah nilai-nilai yang dapat digunakan pada atribut type pada elemen `<ol>`:

| Nilai | Deskripsi                                         |
| ----- | ------------------------------------------------- |
| 1     | Menggunakan angka dalam urutan item (_default_).  |
| a     | Menggunakan huruf kecil dalam urutan item.        |
| A     | Menggunakan huruf besar dalam urutan item.        |
| i     | Menggunakan huruf romawi kecil dalam urutan item. |
| I     | Menggunakan huruf romawi besar dalam urutan item. |

Selain tipe angka pada urutan, kita juga bisa menetapkan nilai awal pada sebuah _ordered list_ dengan menggunakan atribut _start_**.** Contohnya, jika kita ingin memulai sebuah list dari angka 7, kita tetapkan atribut start dengan nilai 7 pada elemen `<ol>`.
```html
<ol start="7">
  <li>Langkah ketujuh</li>
  <li>Langkah kedelapan</li>
  <li>Langkah kesembilan</li>
  <li>Langkah selanjutnya</li>
</ol>
```
dengan begini pengurutannya akan di mulai tergantung nominal yang di dalam start tersebut:
7. Langkah ketujuh
8. Langkah kedelapan
9. Langkah kesembilan
10. Langkah selanjutnya

Secara default, urutan list diawali dengan urutan paling rendah. Namun, kita dapat menambahkan atribut reversed pada elemen `<ol>` untuk membuat urutan dalam sebuah list terbalik. Atribut ini berbeda dengan atribut yang lain (yang sudah dibahas sebelumnya), atribut ini tidak memerlukan sebuah nilai ketika menggunakannya. Atribut ini hanya menandakan sebuah list untuk membalikkan urutan angka pada tiap item-nya. Berikut contoh penggunaannya:
```html
<ol start="7" reversed>
  <li>Langkah ketujuh</li>
  <li>Langkah kedelapan</li>
  <li>Langkah kesembilan</li>
  <li>Langkah selanjutnya</li>
</ol>
```
dengan begini, maka urutannya akan terbalik, mulai dari 7 lalu 6, 5, 4, 3, 2, 1.