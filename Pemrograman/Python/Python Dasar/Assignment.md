#programming 
Fungsi Assignment pada python yaitu untuk penyingkatan penulisan variable yang terlalu panjang hanya dengan 1 variable utama saja, contoh:

```Python
a = 1
b = a + 1
```
jika kita menulis itu secara terus menerus maka akan memakan banyak memori pada code, jadi kita bisa menggunakan Assignment sebagai penyingkatan, hanya dengan menulisnya seperti ini

``` Python
a += 1 #sama dengan a = a + 1
b *= 2
C -= 5
d /= 2
e %= 3
f **= 2
```

selain untuk aritmatika, Assignment juga bisa digunakan untuk logika seperti OR AND XOR NOT.
```Python
x = 5
x += (x > 3)
print(x)
```
output = 6 
karena x = 5 + 1 (true) = 6
