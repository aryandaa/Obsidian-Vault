#programming 
### External Style Sheet

_External Style Sheet_ adalah berkas terpisah yang di dalamnya hanya ada CSS rules. Berkas harus berekstensi **.css** dan akan dihubungkan dengan dokumen HTML. Cara ini merupakan yang paling _powerful_ dalam menerapkan styling. Dengan cara ini, satu berkas styling (.css) dapat digunakan oleh banyak berkas HTML.

Untuk menautkan berkas **.css** dengan dokumen HTML, kita dapat gunakan elemen `<link> `pada `<head>` berkas HTML. Contohnya berikut.
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>Judul Dokumen</title>

    <!-- Impor berkas CSS Anda -->
    <link rel="stylesheet" href="styles.css">
  </head>
  <body>
    <h1>Kota Bandung</h1>
  </body>
</html>
```
```css
h1 {
  color: green;
  text-decoration: underline;
}
```
hasilnya akan menampilkan tulisan "Kota Bandung" berwarna hijau.

Pada elemen `<link>` tersebut, kita tetapkan berkas CSS yang digunakan dengan menggunakan atribut href dan beri nilai “stylesheet” pada atribut rel sebagai _relationship_ (hubungan) antara berkas **style.css** dengan dokumen HTML.

Pada contoh di atas, kita tahu bahwa berkas css yang digunakan adalah berkas lokal (berkas yang berada pada komputer/server kita sendiri). Nilai atribut href juga dapat berupa berkas .css yang tersedia melalui sebuah URL.

Contohnya, banyak pengembang menggunakan **bootstrap.min.css** untuk membantu penyusunan layout website-nya. Kita bisa menggunakannya pada berkas HTML dengan langsung menuliskan URL untuk berkas tersebut.

```html
<head>
  <title>Document Title</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
</head>
```

**Catatan:**  
Nama berkas yang mengandung “min.css” adalah penamaan format berkas CSS yang sudah di-minify atau diminimalkan dengan menghilangkan white space yang tidak digunakan.

### Embedded Style Sheet

_Embedded Style Sheet_ adalah kumpulan rules yang dituliskan dalam berkas HTML dengan menggunakan elemen `<style>`. Dengan demikian, CSS rules yang dituliskan hanya dapat dicakup oleh satu berkas HTML. Penulisan rules harus dituliskan dalam elemen` <style>` dan biasanya ditempatkan dalam `<head>` pada berkas HTML.

```html
<head>
  <title>Document Title</title>
  <style>
    /*
    * Rules styling dituliskan di sini
    */
  </style>
</head> 
```
 berikut contoh penerapan:
 ```html
 <!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>Judul Dokumen</title>

    <style>
      h1 {
        color: green;
      }
    </style>
    
  </head>
  <body>
    <h1>Kota Bandung</h1>
  </body>
</html>
 ```
 kode ini sama seperti yang diatas, bedanya css berada di dalam file html langsung.

### Inline Style

_Inline Style_ adalah styling yang diterapkan secara langsung pada elemen HTML dengan menggunakan atribut `style`. _Yap_, ini tidak berbeda dengan atribut yang telah kita pelajari sebelumnya.

Jadi, apa maksudnya? Kita bisa memberi styling ke target elemennya. Bisa dikatakan juga bahwa kita memberikan style declaration dalam satu baris bersamaan dengan deklarasi elemen HTML. Ingat! Kita tidak perlu lagi selector dalam metode ini.
```html
<nama-elemen style="color: green">Konten elemen HTML</nama-elemen>
```

Untuk memperbanyak styling properties (multiple properties), kita tuliskan saja mereka dalam atribut yang sama, tetapi kita perlu memanfaatkan _semicolon_ (**;**) sebagai pemisah antar styling properties-nya.

```html
<h1 style="color: green; margin-top: 2em">Kota Bandung</h1>
```

Inline styles hanya diterapkan pada elemen tempat atribut **style** diterapkan. Teknik ini seharusnya dihindari, terkecuali benar-benar diperlukan untuk menggantikan sebuah styling yang ditetapkan pada Embedded Style Sheet atau External Style Sheet.