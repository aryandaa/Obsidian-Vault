#programming 
Kita sudah selesai mempelajari praktik pengujian otomatis. Pelajaran penting yang kita dapat adalah menguji program tanpa menjalankannya sama sekali. Cukup bermodalkan module test dan runtime seperti Node.js atau Bun. Selamat! Anda sudah melalui materinya dengan baik.

### Tentukan Konteks, Skenario, dan Ekspektasi

Jika masih ingat dengan kasus pengujian sebelumnya, pasti menemukan bahwa kita selalu memberikan nilai string pada parameter pertama, baik pada describe, it, maupun test. Ini adalah nama dari kasus pengujian yang sedang berusaha kita definisikan. Sebagai pembaca kode, developer akan memahami bagian dan hal yang sedang diuji pada program. Tidak hanya itu, pembaca hasil pengujian pun akan menjadi mudah ketika melihat hasil pengujiannya dalam output Terminal/CMD.

```js
import { it, describe, expect } from 'bun:test';
 
describe('Fitur 1', () => {
  it('harus dapat A', () => {
    expect('A').toBe('A');
  });
 
  it('harus dapat B', () => {
    expect('B').not.toBe('A');
  });
});
```


### Mengikuti Pola AAA

Ada satu pola atau konvensi yang bisa kita terapkan agar pembacaan kode testing makin mudah. Itu adalah pola AAA atau Arrange, Action & Assert. Ketiga A ini adalah sebuah section atau bagian untuk memisahkan kode dalam satu test case guna memudahkan pemahaman pembaca.

- **A pertama - Arrange**: persiapan kode untuk sebelum melakukan eksekusi pengujian fitur. Misalnya, menyiapkan angka yang akan digunakan untuk penjumlahan.
- **A kedua - Action**: eksekusi fitur terjadi dalam bagian ini.
- **A ketiga - Assert**: memastikan antara actual value dan expected value sudah sesuai.

Seharusnya Anda memperhatikan dengan baik latihan kasus kita bahwa terdapat tiga komentar yang berisi AAA. Berikut contoh implementasinya.
```js
import { describe, it, expect } from 'bun:test';
 
function add(numA, numB) {
  return numA + numB;
}
 
describe('Calculator', () => {
  it('should add correctly', () => {
    // Arrange
    const operandA = 1;
    const operandB = 1;
 
    // Action
    const actualValue = add(operandA, operandB);
 
    // Assert
    const expectedValue = 2;
    expect(actualValue).toBe(expectedValue);
  });
});
```


### Definisikan Skenario Positif dan Negatif

Jumlah kasus pengujian berbanding lurus dengan jumlah fitur dalam aplikasi. Ada istilah bernama edge cases, yaitu situasi yang tidak biasa dan jarang terjadi, tetapi bisa menyebabkan masalah jika tidak diantisipasi dengan baik. Edge case dapat mengeluarkan bug fatal yang telah kita lihat sebelumnya. Contoh sederhananya adalah sebuah function bernama `add` sudah selayaknya menerima parameter number. Bagaimana jika kita beri situasi yang tidak umum seperti menggunakan string? Hasilnya akan string, bukan number. Tepat sekali!

Pendekatan yang kami sarankan adalah mulailah membangun skenario-skenario pengujian secara lengkap dengan skenario negatif lebih dahulu dan diikuti dengan skenario positif. Dengan cara seperti ini, kita akan lebih bisa fokus dalam menemukan berbagai edge case. Mengatasi berbagai edge case membantu memastikan bahwa aplikasi atau sistem lebih stabil dan dapat diandalkan dalam berbagai situasi ekstrem.