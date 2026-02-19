#programming 
Pembahasan tentang pengiriman data ini memiliki hubungan dengan web server. Apakah Anda masih ingat tentang peranan dari web server?

Ketika client membutuhkan resources guna menampilkan halaman web ke pengguna, ia akan mengirimkan request ke server tentang kebutuhan yang dimaksud. HTML, CSS, JavaScript, serta aset-aset lainnya merupakan resources yang akan dikirimkan dan di-render oleh browser sehingga tampillah halaman web yang utuh. Nah, hal tersebut merupakan proses yang serupa yang akan dilakukan oleh browser dan server.

Berbicara mengenai mengirim data dari formulir ke server, kita membutuhkan satu elemen esensial dalam membangun formulir. Sebelumnya, kita hanya belajar tentang variasi elemen input untuk mendapatkan data yang sesuai. Ada satu elemen yang berfungsi sebagai wrapper (pembungkus) dari keseluruhan kolom input atau formulir. Elemen yang dimaksud adalah `<form>`.

Jika diterapkan, berikut adalah contoh sederhana penerapan elemen form.
```html
<form>
  <div>
    <label for="email">Email</label>
    <br />
    <input type="email" id="email" />
  </div>
 
  <div>
    <label for="password">Password</label>
    <br />
    <input type="password" id="password" />
  </div>
 
  <button type="submit">Submit</button>
</form>
```

### Atribut Name di Elemen Input

Dalam mengirimkan data ke server, kita wajib menerapkan atribut `name` pada seluruh kolom input dalam formulir. Contohnya, Anda ingin membuat formulir untuk melakukan pemesanan kamar hotel. Anda harus memberi atribut name pada seluruh elemen input.

Silakan perhatikan contoh formulir berikut.
```html
<form>
  <div>
    <label for="fullName">Nama</label>
    <input id="fullName" name="fullName" required />
  </div>
 
  <div>
    <label for="checkIn">Tanggal Check-In</label>
    <input type="date" id="checkIn" name="checkIn" required />
  </div>
 
  <div>
    <label for="checkOut">Tanggal Check-Out</label>
    <input type="date" id="checkOut" name="checkOut" required />
  </div>
 
  <button type="submit">Submit</button>
</form>
```

Mengapa hal ini diperlukan? Seharusnya, setiap data dikirimkan dalam bentuk pasangan key dan value. Key merupakan identitas atau nama dari data yang dikirimkan, sedangkan value adalah data yang diisi oleh user. Hal ini akan memberikan kemampuan pada server untuk mengambil data berdasarkan key-nya. Lebih jelasnya, kita akan melihat penjelasan pada **Cara Membawa Data Formulir**.

### Cara Membawa Data Formulir

Elemen form memiliki atribut-atribut khusus yang menentukan konfigurasi request untuk dikirimkan ketika user menekan tombol submit. Ada dua atribut: action dan method.

#### Atribut Action
Atribut action akan menentukan alamat tujuan dari pengiriman data. Kita bisa memberikannya URL yang mengarah pada suatu server atau kadang disebut sebagai API. Server yang dimaksud dapat server yang berada pada domain yang sama atau berbeda. Dalam hal ini, kita bisa memberikan URL yang relatif atau absolut.
```html
<form action="https://example.com/jalur/ke/alamat/destinasi">
  <!-- Berbagai macam kolom input -->
</form>
```
```html
<form action="/jalur/ke/alamat/destinasi">
  <!-- Berbagai macam kolom input -->
</form>
```

Bagaimana jika kita tidak menyertakan atau menentukan atribut ini pada elemen form? Jika sampai demikian, data-data formulir akan dikirimkan ke alamat yang saat ini sedang diakses.
```html
<form>
  <!-- Berbagai macam kolom input -->
</form>
```

#### **Metode GET**
Biasanya, metode ini digunakan untuk mendapatkan data dari server. Data tersebut akan diterima oleh browser melalui body response (HTTP response). Tidak hanya itu, HTTP request juga memiliki body request untuk mengirimkan data dari browser ke server. Namun, body request dengan metode GET akan kosong. Hal ini karena setiap data yang dikirimkan akan diletakkan dalam URL parameters.

Perhatikan contoh kode di atas pada formulir login user. Lalu, bayangkan kita membuat formulir dengan metode GET seperti berikut.
```html
<form method="GET" action="https://example.com/">
  <!-- Kolom input login disembunyikan -->
</form>
```

Jika setiap input telah diisi dan user menekan tombol submit, setiap data akan diletakkan dalam URL parameter. Data akan diletakkan dalam pasangan key dan value. Key adalah atribut nama pada elemen input, sedangkan value adalah nilai yang diisi oleh user. Berikut adalah tampak URL dari request yang akan diperoleh.
https://example.com/?email=EMAIL_USER&password=PASSWORD_USER
Sebab ada beberapa kolom input yang tersedia, setiap pasangan key dan value akan dipisahkan dengan karakter ampersand (&).


#### **Metode POST**
Metode lain yang bisa digunakan adalah metode POST. Ini merupakan metode untuk mengirimkan data dari browser ke server. Umumnya, metode ini meminta server menanggapi terhadap data yang telah dikirimkan oleh browser dan mengharapkan pengembalian dari hasil tanggapan tersebut (response).

Silakan perhatikan kembali formulir login sebelumnya. Jika metode GET tidak memiliki body request dan menyebabkan data-data diletakkan dalam URL parameters, metode POST akan berperilaku sebaliknya. Maksudnya, setiap data tidak akan berada pada URL, tetapi mereka akan diletakkan dalam body request.
```html
<form method="POST" action="https://example.com/">
  <!-- Kolom input login disembunyikan -->
</form>
```

