#programming 
function yang digunakan untuk melakukan pengulangan atau looping.
ada bermacam macam cara yang digunakan untuk perulangan:
1. For
2. while


## For Syntax
Syntax for berfungsi untuk perulangan seperti biasa, yaitu melakukan perulangan dengan jangka yang sudah di tentukan.
contoh penggunaan:
```python
for i in range (5):
    print (i,".rodok")

print("\n")
```

di dalam For harus ada variable untuk menyimpan hasil dari perulangan tersebut, dan ketika ingin melakukan aksi, maka yang dipanggil adalah variable yang sudah di tentukan itu.
dalam kasus saya diatas, saya menggunakan variable " i ",  dengan range (5) yang artinya saya mengulang sebanyak 5 kali...
dan aksinya tersebut saya memanggil variable " i " sebagai perulangan dan string sebagai kalimat yang ingin di looping.

kita juga bisa menggunakan list sebagai bahan perulangan:
```python
fruits = ['apple', 'banana', 'cherry']
for i in fruits:
    print(i)
```
outputnya adalah semua yang ada di dalam list tersebut.


## While Syntax
Berbeda dengan For. Perulangan While akan berhenti jika kondisinya sudah False, jadi selagi nilainya True. sistemnya akan terus berjalan.
contoh penggunaan:
```python
i = 0
while i < 5:
	print (i)
	i += 1
```
output:
 1
 2
 3
 4

5 nya tidak di tampilkan karena i = 5, kecuali menggunakan 1 <= 5.

sesuai pernyataan diatas perulangan akan terus berjalan selagi bernilai true, kenapa? karena logic nya seperti ini:
1 = 0, di cek apakah 0 < 5? jika true maka lanjut.
lalu i = 1, terus di cek lagi, apakah 1 < 5? true, lanjut lagi ke bilangan selanjutnya,
jika sudah mencapai 5, maka dilakukan lagi pengecekan, apakah 5 > 5, dan hasilnya false 
karena 5 = 5, 
maka code akan berakhir di sebelum angka 5 yaitu 4.

kalo dilihat cara kerja while loop ini seperti cara kerja If, selagi bernilai true, maka akan terus berjalan.

selanjutkan akan membahas [[Nested Loop]] yaitu loop di dalam loop sebagai tambahan perulangan