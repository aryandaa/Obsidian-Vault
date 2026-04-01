#programming 
Salah satu faktor terpenting ketika membuat Single-Page Application adalah memanfaatkan URL, karena secara alami website memanfaatkan URL dalam menampilkan konten. Meskipun SPA sangatlah interaktif, percuma saja bila pengguna tidak bisa memanfaatkan URL dalam mengatur state atau halaman yang ditampilkan.

Mengapa hal ini menjadi penting karena di awal materi kami menjelaskan banyak sekali benefit yang bisa dilakukan dengan URL. Selain mudah dalam membagikan halaman yang spesifik, kita juga sering memanfaatkan fitur bookmark di browser, bukan? Hal tersebut bisa dicapai bila SPA dapat memanfaatkan URL.

Karena masalah inilah kita tidak bisa mengandalkan component state secara manual untuk menampilkan halaman yang berbeda. Kita butuh cara yang lebih komprehensif untuk menangani masalah _routing_ di React ini. Untunglah React memiliki ekosistem yang luas sehingga kita bisa memanfaatkan [react-router](https://reactrouter.com/) untuk mengatasi masalah ini.

Dengan React Router, kita dapat membuat Single-Page App di React dengan lebih mudah. React Router juga sudah menyediakan beberapa kebutuhan untuk routing seperti mengelola navigasi (link), URL, dan masih banyak lainnya.

_“react-router has taken on a new meaning. Instead of just being a router for React, it’s showing what a truly React-like router looks like”_ - Mark Dalgleish (CSS Modules co-creator).

React Router bukan tools resmi yang disediakan React dalam melakukan routing, tetapi penggunaan React Router secara alami selaras dengan konsep dasar React. Di mana, untuk membuat routing, semuanya dilakukan memanfaatkan konsep yang ada di React seperti component, props, composition, dan konsep lainnya. Bila Anda paham dan nyaman dengan konsep atau paradigma yang di React, Anda akan mudah memahami penggunaan dari React Router ini. Bahkan Anda bisa belajar React lebih baik lagi ketika menggunakan react-router. 

**Catatan:** Jika React membuat Anda menjadi JavaScript Developer yang lebih baik, React Router bisa membuat Anda menjadi React Developer yang lebih baik.

React Router tersedia untuk environment web (ReactDOM) ataupun native (React Native) [2]. Untuk menggunakan React Router pada environment web, Anda perlu memasang package [react-router-dom](https://www.npmjs.com/package/react-router-dom) menggunakan NPM atau Yarn.
`npm install react-router-dom`
`yarn add react-router-dom`

### React Router Components

React Router memiliki banyak komponen di dalamnya, tetapi Anda tidak perlu mengetahui seluruhnya sekaligus. Dalam mengimplementasikan _routing_ secara umum, minimal ada 4 komponen yang perlu Anda ketahui. Berikut penjelasannya.

- **BrowserRouter**  
    Komponen ini berperan sebagai pembungkus (_wrapper_) untuk seluruh cakupan aplikasi yang memanfaatkan _routing_. Komponen inilah yang mengatur dan mengawasi perubahan URL guna memastikan komponen atau halaman tampil sesuai dengan perubahannya.
```jsx
import React from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
 
const root = createRoot(document.getElementById('root'));
root.render(
 <BrowserRouter>
   {/* The rest of your app goes here */}
 </BrowserRouter>
);
```

**Link**  
Komponen ini digunakan oleh pengguna untuk menavigasi halaman selama berada di aplikasi. Secara prinsip, komponen ini mirip dengan komponen <Link /> yang kita buat pada latihan sebelumnya, tetapi jauh lebih canggih karena terintegrasi dengan URL dan [History API](https://developer.mozilla.org/en-US/docs/Web/API/History).  
  
Ketika pengguna berinteraksi (mengeklik) komponen Link untuk menavigasi halaman, ia akan memberitahu **BrowserRouter** untuk mengubah URL aplikasi. Karena **Link** dan **BrowseRouter** saling berkomunikasi, penggunaan komponen Link harus berada di dalam cakupan BrowserRouter.  
  
Komponen Link juga memiliki aksesibilitas yang baik. Seluruh tautan yang dibentuk melalui komponen ini memiliki kemampuan yang sama dengan element **`<a>`** secara _native_, seperti dapat diakses menggunakan focus keyboard, dibuka pada tab baru, serta kemampuan anchor _native_lainnya.
```jsx
import React from "react";
import { Link } from "react-router-dom";
 
function UsersIndexPage({ users }) {
  return (
    <div>
      <h1>Users</h1>
      <ul>
        {users.map((user) => (
          <li key={user.id}>
            <Link to={user.id}>{user.name}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
```


**Routes dan Route**  
Dokumentasi React Router mengatakan bahwa komponen Routes dan Route memegang peranan penting dalam React Router. Pasalnya, dengan komponen inilah kita dapat mendefinisikan komponen atau halaman apa yang ditampilkan berdasarkan URL. Komponen ini akan menggantikan peran dari penggunaan if atau short-circuit evaluation yang dilakukan pada latihan sebelumnya. Karena komponen ini terintegrasi dengan URL, kita dapat lebih mudah dalam membuat dan memanfaatkan parameter yang disisipkan dalam bentuk _path_ (/users/:id) atau _query_(/users?id).
```jsx
<Routes>
  <Route path="/" element={<Dashboard />} />
  <Route path="/about" element={<AboutPage />} />
</Routes>
```

**Catatan:** Penggunaan komponen **Route** tak terpisahkan dengan **Routes**. Komponen Route hanya dapat digunakan sebagai _child_ komponen Routes.

Untuk mengetahui lebih dalam mengenai komponen yang tersedia di dalam React Router, tolong untuk eksplorasi dokumentasi yang diberikan.
- [BrowserRouter](https://reactrouter.com/en/main/router-components/browser-router)
- [Link](https://reactrouter.com/en/main/components/link)
- [Routes dan Route](https://reactrouter.com/en/main/components/routes)

