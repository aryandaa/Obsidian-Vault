#programming 
Pembicaraan style tidak hanya berlaku pada saat kita berurusan dengan keindahan, seperti dalam lukisan, fashion, dan arsitektur bangunan. Bisa dibilang mereka adalah sebuah seni. Dalam konteks pemrograman, JavaScript juga memiliki style guide yang mengedepankan konsistensi penulisan kode.

Konsistensi menjadi hal yang sangat penting dalam pengembangan aplikasi. Meskipun sebetulnya hal tersebut tidak berpengaruh terhadap validitas sintaks kode JavaScript. Namun, ini akan berpengaruh pada banyak hal jika tidak kita tanamkan ke setiap developer.

Anda sudah belajar banyak dengan fitur-fitur JavaScript, bukan? Pada satu tujuan, ada beberapa cara yang bisa diambil dan preferensi para developer dapat berbeda. Bahkan, ini terjadi pada hal kecil dalam kehidupan, layaknya metode penyantapan bubur ayam, ada yang suka diaduk ataupun tidak. Keterbukaan pendapat inilah yang menyebabkan inkonsistensi terjadi dalam kolaborasi proyek ataupun perusahaan. Kita membutuhkan sebuah konvensi atau panduan agar semua tertata rapi dan konsisten. Inilah tujuan dari style guide dalam JavaScript.

Mari kita ambil beberapa contoh.

- Penggunaan tanda titik-koma (semicolon).
- Gaya nama variabel.
- Penempatan komentar dalam kode.
- Penggunaan block-code (curly-bracket), seperti dalam percabangan.
- Banyak assignment secara sekaligus dan masih banyak lainnya lagi.

Agar terbayang, kami punya contoh kode program yang inkonsisten. Silakan perhatikan kode berikut.Anda sudah belajar banyak dengan fitur-fitur JavaScript, bukan? Pada satu tujuan, ada beberapa cara yang bisa diambil dan preferensi para developer dapat berbeda. Bahkan, ini terjadi pada hal kecil dalam kehidupan, layaknya metode penyantapan bubur ayam, ada yang suka diaduk ataupun tidak. Keterbukaan pendapat inilah yang menyebabkan inkonsistensi terjadi dalam kolaborasi proyek ataupun perusahaan. Kita membutuhkan sebuah konvensi atau panduan agar semua tertata rapi dan konsisten. Inilah tujuan dari style guide dalam JavaScript.

Mari kita ambil beberapa contoh.

- Penggunaan tanda titik-koma (semicolon).
- Gaya nama variabel.
- Penempatan komentar dalam kode.
- Penggunaan block-code (curly-bracket), seperti dalam percabangan.
- Banyak assignment secara sekaligus dan masih banyak lainnya lagi.

Agar terbayang, kami punya contoh kode program yang inkonsisten. Silakan perhatikan kode berikut.

```js
let no = 'Semicolon'
 
const my_favorite_color = '#112C85';
 
let myNumber = 3;
console.log(myNumber);
 
var random = 1; // declaring random to 1
 
if (foo) foo++;
 
let a = b = c = 5;
```

Bagaimana pengalaman membaca kode Anda dari contoh di atas? Kami yakin Anda merasa tidak nyaman dan mungkin jiwa kerapiannya bergejolak. Nah, di sinilah konvensi penulisan kode dibutuhkan. Ada dua cara yang bisa kami bagikan dan ulas untuk mengatasi masalah ini, yaitu manual dan otomatis. Metode otomatis akan kami bahas dalam materi berikutnya.

Metode manual didefinisikan sebagai penyediaan dokumentasi style guide secara tertulis dan mengikuti aturan tersebut. Misalnya perusahaan kita atau diri kita secara personal memiliki halaman dokumentasi style guide dalam bentuk apa pun. Kita tinggal memahami dan selalu berpatokan pada panduan tersebut agar konsistensi tetap terjaga.

Kami memiliki contoh dokumentasi style guide yang dapat Anda akses [di sini](https://style-guide-sample.netlify.app/). Misalnya, kita akan memperbaiki kode di atas agar mengikuti aturan di sana. Berikut hasilnya.

```js
const no = 'Semicolon';
 
const myFavoriteColor = '#112C85';
 
const myNumber = 3;
console.log(myNumber);
 
// declaring random to 1
const random = 1;
 
if (foo) {
  foo++;
}
 
let a = 5;
let b = 5; 
let c = 5;
```

Kode yang tidak konsisten mungkin memiliki keuntungan tersendiri, seperti lebih cepat, fleksibel, dan sangat bebas. Namun, itu tidak sebanding dengan dampak negatif yang mungkin terjadi, terutama dalam kolaborasi.

- Kode sulit dibaca dan dipelajari oleh sesama kolega developer sehingga produktivitas menurun.
- Kolaborasi menjadi sulit terjalin dengan baik, apalagi saat mengalami penggabungan dua buah perubahan kode dari developer yang berbeda.
- Jika ada developer baru, proses onboarding pun akan membutuhkan waktu lebih untuk memahami kode.

Di luar poin-poin di atas, beberapa kemungkinan dampak negatif lainnya bisa saja terjadi. Alangkah lebih baiknya bila kita antisipasi dan peringatkan sedini mungkin. Nah, secara tidak langsung, kita sudah menjadi developer JavaScript yang selangkah lebih baik dari lainnya. Mungkin, cara ini perlu kesadaran diri yang tinggi dan ketelatenan kuat. Namun, bagi yang memiliki code reviewer, kode kita bisa dicek dan divalidasi lebih lanjut lagi.