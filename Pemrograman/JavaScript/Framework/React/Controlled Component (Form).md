#programming 
Ketika Anda membuat **form** pada aplikasi web, biasanya _state_ atau data input berada di dalam DOM. Namun di React, manajemen state (data) sangat efektif bila dilakukan di dalam komponen. Sehingga, data dalam mengelola nilai form sebaiknya tidak dilakukan di DOM, melainkan di dalam komponen dengan memanfaatkan state. Hal ini membuat state di dalam form dapat lebih terkontrol.

_Controlled Component_ merupakan component yang me-_render_ form, tetapi _“single source of truth”_ atau sumber datanya diambil dari component state, bukan DOM. Alasan mengapa disebut dengan controlled component karena React mengontrol data form.

Contoh, di sini kita memiliki komponen yang me-render form dengan satu input.
```jsx
import React from 'react';
 
class NameForm extends React.Component {
  constructor(props) {
    super(props);
 
    this.state = {
      email: ''
    };
  }
 
  render() {
    return (
      <form>
        <input type="text" value={this.state.email} />
      </form>
    );
  }
}

```
Pada element input, kita memberikan properti `value` dengan nilai yang berasal dari state (_email_). Itu berarti, nilai input akan selalu sama dengan nilai state `email`. Karena itu, satu-satunya cara memperbarui nilai input adalah memperbarui nilai component state. Ini adalah contoh dari controlled element, di mana React yang mengontrol nilai dari input form.

Coba Anda ketik sesuatu di elemen input text tersebut, nilainya tidak akan berubah. Ini karena nilai value akan selalu mengikuti state. Ini sejalan dengan peringatan yang ditampilkan di [dokumentasi resmi React](https://react.dev/reference/react-dom/components/input#controlling-an-input-with-a-state-variable).

Untuk mengubah nilai state email, kita perlu membuat _handler_ seperti ini.
```jsx
import React from 'react';
 
class NameForm extends React.Component {
  constructor(props) {
    super(props);
 
    this.state = {
      email: ''
    };
 
    this.onEmailChangeHandler = this.onEmailChangeHandler.bind(this);
  }
 
  onEmailChangeHandler(event) {
    this.setState(() => {
      return {
        email: event.target.value
      };
    });
  }
 
  render() {
    return (
      <form>
        <input 
        type="text"
        value={this.state.email}
        onChange={this.onEmailChangeHandler} />
      </form>
    );
  }
}
```

Kapan pun input berubah, fungsi handler akan dipanggil karena kita menetapkan fungsi tersebut pada property `onChange`.

Walau dalam membuat controlled component banyak kode yang perlu ditulis, tapi ada kelebihannya juga, _lho_! Salah satunya, kita dapat menerapkan validasi secara instan.Karena state dikelola oleh component, kita bisa menuliskan logika validasi di component dan validasi akan dijalankan setiap kali nilai state berubah.

Ketahuilah bahwa benefit tersebut terjadi karena adanya input dari pengguna. Jika ada input, state akan berubah, dan UI akan diperbarui berdasarkan state terbaru. Ini adalah konsep inti, bukan hanya pada controlled component, tetapi React secara umum. Inilah konsep yang kami tampilkan pada bagan di atas dan sering dikenal dengan istilah [one-way data flow](https://react.dev/learn/thinking-in-react#step-2-build-a-static-version-in-react) atau [unidirectional data flow](https://legacy.reactjs.org/docs/state-and-lifecycle.html#the-data-flows-down).

