#programming 
Sebelumnya, kami menyebutkan bahwa JavaScript memberikan banyak keleluasaan dalam menuliskan sintaksisnya. Misalnya, penggunaan semicolon, quotes, atau spacing menjadi preferensi bagi developer. Hal ini menyebabkan gaya penulisan kode tiap developer kerap berbeda dan tidak konsisten.
```js
const myName = 'John'; // using single quote
const yourName = "Jane"; // using double quote
const herName = `Jess`; // using backticks
 
myName === yourName // without semicolon
myName === yourName; // with semicolon
```
Konsistensi gaya penulisan kode menjadi krusial bila aplikasi yang Anda kembangkan besar dan butuh kolaborasi banyak developer. Pasalnya, inkonsistensi gaya penulisan akan menyulitkan komunikasi yang terjadi seperti pada saat code review atau pair programming. Alih-alih fokus mencari potensi bugs, code review banyak membahas masalah inkonsistensi gaya penulisan. 

Untuk meningkatkan konsistensi dalam menulis kode, penting untuk mengikuti dan patuh terhadap style guide.

Style guide dalam konteks bahasa pemrograman JavaScript adalah peraturan mengenai cara penulisan kode yang baik bagi developer secara individu maupun tim. Beberapa style guide yang umum digunakan, memiliki penjelasan lengkap tentang aturan yang harus diikuti oleh developer. Misalnya, aturan penggunaan double atau single quote, indentasi, semicolon, dan deklarasi variabel.

Berikut adalah beberapa alasan style guide mutlak diterapkan oleh developer.

- **Membuat penulisan kode lebih konsisten**  
    Ini merupakan alasan paling mendasar. Kita perlu konsisten dalam menuliskan kode, terutama jika bekerja dengan tim. Selain kode menjadi terlihat rapi, kode juga mudah dibaca oleh rekan tim. Istilah “kode yang baik yaitu kode yang tidak dapat diketahui siapa penulisnya” akan tercapai bila menerapkan style guide.
- **Membantu proses onboarding pada anggota tim baru**  
    Style guide membantu dalam proses komunikasi ketika ada anggota tim baru, terutama bila masih tergolong pemula. Dengan adanya style guide, anggota tim baru dapat beradaptasi dan belajar dengan cepat.
- **Menambah wawasan guna menjadi programmer yang lebih baik**  
    Dengan mengikuti sebuah style guide, secara tidak langsung kita akan menemukan wawasan baru. Contohnya, saat ada style guide yang menggunakan single quote dalam membuat string, di sana Anda bisa menemukan alasan hal tersebut diharuskan.
- **Membantu proses review kode**  
    _Workflow_ dalam membangun produk yang baik tentu berisi proses _review_ kode. Style guide dapat membantu proses review lebih cepat. Ini karena proses review akan fokus terhadap potensi bugs dibandingkan berdebat masalah gaya penulisan.

  

### Style Guide Standard (Code Convention)

Kita sudah tahu pentingnya memiliki dan mengikuti style guide dalam menuliskan kode. Selanjutnya, style guide seperti apa yang perlu kita ikuti? Ketahuilah bahwa style atau gaya sejatinya adalah pilihan personal. Sama seperti kehidupan sehari-hari, gaya berpenampilan atau berbicara setiap orang pasti berbeda-beda. Demikian juga dengan gaya menulis kode, setiap developer berhak menentukan gaya yang ia inginkan.

Namun, pada kasus tertentu, gaya penulisan perlu disepakati. Contohnya, ketika berkolaborasi dengan banyak developer. Tidak benar rasanya bila gaya penulisan antardeveloper berbeda-beda dalam satu proyek yang sama. Ibarat sebuah band yang personilnya bermain di nada dasar yang berbeda-beda, sangat tidak elok.

Setiap gaya pada individu terbentuk secara alami dan inilah tantangan bagi tim dalam menyepakati gaya mana yang akan diterapkan. Tantangan ini dirasakan oleh banyak perusahaan besar sehingga mereka mengembangkan dan menyepakati style guide untuk diikuti oleh developer di perusahaannya. Perusahaan besar seperti Google dan Airbnb mempublikasikan style guide yang mereka kembangkan sehingga dapat dijadikan pedoman bagi seluruh developer di dunia.

Style guide yang sudah disepakati dan direkomendasikan oleh banyak developer itulah yang disebut Code Convention. Kami (Dicoding) dalam menuliskan kode JavaScript di cakupan kelas juga memiliki convention yang dianut sehingga antar kontributor kelas memiliki gaya yang konsisten. Jika Anda tertarik menerapkan aturan-aturannya, Anda bisa simak di: [Dicoding Academy JavaScript Style Guide](https://github.com/dicodingacademy/javascript-style-guide?tab=readme-ov-file).  
  
Secara umum, di JavaScript sendiri terdapat tiga style guide terkenal yang bisa Anda ikuti.

1. [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript)
2. [Google JavaScript Style Guide](https://google.github.io/styleguide/jsguide.html)
3. [Standard JavaScript Style Guide](https://standardjs.com/rules.html)

Ketiga style guide di atas memiliki aturan serta penjelasan lengkap mengenai penulisan kode di JavaScript. Untuk Anda yang belum memiliki atau mengikuti gaya penulisan mana pun, inilah waktunya mulai mengikuti salah satunya. Silakan buka tautan di atas, baca aturannya, dan pilih gaya penulisan yang cocok untuk Anda.