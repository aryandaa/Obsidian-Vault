#programming 
macam macam slash "\" yang bisa digunakan pada string dan berbagai fungsinya

```
\' tanda kutip tunggal

\" tanda kutip ganda

\n baris baru

\t tap (spasi banyak)

\\ backlash itu sendiri

\b menghapus 1 angka terakir dari kata, dan menggabungkannya dengan kata yang di depan
```


contoh penggunaan
```Python
print ('ini adalah hari jum\'at')
print ("andi berkata: \"aku ingin makan ikan\"")
print ("1. baris pertama \n2. baris kedua")
print ("C:\\user\\yanda") #jika tidak menggunakan \\ maka akan menjadi error karena \ 1 anggap karakter special
print ("aku\bsayang\bkamu")
```
```
ini adalah hari jum'at
andi berkata: "aku ingin makan ikan"
1. baris pertama 
2. baris kedua
C:\user\yanda
aksayankamu
```

  
ada juga yang namanya raw string berfungsi untuk mengubah semuanya menjadi string tanpa harus \
```Python
print(r"C:\user\yanda")
print(f"\n\t\b")
#semuanya akan menjadi string biasa tanpa harus kedetect karakter special
```
```
C:\user\yanda
\n\t\b
```

selain (r""), kita juga bisa menggunakan (f"")

  

multiline string berfungsi membungkus semua teks yang di dalamnya menjadi string, termasuk spasi dan enter. jadi seolah olah didalam situ adalah papan tulis
``` Python
print(""""
Nama  : Aryanda
Umur  : !9
Kelas : 2B
Kampus: Poliban
      """)
```