#programming 
Karena React component merupakan fungsi JavaScript, kita dapat memberikan parameter ketika menggunakannya. Namun, React component hanya dapat menerima satu parameter--berupa objek--yang biasa kita sebut dengan properties (props).
```jsx
function SayHello(props) {
  const name = props.name;
  const company = props.company;
 
  return (
    <p>
      Hello, {name} from {company}!
    </p>
  );
}
```

penggunaan:
```jsx
<SayHello name="Bill" company="Microsoft" />; // <p>Hello, Bill from Microsoft!</p>
<SayHello name="Steve" company="Apple" />; // <p>Hello, Steve from Apple!</p>
<SayHello name="Mark" company="Facebook" />; // <p>Hello, Mark from Facebook!</p>
```
Melalui props yang ditunjukkan kode di atas, kita dapat mengirimkan data ketika menggunakannya. Hal inilah yang membuat component sangat _reusable_ karena hanya dengan satu component--beserta properti yang terdefinisikan--kita dapat menampilkan UI serupa dengan data yang berbeda.


#### Beberapa Best Practice ketika membuat dan menggunakan properti
Hampir seluruh tipe data di JavaScript dapat dikirimkan melalui props. Namun, terdapat best practice dalam menetapkan properti yang penting untuk Anda ikuti. 

_Best practice_ yang pertama adalah hindari penggunaan JavaScript object ketika mengirimkan data pada properti component.

Contohnya seperti ini:
```jsx
function InstagramProfile(props) {
  const profile = props.profile;
  const name = profile.name;
  const username = profile.username;
  const bio = profile.bio;
  const isVerified = profile.isVerified;
  return (
    <div className="container">
      <dl>
        <dt>Name: </dt>
        <dd>{name}</dd>
        <dt>Username: </dt>
        <dd>{username}</dd>
        <dt>Bio: </dt>
        <dd>{bio}</dd>
        <dt>Verified: </dt>
        <dd>{isVerified ? 'yes' : 'no'}</dd>
      </dl>
    </div>
  );
}
 
const profile = {
  name: 'Dicoding Indonesia',
  username: 'dicoding',
  bio: 'Bangun Karirmu Sebagai Developer Profesional',
  isVerified: true
};
 
<InstagramProfile profile={profile} />; // sebisa mungkin, hindari praktik seperti ini
```
Oke, mungkin menggunakan objek sebagai “pembungkus” data terlihat lebih mudah karena kita hanya perlu mendefinisikan satu properti saja pada component yaitu profile. Namun, hal ini lah yang menyebabkan kontrak dalam penggunaan component tersebut tidak jelas. Sebab JavaScript merupakan bahasa yang tidak terikat dengan tipe data (weakly typed) sehingga praktik seperti ini sebaiknya dihindari.

Alih-alih mengirimkan props dalam bentuk objek, sebaiknya definisikanlah propertinya satu per satu. Sehingga, kita tak lagi mengirimkan objek, melainkan cukup dengan nilai primitif seperti string, number, atau boolean.
```jsx
function InstagramProfile(props) {
  const name = props.name;
  const username = props.username;
  const bio = props.bio;
  const isVerified = props.isVerified;
 
  return (
    <div className="container">
      <dl>
        <dt>Name: </dt>
        <dd>{name}</dd>
        <dt>Username: </dt>
        <dd>{username}</dd>
        <dt>Bio: </dt>
        <dd>{bio}</dd>
        <dt>Verified: </dt>
        <dd>{isVerified ? 'yes' : 'no'}</dd>
      </dl>
    </div>
  );
}
 
<InstagramProfile
  name="Dicoding Indonesia"
  username="dicoding"
  bio="Bangun Karirmu Sebagai Developer Profesional"
  isVerified // pemberian nilai boolean "true" cukup dengan menuliskan nama properti tanpa nilai apa pun
/>;
```
Dengan cara ini, kontrak dalam menggunakan component akan lebih terlihat lebih jelas. Selain itu, secara tidak langsung kita juga sudah menerapkan prinsip [least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege) guna menghindari dalam mengirimkan data yang sebenarnya tidak diperlukan.

_Best practice_ lainnya adalah selalu gunakan fitur ES6 agar sintaksis yang dituliskan lebih bersih, singkat, dan mudah dibaca. Contohnya pada komponen InstagramProfile, kita dapat menggunakan [_object destructuring_](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment) dalam mengakses nilai propertinya. Sehingga, kita tidak perlu menuliskan kode satu per satu dalam membuat variabel lokal yang menampung nilai dari props.
```jsx
function InstagramProfile({ name, username, bio, isVerified }) {
  return (
    <div className="container">
      <dl>
        <dt>Name: </dt>
        <dd>{name}</dd>
        <dt>Username: </dt>
        <dd>{username}</dd>
        <dt>Bio: </dt>
        <dd>{bio}</dd>
        <dt>Verified: </dt>
        <dd>{isVerified ? 'yes' : 'no'}</dd>
      </dl>
    </div>
  );
}
```
Terakhir, ketika menggunakan nilai properti, tanamkan di pikiran Anda bahwa properti bersifat read-only alias hanya boleh dibaca dan tidak boleh diubah nilainya. React component harus bersifat _pure_, salah satunya dengan tidak mengubah nilai yang diberikan melalui sebuah parameter atau properti. Hal ini sama seperti prinsip [_pure function_](https://github.com/MostlyAdequate/mostly-adequate-guide/blob/master/ch03.md) pada _functional programming_. Jika di dalam component Anda menuliskan kode yang mengubah nilai dari properti, silakan evaluasi kode tersebut. Pastikan Anda tidak melakukan perubahan pada nilainya.

> **Catatan:** UI aplikasi memang bersifat dinamis dan seringkali berubah seiring terjadinya interaksi oleh pengguna. Namun, data di dalam komponen yang bertugas untuk menampung perubahan bukanlah props, melainkan state. Jangan khawatir akan state saat ini karena kami akan membahas state pada component di modul selanjutnya.


#### Children
React component memiliki satu properti spesial bernama children. Properti ini spesial karena cara memberikan nilainya berbeda dengan properti biasa. Anda sudah mengetahui bahwa pemberian nilai properti pada component dilakukan sama seperti pemberian nilai atribut HTML. 

Contoh, untuk memberikan properti name pada component SayHello, Anda bisa melakukannya dengan seperti ini.
```jsx
function SayHello({ name }) {
  return <p>Hello, {name}!</p>;
}
 
<SayHello name="Dicoding" />; // <p> Hello, Dicoding!</p>
```

Cara pemberian nilai pada properti _children_ berbeda. Alih-alih menggunakan gaya atribut seperti kode di atas, nilai children ditetapkan di antara tag pembuka `<SayHello>` dan tag penutup `</SayHello>` component.
```jsx
function SayHello({ children }) {
  return <p>Hello, {children}!</p>;
}
 
<SayHello>Dicoding</SayHello>; // Hello, Dicoding!
```

Jadi, untuk menggunakan properti children, cara pemanggilan component pun harus menggunakan tag pembuka dan penutup.