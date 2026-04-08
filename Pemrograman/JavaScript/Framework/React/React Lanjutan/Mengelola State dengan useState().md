#programming 
Sebelum hooks, sudah menjadi aturan baku bahwa untuk menggunakan state di dalam komponen, kita harus membuat class component. Namun, setelah hadirnya hooks, Anda tahu bahwa functional component bisa memanfaatkan state melalui fungsi `React.useState()`.

Fungsi `React.useState()` hadir sejak React v16.8. Fungsi tersebut menerima satu argumen berupa nilai awal state dan mengembalikan array. Index pertama dari array tersebut berupa nilai state, sedangkan index kedua merupakan fungsi untuk mengubah nilai state.
```jsx
const localeArray = React.useState('id')
const locale = localeArray[0]
const setLocale = localeArray[1]
 
...
 
locale // 'id'
setLocale('en')
locale // 'en'
```

Praktik terbaik dalam mendapatkan nilai state dan fungsi untuk mengubahnya adalah dengan memanfaatkan _destructuring assignment_ sehingga dapat dilakukan hanya dengan satu baris. Kode selengkapnya dapat Anda simak di bawah ini.
```jsx
function Greeting() {
  const [locale, setLocale] = React.useState('id');
 
  const changeToId = () => setLocale('id');
  const changeToEn = () => setLocale('en');
 
  return (
    <div>
      {locale === 'id' ? (
        <>
          <p>Selamat pagi!</p>
          <button onClick={changeToEn}>Translate</button>
        </>
      ) : (
        <>
          <p>Good morning!</p>
          <button onClick={changeToId}>Terjemahkan</button>
        </>
      )}
    </div>
  );
}
```
> **Catatan**: Cobalah jalankan kode tersebut pada tautan [contoh-react-usestate](https://codesandbox.io/s/7-contoh-react-usestate-v22utk).

  
### Memicu untuk Me-render Ulang dan Mempertahankan Nilai State
Jika Anda mencoba kode yang kami berikan di atas, lihatlah cara kerja `useState()` terlebih dahulu. Sama seperti state pada class component, perubahan nilai state yang dibuat oleh `useState()` akan memicu komponen (yang menggunakannya) me-render ulang. Namun, ajaibnya nilai state yang berada di functional component tidak hilang atau reset ke nilai awal. Mengapa bisa demikian?

Biasanya setiap variabel yang hidup di dalam fungsi akan dibawa oleh garbage collector untuk dihapus dari memori setiap kali fungsi tersebut selesai dieksekusi (terkecuali Anda membuat sebuah closure).
```jsx
function foo() {
  const name = 'John';
  const surname = 'doe';
}
 
foo();
// name dan surname dibawa oleh garbage collector untuk dihapus
```
Komponen yang dibuat dengan fungsi seharusnya memiliki cara kerja yang sama. Namun, jika itu terjadi, state di dalam functional component tidak akan pernah bisa bekerja sesuai harapan. Anda pasti berpikir bahwa nilai state seharusnya terhapus dan kembali ke awal ketika proses render terjadi, tetapi ternyata tidak.

Hal ini menyiratkan bahwa di belakang layar, React berhasil menemukan cara untuk mempertahankan nilai dari proses render yang terjadi berulang kali. Anda tidak perlu tahu proses React dapat melakukan itu. Yang pasti, melalui `useState()` kita mampu membuat variabel yang dapat bertahan dari proses render dan memicu komponen untuk me-render ulang.


### Membuat Banyak State pada Komponen
Membuat lebih dari satu state di dalam komponen merupakan hal yang wajar. Di class component, this.state selalu bernilai objek. Ketika Anda butuh lebih dari satu state, buatlah banyak properti di dalam objek this.state seperti berikut.
```jsx
class ProfileInput extends React.Component {
  constructor(props) {
    super(props);
 
    this.state = {
      name: 'John',
      surname: 'Doe'
    };
  }
  
  // ...
}
```

Berbeda dengan `useState()`, Anda bisa membuat banyak state secara terpisah seperti ini.
```jsx
function ProfileInput() {
  const [name, setName] = useState('John');
  const [surname, setSurname] = useState('Doe');
 
  return (
    // ...
  )
}
```

Mungkin Anda penasaran, mengapa tidak dibuat state objek seperti class component? Bukankah akan terlihat lebih mudah jika dibuat seperti ini?
```jsx
function ProfileInput() {
  const [ state, setState ] = useState({
    name: 'John',
    surname: 'Doe'
  });
 
  return (
    // ...
  )
}
```

Cara di atas memang bisa dilakukan, tetapi ada hal yang perlu Anda perhatikan. Mengubah nilai state melalui fungsi yang berasal dari `useState` memiliki cara kerja yang berbeda dengan `this.setState()` milik class component. Seperti yang Anda ketahui pada class component, perubahan state dengan `this.setState()` tidak akan memengaruhi nilai state yang tidak diubah. Contoh, bila Anda hanya ingin mengubah nilai state `name`, lakukan dengan cara berikut.
```jsx
this.state = {
  name: 'John',
  surname: 'Doe',
}
 
this.setState(() => {
  return {
    name: 'Jane'
  };
});
 
console.log(this.state) // { name: 'Jane', surname: 'Doe' }
```
Kode di atas tidak akan mengubah nilai state surname karena `this.setState()` bersifat “menggabungkan”, bukan mengganti seluruh nilai state.

Nah, kontras dengan perubahan state yang dilakukan dengan `useState()`. Alih-alih menggabungkan, perubahan state dengan `useState()` akan “mengganti” seluruh nilai state yang ada. Sehingga, jika kita mengubah nilai state `name` dengan cara seperti kode di bawah ini, akan menghapus nilai state `surname`.
```jsx
const [state, setState] = useState({
  name: 'John',
  surname: 'Doe',
});
 
setState({
  name: 'Jane'
});
 
console.log(state) // { name: 'Jane' }
```

Cara untuk mengatasi masalah ini adalah dengan memanfaatkan nilai state sebelumnya untuk menjaga nilainya tidak berubah. Namun, cara ini bukan pilihan yang tepat bila objek state yang dikelola kompleks karena akan berimbas performa komponen yang Anda buat.
```jsx
const [state, setState] = useState({
  name: 'John',
  surname: 'Doe',
});
 
setState((prevState) => {
  return {
    ...prevState, // tidak disarankan.
    name: 'Jane'
  }
})
 
console.log(state) // { surname: 'Doe', name: 'Jane' }
```

### Perubahan State Berjalan secara Asynchronous
Pada fungsi `this.setState()` yang dimiliki class component, setiap kali kita ingin mengubah nilai state berdasarkan nilai sebelumnya, disarankan untuk melampirkan fungsi sebagai argumen di dalam `this.setState()` daripada objek.

Direkomendasikan:
```jsx
class Counter extends React.Component {
  constructor(props) {
    super(props);
 
    this.state = {
      count: 0
    };
 
    this.increment = this.increment.bind(this);
    this.decrement = this.decrement.bind(this);
  }
 
  increment() {
    this.setState((prevState) => {
      return {
        count: prevState.count + 1
      };
    });
  }
  decrement() {
    this.setState((prevState) => {
      return {
        count: prevState.count - 1
      };
    });
  }
 
  render() {
    return (
      <div>
        <p>{this.state.count}</p>
        <button onClick={this.increment}>+</button>
        <button onClick={this.decrement}>-</button>
      </div>
    );
  }
}
```

Tidak Direkomendasikan:
```jsx
class Counter extends React.Component {
  constructor(props) {
    super(props);
 
    this.state = {
      count: 0
    };
 
    this.increment = this.increment.bind(this);
    this.decrement = this.decrement.bind(this);
  }
 
  increment() {
    this.setState({
      count: this.state.count + 1
    });
  }
  decrement() {
    this.setState({
      count: this.state.count - 1
    });
  }
 
  render() {
    return (
      <div>
        <p>{this.state.count}</p>
        <button onClick={this.increment}>+</button>
        <button onClick={this.decrement}>-</button>
      </div>
    );
  }
}
```

Alasan dari semua itu adalah fungsi `this.setState()` berjalan secara _asynchronous_. Banyak sekali hal yang terjadi di balik layar ketika `this.setState()` dipanggil. Itulah sebabnya React menjadikan proses update state berjalan secara _asynchronous_. Lalu, untuk menjamin kita mengakses “state sebelumnya” secara tepat, React menyelipkan nilai pada argumen fungsi `this.setState()` sebagai nilai state yang paling _up-to-date_.

Cara yang sama juga diterapkan pada fungsi pengubah state yang dihasilkan `useState()`. Jika ingin mengubah nilai state yang bergantung dengan nilai state sebelumnya, pastikan Anda memberikan fungsi sebagai argumen di fungsi pengubah nilai `state`, bukan nilai `state` secara langsung.
```jsx
function Counter() {
  const [count, setCount] = useState(0);
 
  const increment = () => setCount((prevCount) => prevCount + 1);
  const decrement = () => setCount((prevCount) => prevCount - 1);
 
  return (
    <div>
      <p>{count}</p>
      <button onClick={increment}>+</button>
      <button onClick={decrement}>-</button>
    </div>
  );
}
```


### Tingkatkan Performa dengan _Lazy State Initialization_
Anda sudah tahu bahwa `useState()` menerima satu argumen yang nilainya akan dijadikan nilai awal state. Lalu, bagaimana bila nilai awal state diambil dari sebuah proses yang “mahal”? Anggaplah, nilai state count diambil dari proses kalkulasi matematika yang sangat rumit.
```jsx
function getExpensiveCount() {
  console.log("Calculating initial count");
  return 9999;
}
```

Untuk menggunakan fungsi `getExpensiveCount()` sebagai nilai awal state `count`, pasti intuisi Anda mengarahkan untuk menuliskan kode seperti ini.
```jsx
function Counter() {
  const [count, setCount] = useState(getExpensiveCount());
 
  const increment = () => setCount((prevCount) => prevCount + 1);
  const decrement = () => setCount((prevCount) => prevCount - 1);
 
  return (
    <div>
      <p>{count}</p>
      <button onClick={increment}>+</button>
      <button onClick={decrement}>-</button>
    </div>
  );
}
```

Cara tersebut bekerja, tetapi terdapat dampak terhadap performa yang buruk karena fungsi `getExpensiveCount()` akan dijalankan setiap kali proses _render_ terjadi. Sangat tidak ideal, bukan? Jika Anda ingin fungsi tersebut hanya dijalankan satu kali (tidak di setiap _render_), berbahagialah karena React menyediakan cara untuk terlepas dari permasalahan ini.

Caranya, berilah nilai pada `useState()` sebuah fungsi sehingga ketika fungsi tersebut dipanggil akan mengembalikan nilai awal state. Mungkin terdengar abstrak, tetapi kode berikut ini dapat memberikan Anda gambaran dengan jelas.
```jsx
function Counter() {
  const [count, setCount] = useState(() => getExpensiveCount());
 
  const increment = () => setCount((prevCount) => prevCount + 1);
  const decrement = () => setCount((prevCount) => prevCount - 1);
 
  return (
    <div>
      <p>{count}</p>
      <button onClick={increment}>+</button>
      <button onClick={decrement}>-</button>
    </div>
  );
}
```

Jika Anda masih bingung perbedaannya, simak kode yang kami berikan di dalam `useState()`. Di contoh pertama, _function invocation_ (pemanggilan fungsi) pada `useState()` secara langsung mendapatkan nilai 9999 karena itu yang akan dikembalikan oleh fungsi `getExpensiveCount()`. Namun, pada contoh kedua, kami memberikan nilai _function declaration_ pada `useState()`. Cara ini akan memberitahu React bahwa fungsi `getExpensiveCount()` hanya butuh dipanggil satu kali saja.