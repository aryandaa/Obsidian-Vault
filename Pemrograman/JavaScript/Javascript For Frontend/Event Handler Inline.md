#programming 
Mungkin Anda sudah sangat familiar dengan istilah inline. Tahukah Anda bahwa kita bisa menerapkan event handler di dalam tag HTML dan tidak perlu menerapkan sintaks event handler dalam tag `<script>?`

pada code event.html sebelumnya di duplikat ke dalam file EventHandlerInline.html.
tetapi bedanya berikan komentar pada Handler event nya, sehingga kodenya menjadi non-aktif.
```js
// document.getElementById('incrementButton').onclick = increment;
// document.body.onload = welcome;
```

Tenang, semua fiturnya akan kita kembalikan melalui inline event handler, yakni menulis event handler melalui atribut tag HTML (onload dan onclick). 

Tambahkan event handler pada tag `<body>` dan `<button>` sebagai berikut:
```js
onload="welcome()"
onclick="increment()"
```

**Tada!** Semua fungsionalitas telah kembali seperti semula.