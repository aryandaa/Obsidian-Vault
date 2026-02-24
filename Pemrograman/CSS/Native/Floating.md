#programming 

Secara sederhananya, properti float dapat membuat elemen berada pada sebelah kanan atau kiri. Bahkan, jika diterapkan pada elemen inline memungkinkan elemen di sekitarnya mengelilingi elemen tersebut (_wrap_).

HTML:
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>Judul Dokumen</title>
    
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
    <div class="container">
      <img
        src="https://raw.githubusercontent.com/dicodingacademy/a123-webdasar-labs/099-shared-files/shared-media/g-dicoding-logo.png"
        alt="g Dicoding Logo"
        width="200px"
      />
      <p>
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet asperiores commodi corporis
        doloribus eum ipsum obcaecati pariatur quam quo, voluptatum? A, assumenda atque delectus
        dolore nam natus neque quisquam repudiandae?
      </p>
      <p>
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. At deserunt illum inventore
        numquam officia recusandae, sit! Ab asperiores delectus dolor, eius est explicabo impedit
        ipsa ipsum itaque mollitia neque nihil nisi officia praesentium sint! Accusantium libero
        obcaecati provident qui? Error!
      </p>
      <p>
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam debitis dolorem eaque eius
        eos error eum ex facilis fuga ipsa iste iusto mollitia nam natus necessitatibus praesentium
        quam qui quod, rerum sed sequi sint voluptates? Atque enim, ex facere fugiat ipsum mollitia
        quos sunt. At, autem commodi dolorum eos, est expedita, incidunt molestias nobis nostrum
        officia porro reiciendis saepe voluptatum.
      </p>
    </div>
  </body>
</html>
```

CSS:
```css
.container {
  width: 800px;
  border: 4px solid black;
  padding: 10px;
}

img {
  float: left;
  margin: 10px;
}
```

Output:
![](image/Floating.png)

Selain dalam membuat text wrapping, float juga merupakan salah satu teknik dalam membuat layout website. Teknik ini masih banyak digunakan oleh developer karena sangat mudah dipahami dan tergolong mudah untuk _multiple column_ seperti gambar berikut
![](image/Floating%202.png)

Hal ini dapat dilakukan dengan mudah menggunakan properti `float` karena nilai dari properti ini adalah `left` dan `right`. Nilai tersebut menunjukkan posisi elemen harus diletakkan. Contoh penerapannya seperti berikut.

HTML:
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>Judul Dokumen</title>
    
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
    <div class="container">
      <div class="left-content">
        <h3>Left Content</h3>
      </div>
      <div class="right-content">
        <h3>Right Content</h3>
      </div>
    </div>
  </body>
</html>
```

CSS:
```css
* {
  /* digunakan untuk menghapus seluruh padding dan margin standar yang diberikan browser pada elemen */
  margin: 0;
  padding: 0;

  /* Menggunakan border-box dalam perhitungan dimensi box-nya */
  box-sizing: border-box;
}

.container {
  width: 800px;
  height: 400px;
  border: 1px solid black;
  margin: 0 auto;
}

.left-content {
  text-align: center;
  line-height: 400px;
  width: 30%;
  height: 100%;
  background-color: #00c7ed;

  /* digunakan untuk memindahkan posisi elemen ke sisi kiri container */
  float: left;
}

.right-content {
  text-align: center;
  line-height: 400px;
  width: 70%;
  height: 100%;
  background-color: #60d0a8;

  /* digunakan untuk memindahkan posisi elemen ke sisi kanan container */
  float: right;
}
```

sehingga hasilnya akan seperti diatas itu.

Dari contoh di atas, kita bisa melihat pada selector .left-content dan .right-content ditetapkan properti float dengan nilai **left** dan **right** sehingga elemen tersebut dapat diposisikan secara bersebelahan. 

Ketika menggunakan properti float, jangan lupa untuk menentukan ukuran lebar dari propertinya karena nilai dari lebar menentukan seberapa banyak ruang yang dicakup oleh elemen. Pada contoh di atas, kita menetapkan nilai 30% untuk konten kiri dan 70% untuk konten sebelah kanan.


