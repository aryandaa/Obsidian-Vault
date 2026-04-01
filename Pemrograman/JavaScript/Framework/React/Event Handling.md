#programming 
Mungkin kami sudah berkali-kali mengatakan bahwa perubahan data terjadi karena ada input atau interaksi pengguna. Pertanyaannya, bagaimana cara menangkap interaksi pengguna di React, contohnya seperti mendeteksi adanya aksi click pada sebuah tombol? Oke mari kita bahas.

Jika Anda sudah familier dengan DOM manipulation dan event handling, seharusnya memahami cara kerja event handling di React tidaklah susah. Sejatinya event handling di React mirip dengan apa yang kita lakukan pada DOM element. Contohnya, secara standar kita dapat menetapkan event pada element dengan cara seperti ini.

```jsx
<button onclick="increaseValue()">
  Increase Value
</button>
```
Berbeda dengan React, untuk menetapkan event, Anda dapat melakukannya dengan cara seperti berikut.
```jsx
<button onClick={increaseValue}>
  Increase Value
</button>
```

Dalam pemberian nama event, alih-alih menggunakan _lowercase_, React selalu menggunakan camelCase. Jadi penulisan event _onclick_ di React adalah **onClick**. Daftar props selengkapnya dapat dicek di [dokumentasi resmi React ini](https://react.dev/reference/react-dom/components/common#common).

Ketika menggunakan React, Anda juga tidak perlu lagi menggunakan perintah **addEventListener()** untuk menetapkan event setelah element ditampilkan pada DOM. Cukup sediakan event handler pada React element secara langsung melalui properti.

### Props Drilling Event Handler

Data atau _state_ sebaiknya berada di parent component dan hanya boleh diubah oleh komponen itu sendiri sehingga fungsi handler_--yang notabene akan mengubah state--_haruslah berada di parent component.

Ketika Anda memecah belah komponen menjadi komponen yang lebih kecil, kemungkinan Anda akan menemukan kasus di mana component yang menerima input pengguna_--contohnya tombol--_dibuat secara terpisah dari parent component. Ketika ini terjadi, Anda perlu memberikan event handler melalui **props** secara _drilling_. Hal ini sangat umum dilakukan karena React menganut konsep [_unidirectional data flow_](https://legacy.reactjs.org/docs/state-and-lifecycle.html#the-data-flows-down).

Perhatikan bagan berikut.
![](img/Pasted%20image%2020260323182823.png)

State **count** hidup di dalam component **CounterApp** yang merupakan parent component dari seluruh komponen yang ditampilkan. Karena CounterApp pemilik data, maka ia-lah yang berhak memperbarui datanya melalui fungsi **onIncreaseEventHandler** yang dimilikinya.

Bagan di atas menunjukkan bahwa kita memecah UI berdasarkan tugas. Tugas pertama yaitu menampilkan data **count** didelegasikan pada component **CounterScreen** sehingga komponen tersebut diberikan data _count_ oleh parent (CounterApp) melalui **props**.

Selanjutnya, tugas keduanya yaitu menerima input_--untuk menambah nilai count--_yang didelegasikan kepada component **IncreaseButton**. Di sinilah praktik props drilling event handler dilakukan. _IncreaseButton_ tidak berhak untuk mengubah data **count**, itulah sebabnya ia diberikan fungsi handler milik parent melalui props. Nantinya fungsi handler digunakan ketika _IncreaseButton_ menerima sinyal input (_click_) dari pengguna.

Data yang disimpan di dalam state bersifat reaktif. Jika datanya berubah, ia akan me-render ulang komponen yang ditampilkan sehingga data yang tampak akan selalu _up-to-date_.