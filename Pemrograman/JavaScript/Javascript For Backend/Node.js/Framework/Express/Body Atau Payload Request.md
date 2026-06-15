#programming 
Ketika menggunakan Node.js, untuk mendapatkan data pada body request--meskipun datanya hanya sebatas teks--kita harus berurusan dengan _**Readable Stream**_. Di mana untuk mendapatkan data melalui stream tak semudah seperti kita menginisialisasikan sebuah nilai pada variabel. 

_Good News!_  
Di Express, Anda tidak perlu lagi repot membaca stream manual. Express sudah menyediakan middleware yang akan otomatis mengubah payload JSON menjadi objek JavaScript yang bisa langsung digunakan.

Untuk dapat membaca body JSON di Express 5, kita perlu menggunakan middleware `express.json()`. Middleware ini akan membaca request dengan `Content-Type: application/json` dan mengubahnya menjadi objek JavaScript pada properti **`req.body`**.

Contoh implementasi:
```js
const app = express();
const port = 3000;
const host = 'localhost';
 
// Middleware untuk parsing JSON body
app.use(express.json());
 
app.post('/login', (req, res) => {
    const { username, password } = req.body;
    res.send(`Welcome ${username}!`);
});
 
app.listen(port, () => {
    console.log('Server berjalan di http://${host}:3000');
});
```

Misalkan client mengirimkan data login dengan struktur:
```json
{
 "username": "harrypotter",
 "password": "encryptedpassword"
}
```

Handler di atas akan bisa langsung mengaksesnya melalui `req.body.username` dan `req.body.password`.