#programming 
PropTypes API merupakan cara melakukan validasi properti di runtime yang dikembangkan langsung oleh core team React. Sayangnya, pada versi React v19 ke atas, implementasi fitur ini sudah dihapus. Namun, hal itu tidak menghilangkan esensi mengapa kita tetap perlu melakukan validasi properti.

Sejak awal, validasi properti hadir untuk menjaga kontrak antar-komponen tetap jelas dan andal ketika aplikasi dijalankan. Di dunia nyata, data yang dikonsumsi oleh komponen sering datang dari luar kendali kita, contoh response API yang tidak konsisten, data dari localStorage yang kedaluwarsa, query string yang dimanipulasi pengguna, dan faktor eksternal lainnya. Semua itu terjadi di runtime, bukan kompilasi, sehingga mekanisme pengecekan di runtime tetap relevan  dan layak dipertahankan.

Pengalaman Anda belajar PropTypes di React v18 sama sekali tidak sia-sia. Justru pemahaman tentang “kontrak data” itulah yang kita bawa maju. PropTypes sejauh ini sudah memberikan kesan yang baik (mendeskripsikan bentuk data, membedakan yang wajib dan opsional, dll). Nilai-nilai ini tetap kita butuhkan di React v19, tetapi kita mengandalkan library validasi runtime tersendiri seperti Zod atau Joi.

Kedua library tersebut memungkinkan kita menulis schema yang eksplisit, penanganan error yang fleksibel, dan memberikan jembatan yang elegan untuk solusi validasi runtime. Untuk proyek yang belum menggunakan TypeScript, Joi menjadi pilihan yang tepat untuk digunakan saat ini.

### Runtime Property Validation dengan Joi

Lalu bagaimana konsep validasi properti menggunakan Joi? Sebelum langsung latihan, kita bahas dulu secara konsep dan teori.

Joi merupakan library JavaScript yang digunakan untuk melakukan validasi data. Ketika menggunakan Joi, validasi akan terasa mudah karena kita bisa mendefinisikan schema secara deklaratif. Sebagai contoh, anggaplah kita memiliki komponen User yang menerima properti:

1. name: string, minimal 2 karakter, wajib diisi.
2. email: string, harus email valid, wajib diisi.
3. gender: string, nilai valid “Male”, “Female” dan “Prefer not to say”, tidak wajib diisi, nilai default “Prefer not to say”.

Di Joi, schema tersebut dapat kita definisikan dengan:
```jsx
import Joi from 'joi';
const userPropsSchema = Joi.object({
  name: Joi.string().min(2).required(),
  email: Joi.string().email({ tlds: true }).required(),
  gender: Joi.string().valid("Male", "Female", "Prefer not to say").default("Prefer not to say"),
});
```

Jika Anda lihat kode di atas, sebetulnya dalam mendefinisikan schema mirip seperti yang kita lakukan pada PropsType API kan? Bedanya, Joi lebih banyak menyediakan opsi validasi yang lebih spesifik. Misalnya, kita bisa menggunakan `.email()` setelah `string()` untuk memastikan nilai string berpola email. Lalu kita juga bisa memberikan batasan pada sebuah nilai yang valid dengan method `.valid()`. Kita juga bisa menggunakan `.required()` untuk menandai nilai mana yang wajib diberikan dan .default() untuk menetapkan nilai default.

Anda bisa eksplorasi lebih dalam API yang disediakan oleh Joi pada [dokumentasi yang tersedia](https://joi.dev/api/?v=17.13.3).

Setelah kita mendefinisikan schema, validasi dilakukan dengan menggunakan method schema.validate(). Method akan mengembalikan hasil validasi yang memiliki dua properti penting:

1. error: properti ini berisi informasi error jika validasi gagal. Kita bisa melihat apa yang menyebabkan validasi gagal. Jika validasi berhasil, properti error akan bernilai null.
2. value: properti ini berisi nilai hasil validasi, termasuk memberikan nilai default pada properti schema yang tidak didefinisikan nilainya.

Berikut contoh kode dalam melakukan validasi data menggunakan Joi.
```jsx
import Joi from 'joi';

function validateUser(userToValidate) {
  const userPropsSchema = Joi.object({
    name: Joi.string().min(2).required(),
    email: Joi.string().email({ tlds: true }).required(),
    gender: Joi.string().valid("Male", "Female", "Prefer not to say").default("Prefer not to say"),
  });

  const validationResult = userPropsSchema.validate(userToValidate, { abortEarly: false });

  if (validationResult.error) {
    const { details } = validationResult.error;
    details.forEach((error) => console.warn(`Validation Error: ${error.message}`));
  }

  return validationResult.value;
}



// contoh penggunaan 
const userInvalid = { name: "A", email: "invalid-email" }; // both name and email are invalid
const userValid = { name: "Alice", email: "alice@example.com" }; // valid user

const userInvalidValidated = validateUser(userInvalid);
const userValidValidated = validateUser(userValid);

console.log(`Validated Invalid User: ${JSON.stringify(userInvalidValidated)}`);
console.log(`Validated Valid User: ${JSON.stringify(userValidValidated)}`);

/**
 * Output:
 * Validation Error: "name" length must be at least 2 characters long
 * Validation Error: "email" must be a valid email
 * Validated Invalid User: { name: 'A', email: 'invalid-email', gender: 'Prefer not to say' }
 * Validated Valid User: {
 *   name: 'Alice',
 *   email: 'alice@example.com',
 *   gender: 'Prefer not to say'
 * }
 */
```

Pada kode di atas, proses validasi kita bungkus dalam fungsi bernama validateUser, Anda bisa fokus ke fungsi ini untuk cara validasi data dengan Joi. Di kode tersebut, jika validasi gagal, kode akan mencetak pesan warning pada console beserta pesan detail kesalahannya. Di akhir, fungsi akan mengembalikan nilai value yang dibawa oleh validationResult sebagai nilai hasil validasi.

Lantas bagaimana jika kita implementasikan untuk validasi React Component props?

Untuk React Functional Component, validasi bisa dilakukan di dalam body function. Agar fungsi validasi dapat _reusable_, buatlah semacam fungsi `validateProps` yang menerima tiga input parameter, yakni `schema`, `props`, dan `componentName` di berkas terpisah.

Berikut adalah contoh kode dalam validasi komponen props menggunakan Joi.

App.js:
```jsx
import React from 'react';
import Joi from 'joi';
import { validateProps } from './utils';
import User from './User';

export default function App() {
  return (
    <>
      <User name="A" email="invalid-email" />
      <User name="Alice" email="alice@example.com" gender="Female" />
    </>
  );
}
```

User.js:
```jsx
import React from 'react';
import Joi from 'joi';
import { validateProps } from './utils';

const userPropsSchema = Joi.object({
  name: Joi.string().min(2).required(),
  email: Joi.string().email({ tlds: true }).required(),
  gender: Joi.string().valid("Male", "Female", "Prefer not to say").default("Prefer not to say"),
});

function User(props) {
  const { name, email, gender } = validateProps(userPropsSchema, props, 'User');

  return (
    <div className="user">
      <p>Name: {name}</p>
      <p>Email: {email}</p>
      <p>Gender: {gender}</p>
    </div>
  );
}

export default User;
```

utils.js:
```jsx
import Joi from 'joi';

export function validateProps(schema, props, componentName) {
  const validationResult = schema.validate(props, { abortEarly: false });

  if (validationResult.error) {
    const { details } = validationResult.error;
    details.forEach((error) =>
      console.warn(`[${componentName}] Validation Error: ${error.message}`)
    );
  }

  return validationResult.value;
}
```

![](Pemrograman/JavaScript/Framework/React/React%20Lanjutan/img/3.png)

Bagaimana? Hasilnya serupa kan dengan ketika kita memanfaatkan PropTypes API? Kita akan diberikan warning ketika terdapat kesalahan ketika memberikan props pada sebuah komponen.

Pertanyaan lain, bagaimana implementasinya jika dilakukan pada Class Component? Memang implementasinya lebih _tricky_, tetapi masih masuk akal untuk dilakukan.

Proses validasi dilakukan di dalam constructor. Yang perlu diperhatikan adalah **kita tidak boleh mengubah nilai props melalui this.props karena props harus tetap bersifat immutable** ([ref](https://legacy.reactjs.org/docs/components-and-props.html#props-are-read-only)). Solusinya nilai props hasil dari proses validasi disimpan di dalam state, misalnya this.state.validatedProps. Di method render(), untuk menggunakan nilai props, alih-alih mengakses melalui this.props, gunakanlah this.state.validatedProps.  
  
Masih cukup simpel kan?

Berikut contoh implementasinya.
```jsx
import React from 'react';
import Joi from 'joi';
import { validateProps } from './utils';
import User from './User';

export default function App() {
  return (
    <>
      <User name="A" email="invalid-email" />
      <User name="Alice" email="alice@example.com" gender="Female" />
    </>
  );
}
```
```jsx
import React from 'react';
import Joi from 'joi';
import { validateProps } from './utils';

const userPropsSchema = Joi.object({
  name: Joi.string().min(2).required(),
  email: Joi.string().email({ tlds: true }).required(),
  gender: Joi.string().valid("Male", "Female", "Prefer not to say").default("Prefer not to say"),
});

class User extends React.Component {
  constructor(props) {
    super(props);

    const validatedProps = validateProps(userPropsSchema, props, "User");

    this.state = { validatedProps };
  }

  render() {
    const { name, email, gender } = this.state.validatedProps;

    return (
      <div className="user">
        <p>Name: {name}</p>
        <p>Email: {email}</p>
        <p>Gender: {gender}</p>
      </div>
    );
  }
}

export default User;
```
```jsx
import Joi from 'joi';

export function validateProps(schema, props, componentName) {
  const validationResult = schema.validate(props, { abortEarly: false });

  if (validationResult.error) {
    const { details } = validationResult.error;
    details.forEach((error) =>
      console.warn(`[${componentName}] Validation Error: ${error.message}`)
    );
  }

  return validationResult.value;
}
```

Singkatnya, penghapusan PropTypes di React v19 tidak menghapus kebutuhan akan validasi properti, yang berubah hanyalah alatnya, bukan prinsipnya. Aplikasi tetap berinteraksi dengan data yang rapuh dan tidak terduga di runtime, sehingga penjagaan kontrak antarkomponen tetap wajib dilakukan. 

Pengalaman Anda dengan PropTypes tetap bernilai sebagai fondasi berpikir tentang bentuk dan kewajiban data, sementara implementasinya kini berubah melalui skema eksplisit menggunakan Joi. 

Dengan tetap mengimplementasi validasi, Anda mempertahankan keandalan UI, memudahkan observabilitas, dan menekan biaya perbaikan, sekaligus memastikan praktik validasi properti di runtime tetap sahih, relevan, dan berumur panjang meskipun PropTypes bukan lagi bagian inti React.