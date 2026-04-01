#programming 
Di modul sebelumnya, Anda sudah belajar bahwa React component dibuat melalui sebuah fungsi. Namun, selain hanya fungsi, React component juga dapat dibuat menggunakan sintaksis **class**. Component yang dibuat menggunakan fungsi sering disebut dengan _functional component_, sedangkan component yang dibuat oleh class disebut dengan _class component_.

Class Component:
```jsx
import React from 'react';
 
class MyComponent extends React.Component {
  render() {
    const { name } = this.props;
 
    return (
      <div>
        <p>Hello, {name}!</p>
      </div>
    );
  }
}
```

Function Component:
```jsx
import React from 'react';
 
function MyComponent({ name }) {
  return (
    <div>
      <p>Hello, {name}!</p>
    </div>
  );
}
```

Perbedaan paling mendasar antara class component dan functional component adalah benefit yang didapatkan. Maksudnya, ketika Anda membuat component dengan class, React secara default menawarkan fitur state dan lifecycle yang dapat Anda manfaatkan. Itulah sebabnya component yang dibuat menggunakan class bersifat stateful atau disebut dengan “stateful” component, sedangkan component yang dibangun menggunakan function bersifat stateless karena tidak dapat memanfaatkan state. Functional component hanya memanfaatkan props sebagai data dalam menampilkan UI.

>Stateless dan stateful berbeda pada penyimpanan data sesi: **stateless** tidak mengingat interaksi sebelumnya (independen), sedangkan **stateful** melacak dan menyimpan data sesi pengguna. Stateless unggul di skalabilitas dan kecepatan, sementara stateful diperlukan untuk aplikasi dinamis yang membutuhkan konteks pengguna seperti keranjang belanja atau sistem login.

Walaupun terdengar memiliki banyak benefit, mohon untuk tidak membuat class component secara berlebihan karena pembuatan class component lebih “mahal” daripada functional component. Dari cara pembuatannya saja class component membutuhkan lebih banyak sintaksis dibandingkan dengan functional component. Jika Anda tidak berniat untuk memanfaatkan salah satu benefit yang ditawarkan, sebaiknya tetap gunakan functional component daripada class component.