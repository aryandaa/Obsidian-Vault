#programming 
Di latihan sebelumnya, Anda sudah berhasil membuat SPA routing sederhana dengan React Router. Selanjutnya, kita berlatih dengan kasus yang lebih kompleks, yakni memanfaatkan path dan query (biasa disebut search params) dalam memberikan parameter di URL. Namun, sebelum memulai latihan, kita bahas sedikit teori tentang path dan query parameter dan implementasinya di React Router.

### Path Parameter

Path dalam _routing_ bisa dikatakan sebagai alamat yang digunakan browser untuk menampilkan halaman website. Alamat atau path yang dibuat biasanya merupakan teks verbal yang dapat dimengerti oleh pengguna. Tak jarang hanya dengan membaca path dari sebuah tautan kita langsung mengerti apa yang client minta kepada server.

Sebagai contoh, ketika membaca tautan GitHub ini [https://github.com/dicodingacademy](https://github.com/dicodingacademy), Anda pasti mengerti bahwa browser akan menampilkan profil dari username “dicodingacademy”. Contoh lain, dari alamat [https://www.linkedin.com/company/dicoding](https://www.linkedin.com/company/dicoding/), Anda bisa menebak bahwa browser akan menampilkan profil perusahaan Dicoding di platform LinkedIn.

GitHub dan LinkedIn menggunakan pendekatan yang sama dalam menampilkan halaman profil. Mereka memanfaatkan username sebagai bagian dari path untuk melakukan permintaan ke server. Apakah Anda terbayang cara mereka melakukannya? Di saat mereka memiliki pengguna yang banyak, apakah mereka menetapkan route satu per satu berdasarkan username untuk setiap penggunanya? Tentu tidak! Untuk melakukan hal tersebut, GitHub dan LinkedIn menggunakan teknik **path parameter**.

Singkatnya path parameter adalah salah satu teknik untuk mengirimkan atau menyisipkan sebuah data dengan memanfaatkan URL. Di React Router, kita dapat membuat path parameter dengan mudah. Caranya tambahkan tanda titik dua “:” yang menandai bahwa path tersebut adalah parameter. Contohnya seperti ini.

```jsx
<Routes>
  <Route path="/company/:name" element={<CompanyDetailPage />} />
</Routes>
```

Seperti yang Anda lihat di atas, pada props **path** terdapat bagian nilai yang ditulis dengan `:name`. Itu berarti, path tersebut adalah parameter dan nilainya bersifat dinamis. Contoh, Anda bisa mengaksesnya dengan alamat **/company/dicoding**, **/company/facebook**, **/company/twitter**, dan sebagainya. Seluruh path tersebut akan menampilkan component `<CompanyDetailPage />`.

Nilai parameter ini dapat diakses oleh `<CompanyDetailPage />` untuk dijadikan patokan perusahaan apa yang harus ditampilkan. Di React Router v5 ke atas, path parameter dapat diakses dengan memanfaatkan fungsi `useParams()` seperti berikut.

```jsx
import React from 'react';
import { useParams } from 'react-router-dom';
 
function CompanyDetailPage() {
  const params = useParams();
  return <p>Selamat datang di halaman perusahaan {params.name}</p>;
}
```

Fungsi `useParams()` akan mengembalikan objek yang berisi properti dan nilai dari path parameter. Dalam kasus routing di atas, kita dapat mengakses path `:name` dengan melalui `params.name`. Anda juga bisa memanfaatkan sintaksis ES6 (destructuring object) untuk mendapatkan nilai path parameters agar lebih ringkas.
```jsx
import React from 'react';
import { useParams } from 'react-router-dom';
 
function CompanyDetailPage() {
  const { name } = useParams();
  return <p>Selamat datang di halaman perusahaan {name}</p>;
}
```
Ketahuilah bahwa fungsi `useParams()` mengandalkan fitur [React Hooks](https://reactjs.org/docs/hooks-intro.html) yang akan kami bahas di modul akhir kelas ini. Jangan terlalu khawatir terkait Hooks saat ini.


### Query Parameter

Selain path parameter, ada cara lain yang dapat digunakan untuk mengirimkan data melalui URL, yakni dengan query atau search parameter. Teknik ini umum digunakan pada fitur pencarian atau filter data.

Data yang dikirim melalui query memiliki format _key=value_. Contohnya seperti berikut.

|   |
|---|
|/company/search?**name=dicoding&location=bandung**|

Query parameter diawali setelah tanda ? di akhir path URL dan dipisahkan dengan tanda & untuk setiap parameternya. URL yang ditunjukkan di atas memiliki dua query parameter, yaitu **name=dicoding** dan **location=bandung**. 

Seluruh nilai yang dikirim melalui query parameter diharapkan bersifat opsional, artinya bila nilainya tidak ditetapkan, halaman website tetap berjalan lancar. Hal ini berbeda dengan path parameter, di mana bila nilainya tidak ditetapkan, website bisa mengarah ke halaman yang berbeda.

Di React Router v5 ke atas, untuk mendapatkan query parameter yang berada di URL, gunakan fungsi `useSearchParams()`. Fungsi ini mengembalikan array yang memiliki dua item di dalamnya.

```jsx
import React from 'react';
import { useSearchParams } from 'react-router-dom';
 
function CompanySearchPage() {
  const [searchParams, setSearchParams] = useSearchParams();
 
  // ...
}
```

Item pertama (**searchParams**) merupakan instance dari [URLSearchParams](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams). Melalui instance ini, kita bisa mendapatkan nilai query params yang ada di URL. Contoh, jika URL saat ini adalah _/company/search?name=dicoding&location=bandung_, Anda bisa mengakses nilai parameter **name** dan **location** dengan cara seperti ini.
```jsx
import React from 'react';
import { useSearchParams } from 'react-router-dom';
 
function CompanySearchPage() {
  const [searchParams, setSearchParams] = useSearchParams();
 
  const name = searchParams.get('name');
  const location = searchParams.get('location');
 
  return (
    <p>
      Mencari perusahaan {name} di {location}
    </p>
  );
}
```


Kemudian item kedua (**setSearchParams**) merupakan fungsi untuk mengubah nilai query params secara terprogram (_programatically_). Fungsi ini berguna untuk menyelaraskan nilai query params di URL dengan state yang berada di UI.
```jsx
import React from 'react';
import { useSearchParams } from 'react-router-dom';
 
function CompanySearchPage() {
  const [searchParams, setSearchParams] = useSearchParams();
 
  const name = searchParams.get('name');
  const location = searchParams.get('location');
 
  // contoh, mengatur query name dengan nilai baru
  function updateNameUrlSearchParams(newValue) {
    setSearchParams({ name: newValue });
  }
 
  return (
    <p>
      Mencari perusahaan {name} di {location}
    </p>
  );
}
```

Sama halnya seperti fungsi _useParams_, _useSearchParams_ juga memanfaatkan React Hooks.