#programming 
Di modul sebelumnya, Anda sudah mengenal fitur React Context. Dengan memanfaatkan Context, kita bisa meminimalisasi praktik _props drilling_ pada tiap level komponen ketika mengirimkan state yang bersifat “global”. Context merupakan fitur penting dan tim React menyediakan cara yang lebih baik lagi ketika memanfaatkan Context pada functional component.

Sebelum hooks, untuk mengakses data dari Context, Anda memanfaatkan komponen `Context.Consumer` seperti ini.
```jsx
const LocaleContext = React.createContext('id');
 
function Content() {
  return (
    <LocaleContext.Consumer>
      {
        (locale) => (<Article locale={locale} />)
      }
    </LocaleContext.Consumer>
  );
}
```

Komponen `LocaleContext.Consumer` menggunakan teknik render props dalam memberikan akses data Context. Teknik ini akan menimbulkan **wrapper hell** ketika mengakses lebih dari satu Context.
```jsx
const LocaleContext = React.createContext('id');
const ThemeContext = React.createContext('light');
const UserContext = React.createContext({ id: 'user-1', name: 'Dicoding' });
 
function Content() {
  return (
    <LocaleContext.Consumer>
     {
       (locale) => (
         <ThemeContext.Consumer>
           {
             (theme) => (
               <UserContext.Consumer>
                 {
                   (user) => (
                     <Article locale={locale} theme={theme} user={user} />
                   )
                 }
                </UserContext.Consumer>
             )
           }
         </ThemeContext.Consumer>
       )
     }
    </LocaleContext.Consumer>
  )
}
```

Inilah alasan React menciptakan fungsi hooks lain yang bernama `useContext()`. Dengan `useContext()`, Anda bisa mendapatkan data dari React Context dengan cara yang lebih sederhana. Alih-alih menggunakan teknik render props, ia mengadopsi cara yang sama dengan penggunaan fungsi hooks lain, seperti `useState()`.
```jsx
const LocaleContext = React.createContext('id');
const ThemeContext = React.createContext('light');
const UserContext = React.createContext({ id: 'user-1', name: 'Dicoding' });
 
function Content() {
  const locale = React.useContext(LocaleContext);
  const theme = React.useContext(ThemeContext);
  const user = React.useContext(UserContext);
 
  return (
    <Article locale={locale} theme={theme} user={user} />
  );
}
```
Ingat, fungsi `useContext()` menerima satu argumen, yakni objek Context, bukan komponen `Context.Consumer` apalagi `Context.Provider`.

- **Benar**: `useContext(MyContext)`
- **Salah**: `useContext(MyContext.Consumer)`
- **Salah**: `useContext(MyContext.Provider)`

Sama halnya dengan `Context.Consumer`, fungsi `useContext()` akan mengembalikan nilai Context terdekat dari hierarki komponen. Jika nilai Context tidak tersedia dalam cakupan hierarki, ia akan mengembalikan nilai default. Selain itu, komponen yang menggunakan `useContext()` akan di-render ulang bila nilai di dalam Context berubah.


### Memoization State Context

> **Catatan:** Memoization adalah teknik dalam meningkatkan performa aplikasi dengan cara mempertahankan nilai--_beserta referensi memorinya_--yang "mahal" didapatkan untuk digunakan kembali ketika dibutuhkan.

Di modul sebelumnya, Anda sudah mengenal bahwa `this.state` adalah tempat yang cocok untuk menyimpan nilai state Context. Hal itu karena `this.state` memiliki referensi memori yang jelas sehingga React dapat mendeteksi perubahan data dengan tepat. Cara inilah yang digunakan React untuk menjaga performa aplikasi tetap unggul.
```jsx
class App extends React.Component {
  constructor(props) {
    super(props);
 
    this.state = {
      locale: 'id',
      toggleLocale: () => {
        this.setState((prevState) => {
          return {
            locale: prevState.locale === 'id' ? 'en' : 'id'
          };
        });
      }
    };
  }
 
  render() {
    return (
      <LocaleContext.Provider value={this.state}>
        {/* a whole app */}
        {/* a whole app */}
      </LocaleContext.Provider>
    );
  }
}
```

Setelah hadirnya hooks, kita bisa membuat state di dalam functional component dengan fungsi `useState()`. Lalu, seperti apa jadinya bila kasus di atas diterapkan pada functional component? Mungkin, intuisi Anda mengarahkan untuk menulis kode seperti ini.
```jsx
const LocaleContext = React.createContext();
 
function App() {
  const [locale, setLocale] = useState('id');
 
  const toggleLocale = () => {
    setLocale((prevLocale) => {
      return prevLocale === 'id' ? 'en' : 'id';
    });
  };
 
  const contextValue = {
    locale,
    toggleLocale
  };
 
  return (
    <LocaleContext.Provider value={contextValue}>
      {/* a whole app */}
      {/* a whole app */}
    </LocaleContext.Provider>
  );
}
```

Cara tersebut bukan praktik yang baik karena objek `contextValue` selalu dibuat kembali sehingga React menganggap bahwa nilai Context berubah. Ingat, variabel lokal yang berada di dalam fungsi akan dihapus setelah fungsi selesai dipanggil, begitu juga dengan referensinya. Untuk mengatasi masalah ini, React menyediakan fungsi hooks bernama `useMemo()` yang dapat dimanfaatkan untuk **membuat objek yang referensinya selalu sama**, kecuali ada perubahan data.
```jsx
const LocaleContext = React.createContext();
 
function App() {
  const [locale, setLocale] = useState('id');
 
  const toggleLocale = () => {
    setLocale((prevLocale) => {
      return prevLocale === 'id' ? 'en' : 'id';
    });
  };
 
  const contextValue = React.useMemo(() => {
    return {
      locale,
      toggleLocale
    };
  }, [locale]);
 
  return (
    <LocaleContext.Provider value={contextValue}>
      {/* a whole app */}
      {/* a whole app */}
    </LocaleContext.Provider>
  );
}
```

React menjamin nilai yang dikembalikan `useMemo()` selalu identik, kecuali ada perubahan data `locale`. Dengan cara ini, komponen apa pun yang menggunakan `LocaleContext`, baik melalui Consumer atau `useContext()`, akan di-render bila nilai `locale` berubah.