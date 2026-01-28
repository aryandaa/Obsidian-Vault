#programming 
seperti di bahasa pemrograman lain, python juga memiliki yang namanya function, function ini berfungsi untuk mengumpulkan blok kode untuk melakukan operasi tertentu, agar code tersebut terlihat rapi.

basic structure Function dalam python seperti berikut:

```python
def function_name(function_parameter):
	code1
	code2
	...
	return 
```
- `def` adalah keyword yang digunakan python untuk mendeklarasikan sebuah function
- `function_name` adalah nama function yang di deklarasikan, berfungsi untuk memanggilnya nanti.
- `function_parameter` digunakan sebagai representasi datanya nanti, misalnya:
	- `(a, b, c)` berarti a b dan c ini adalah data yang perlu di isi ketika memanggil functionnya dengan cara:
		`function_name(1, 2, 3)` 1, 2 dan 3 adalah data dari a b c yang sudah di isi.
- `code` berfungsi untuk eksekusi dari parameternya nanti mau di apakan.
- `return` digunakan untuk mengembalikan nilai sesuatu ketika code sudah selesai di jalankan:
	contoh penggunaan: `return output1`


## Call function
penggunaan function bukanlah hal yang wajib, kita juga bisa menjalankan code tanpa function, tetapi function memiliki beberapa keuntungan apabila memakainya:
1. lebih terstructure
2. dapat digunakan kembali untuk program yang lain, jadi tidak perlu menuliskan ulang
3. memudahkan untuk maintence.

cara untuk memanggil function dengan cara memanggil namanya lalu isi parameternya saja
```python
def callstar(start, end):
    for x in range(start, end+1):
        x = "*"
        print (x)

callstar(1, 2)
#output
*
*
```
parameter tersebut adalah representasi dari value yang ingin di tampilkan hasil dari proses functionnya, dan isinya tersebut dinamakan dengan `"argumen"`.


