#programming 
Arbitrary Argument adalah sebuah teknik yang digunakan untuk function, ini berfungsi ketika kita belum bisa memastikan jumlah argument yang akan digunakan ketika pemanggilan function, jadi code akan menyesuaikan secara otomatis tergantung berapa banyak jumlah argument yang di tambahkan.

Cara menggunakan Arbitrary argument dengan cara menambahkan `*` di depan parameter yang digunakan, contoh
```python
def orang(*names):
    for name in names:
        print (f"hello {name}!")

orang("yanda", "reja", "rifki")

```
output:
```
hello yanda!
hello reja!
hello rifki!
```

dalam function orang, saya menggunakan arbitrary pada parameter names, lalu parameter di teruskan ke dalam for loop.