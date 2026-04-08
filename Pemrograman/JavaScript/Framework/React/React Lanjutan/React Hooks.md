#programming 
Sejak React v.0.14.0, kita memiliki dua cara untuk membuat komponen, yaitu menggunakan `class` dan `function`. Perbedaan paling mendasar antara class component dan functional component adalah benefit yang didapatkan. Maksudnya, ketika membuat component dengan class, React secara default menawarkan fitur state dan lifecycle yang dapat Anda manfaatkan. Namun, bila Anda hanya membutuhkan komponen yang dapat menerima props dan me-render UI saja, gunakanlah functional component.

**Setelah hadirnya React Hooks, teori tersebut sudah tidak berlaku**. Dengan hooks, Anda bisa membuat komponen menggunakan function “hampir” dalam semua kasus. Contohnya penggunaan state, sinkronisasi data (yang sebelumnya dilakukan oleh lifecycle method), context, dan lainnya.

> **Catatan:** Kami menyebut “hampir” karena tim React sendiri masih terus mengembangkan hooks agar mampu mencakup seluruh hal yang dapat dilakukan oleh class component.

Dengan begitu, kita tidak perlu memanggil super(props), khawatir lupa melakukan binding method, bahkan tak perlu menggunakan keyword this lagi. Pokoknya, seluruh masalah yang timbul akibat class sudah dipastikan lenyap.

Lalu, bagaimana masalah state, lifecycle method, dan berbagi kode “nonvisual” dapat ditangani oleh functional component? Oke, mari kita bahas satu per satu.

### State
Karena dengan functional component kita tidak bisa lagi mengakses `this.state`, React menyediakan API baru untuk membuat dan mengelola state. Caranya, manfaatkanlah fungsi hooks `React.useState()`.

> **Catatan:** Saat ini kami cukup menunjukkan penggunaan fungsi `useState()` secara singkat. Kita akan membahas masing-masing fungsi hooks lebih jauh di materi selanjutnya.

```jsx
const loadingTuple = React.useState(true);
const isLoading = loadingTuple[0];
const setLoading = loadingTuple[1];
 
// ...
 
isLoading; // true
setLoading(false);
isLoading; // false
```

Fungsi `useState()` menerima satu argumen, yaitu nilai awal state. Fungsi `useState()` mengembalikan array dengan index pertama merupakan state (`isLoading`) dan index kedua berupa fungsi untuk mengubah nilai state (`setLoading`). Supaya lebih ringkas, Anda dapat memanfaatkan sintaksis [destructuring assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment) untuk mendapatkan nilai dari kedua index tersebut seperti ini.

```jsx
// const loadingTupple = React.useState(true);
// const isLoading = loadingTupple[0];
// const setLoading = loadingTupple[1];
 
const [isLoading, setLoading] = React.useState(true);
```

Sekarang, kita lihat penggunaan fungsi `useState()` dalam membuat state `isLoading` dan movie pada komponen `MovieDetail`.
```jsx
function MovieDetail({ id }) {
  const [isLoading, setLoading] = React.useState(true);
  const [movie, setMovie] = React.useState(null);
 
  if (isLoading) {
    return <p>Loading ...</p>;
  }
 
  return (
    <div>
      <h1>{movie.title}</h1>
      <p>{movie.description}</p>
    </div>
  );
}
```
Oke, masalah state sudah terselesaikan dengan fungsi `React.useState`.

### Lifecycle Methods
Seperti yang sudah Anda ketahui, bila menggunakan functional component, kita tidak bisa mengakses method lifecycle. Bila Anda beranggapan bahwa dengan hadirnya hooks, functional component dapat mengakses lifecycle method, maaf, anggapan Anda kurang tepat.

Ketahuilah bahwa hooks tidak menyediakan cara mengakses lifecycle method di functional component. Karena lifecycle-lah yang sebenarnya mendorong kita untuk menuliskan duplikasi logika. Alih-alih menyediakan alternatif dalam mengakses lifecycle, React ingin kita fokus dengan paradigma lain, yaitu sinkronisasi.

Sinkronisasi adalah hal yang krusial di React. Sering kali kita perlu menyinkronkan state dengan perubahan yang terjadi, baik yang datangnya dari internal (props) maupun eksternal (DOM, websocket, dan lainnya).

Cara terbaik untuk melakukan sinkronisasi berdasarkan perubahan adalah membuat efek samping (side-effect). Itulah sebabnya React menyediakan fungsi hooks bernama `React.useEffect` untuk membuat  fungsi efek berdasarkan perubahan nilai.
```jsx
React.useEffect(() => {
   document.title = `Hello, ${username}`;
}, [username]);
```

Pada kode di atas, fungsi yang didefinisikan di dalam `useEffect()` akan dijalankan setiap kali `username` berubah. Oleh karena itu, kita dapat menyinkronkan [document title](https://developer.mozilla.org/en-US/docs/Web/API/Document/title) dengan nilai `username` tanpa perlu mendefinisikan logika di berbagai method lifecycle, seperti `componentDidMount()` dan `componentDidUpdate()`.  
  
Lalu, bagaimana jika `useEffect` diimplementasikan pada komponen `MovieDetail` untuk menangani fetch request? Anda dapat melakukan hal berikut.
```jsx
function MovieDetail({ id }) {
  const [isLoading, setLoading] = React.useState(true);
  const [movie, setMovie] = React.useState(null);
 
  React.useEffect(() => {
    async function updateMovie() {
      setLoading(true);
      const movie = await fetchMovie(id);
      setLoading(false);
      setMovie(movie);
    }
    // perform update movie every id change
    updateMovie();
  }, [id]);
 
  if (isLoading) {
    return <p>Loading ...</p>;
  }
 
  return (
    <div>
      <h1>{movie.title}</h1>
      <p>{movie.description}</p>
    </div>
  );
}
```
Dari kode di atas, `updateMovie()` akan dijalankan setiap kali props `id` berubah. Dengan begitu, `MovieDetail` selalu menampilkan film yang _update_. Cukup jelas, bukan? Tidak ada lagi duplikasi kode yang dituliskan pada method lifecycle untuk melakukan sinkronisasi state di komponen. Hal tersebut hilang dan telah diganti dengan sebuah fungsi.


### Berbagi Kode Nonvisual
Di materi sebelumnya, kami menyebutkan bahwa React tidak menyediakan cara untuk berbagi kode nonvisual antar komponen. Hal itu sulit dilakukan karena state di dalam class component sangat terikat dan terisolasi. Masalah ini memicu kita untuk menggunakan teknik High-Order Component yang dapat menimbulkan kendala lain seperti wrapper hell.

Sudah lama React Developer bertahan dalam keadaan seperti ini hingga tim React mampu menyelesaikan masalahnya melalui React Hooks. Sebenarnya, tidak ada cara khusus untuk berbagi kode di hooks selain membuat “custom hooks” yang dapat mengeluarkan logika (nonvisual) agar dapat digunakan pada banyak komponen. Agar lebih jelas, mari kita lihat implementasi custom hooks pada komponen `MovieDetail`.

Di dalam `MovieDetail` terdapat logika untuk mengelola state movie dan isLoading serta menjaga nilai movie agar tetap update berdasarkan props `id`.
```jsx
function MovieDetail({ id }) {
  const [isLoading, setLoading] = React.useState(true);
  const [movie, setMovie] = React.useState(null);
  
  React.useEffect(() => {
    async function updateMovie() {
      setLoading(true);
      const movie = await fetchMovie(id);
      setLoading(false);
      setMovie(movie);
    }
    updateMovie();
  }, [id]);
 
  if (isLoading) {
    return <p>Loading ...</p>;
  }
 
  return (
    <div>
      <h1>{movie.title}</h1>
      <p>{movie.description}</p>
    </div>
  );
}
```

Jika kita ingin komponen lain dapat melakukan hal yang serupa, ekstrak kode tersebut menjadi fungsi terpisah.

```jsx
function useMovie(id) {
  const [isLoading, setLoading] = React.useState(true);
  const [movie, setMovie] = React.useState(null);
 
  React.useEffect(() => {
    async function updateMovie() {
      setLoading(true);
      const movie = await fetchMovie(id);
      setLoading(false);
      setMovie(movie);
    }
 
    updateMovie();
  }, [id]);
 
  return { isLoading, movie };
}
```

Fungsi `useMovie()` merupakan custom hooks alias fungsi hooks yang kita buat sesuai kebutuhan sendiri.

Fungsi tersebut menerima satu argumen `id` yang perubahan nilainya akan menjadi patokan kapan film harus diperbarui. Selain itu, fungsi ini mengembalikan state `isLoading` dan `movie` yang nantinya akan digunakan oleh komponen dalam menampilkan UI. Menariknya, segala hal yang berurusan untuk mengelola dan memperbarui state `movie` serta `isLoading` dapat dipindahkan ke dalam custom hooks ini. Dengan begitu, berbagi kode antar komponen menjadi lebih mudah.

Contoh, jika komponen apa pun membutuhkan akses terhadap state `movie` atau `isLoading`, gunakanlah fungsi hooks `useMovie()`.
```jsx
function MovieDetail({ id }) {
  const { isLoading, movie } = useMovie(id);
 
  return (
   // ... normal layout
  );
}
 
function MovieDetailGridMode({ id }) {
  const { isLoading, movie } = useMovie(id);
 
  return (
    // ... grid layout
  )
}
```
Sungguh menakjubkan! Dengan custom hooks tentu dapat meringkas banyak duplikasi kode dan penggunaan pola yang sulit seperti High-Order Components.

Sekarang semua masalah yang kami sebutkan di awal sudah teratasi oleh hooks.

- ~~Memanggil `super()` di class component adalah hal yang menjengkelkan.~~
- ~~Keyword `this` sulit untuk dipahami oleh manusia, bahkan mesin.~~
- ~~Jika Anda tahu cara kerja `this`, tetap saja harus melakukan bind secara manual. Ini lebih menjengkelkan.~~
- ~~React memaksa kita untuk menata logika dengan orientasi komponen lifecycle. Hal ini membuat duplikasi kode.~~
- ~~Tidak ada cara yang sederhana dan baik untuk berbagi kode nonvisual di React.~~

Hooks tidak hanya membuat functional component dapat menggunakan state, tetapi hooks dapat melakukan lebih dari itu. Dengan hooks, kita bisa mendapatkan banyak benefit mulai dari menyederhanakan kode, menciptakan kode yang reusable, hingga membuat developer dan klien bahagia.

Saat ini kami sudah mengenalkan secara singkat beberapa fungsi hooks, seperti `useState()`, `useEffect()`, dan custom hooks. Di materi selanjutnya, kita akan mengenal lebih jauh masing-masing fitur tersebut.

