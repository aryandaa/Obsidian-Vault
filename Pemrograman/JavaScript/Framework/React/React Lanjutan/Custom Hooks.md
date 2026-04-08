#programming 
Setelah mendapatkan pemahaman tentang hooks melalui `useState()`, `useEffect()`, dan `useContext()`, sekarang kita akan mencari tahu cara untuk membuat fungsi hooks sendiri. Ketahuilah bahwa fungsi hooks bersifat _reusable_. Ketika Anda memiliki logika nonvisual di dalam sebuah komponen yang ingin diterapkan di banyak komponen, ekstrak logika tersebut menjadi sebuah fungsi hooks, inilah yang disebut custom hooks.

Dalam membuat fungsi hooks, React menetapkan aturan bahwa nama dari fungsi hooks harus diawali dengan kata “use”, contohnya `useInput()` atau `useUser()`.
```jsx
// ini fungsi hooks
function useInput() {}
 
// ini fungsi hooks
function useUser() {}
 
// ini bukan fungsi hooks
function createInput() {}
 
// ini bukan fungsi hooks
function getUser() {}
```

Alasan dari konvensi ini adalah untuk memberitahu React bahwa fungsi tersebut merupakan hooks karena fungsi hooks perlu diperlakukan sesuai aturan yang ditetapkan oleh React (nanti akan kami bahas aturan dari penggunaan hooks). 

Sekarang, mari kita lihat bagaimana kita dapat mengekstraksi logika nonvisual pada sebuah komponen. Anggaplah kita memiliki komponen yang membangun UI form input. Jika Anda menggunakan teknik _controlled component_, tentu sumber data form-nya berasal dari state komponen. Oleh karena itu, bangunlah controlled component dengan fungsi hooks `useState()` seperti ini.
```jsx
function RegisterForm() {
  const [email, setEmail] = React.useState('');
  const [password, setPassword] = React.useState('');
  const [confirmPassword, setConfirmPassword] = React.useState('');
 
  const handleEmailChange = (event) => setEmail(event.target.value);
  const handlePasswordChange = (event) => setPassword(event.target.value);
  const handleConfirmPasswordChange = (event) => setConfirmPassword(event.target.value);
 
  return (
    <form>
      <input value={email} onChange={handleEmailChange} />
      <input value={password} onChange={handlePasswordChange} />
      <input value={confirmPassword} onChange={handleConfirmPasswordChange} />
    </form>
  );
}
```

Pada kode di atas, ada beberapa duplikasi logika dalam membangun controlled component. Kita perlu melakukan dua hal untuk menangani sebuah input, yaitu menyediakan state sebagai sumber data input dan menyediakan fungsi handler untuk mengubah nilai state berdasarkan masukan pengguna. Di komponen `RegisterForm`, setidaknya ada 3 input yang perlu dibuat sehingga akan ada 3 duplikasi logika yang dituliskan di sana.

Untuk mengurangi hal itu, kita perlu mengekstraksi logika input dengan membuat custom hooks seperti ini.
```jsx
function useInput(defaultValue) {
  const [value, setValue] = React.useState(defaultValue);
  const handleValueChange = (event) => setValue(event.target.value);
  return [value, handleValueChange];
}
```

Di dalam fungsi `useInput()` kita menuliskan seluruh logika yang dibutuhkan ketika membangun input, yakni menyediakan state dan fungsi handler untuk mengubah nilai state. Kemudian di akhir fungsi, kembalikan lagi dua nilai tersebut agar dapat digunakan oleh komponen untuk membangun UI input. Ketika mengembalikan nilai `value` dan `handleValueChange`, kami memanfaatkan array literal untuk menciptakan pengalaman yang sama seperti ketika menggunakan fungsi hooks `useState()`.

> **Catatan:** Di dalam fungsi custom hooks, kita dapat memanggil fungsi hooks lain seperti useState(), useEffect(), atau bahkan custom hooks lainnya.

Sekarang, gunakanlah fungsi `useInput()` untuk meminimalisasi duplikasi kode yang ditulis.
```jsx
function RegisterForm() {
  const [email, handleEmailChange] = useInput('');
  const [password, handlePasswordChange] = useInput('');
  const [confirmPassword, handleConfirmPasswordChange] = useInput('');
 
  return (
    <form>
      <input value={email} type="email" onChange={handleEmailChange} />
      <input value={password} type="password" onChange={handlePasswordChange} />
      <input value={confirmPassword} type="password" onChange={handleConfirmPasswordChange} />
    </form>
  );
}
```

Fungsi `useInput()` bisa digunakan di banyak komponen bila komponen tersebut membutuhkan logika yang sama.
```jsx
function LoginForm() {
  const [email, handleEmailChange] = useInput('');
  const [password, handlePasswordChange] = useInput('');
 
  return (
    <form>
      <input value={email} onChange={handleEmailChange} />
      <input value={password} type="password" onChange={handlePasswordChange} />
    </form>
  );
}
```

>**Catatan:** Anda bisa mengakses kode lengkapnya secara langsung melalui tautan: [custom-hooks-useinput-sample](https://codesandbox.io/s/10-custom-hooks-useinput-sample-zz4zpb?file=/src/index.js).

