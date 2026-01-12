macam macam tipe data yang bisa digunakan dalam bahasa python

1. Integer (angka satuan)
`int = 1`

  2. Float (angka pecahan)
`float = 1.5`

3. String (kumpulan karakter)
`str = "Hello, World!"
`
4. Boolean (benar/salah)
``` python
boolT = True
boolF = False
```

5. List (kumpulan data yang dapat berubah-ubah)
list = [1, 2, 3, 4, "yanda"]

(kalo di bahasa php namanya Array)
index list dimulai dari 0,1,2,3 dst.

``` python
print(list[0])
#berarti hasilnya adalah "1"
```
list dapat menyimpan berbagai type data di dalamnya.
  
6. Set (Kumpulan tipe data yang tidak bisa duplikat)
```python
my_set = {10, 20, 30, 30, 10, 40, 20, 60}
print (my_set)
#output = 10, 20, 30, 40, 60.
```
set tidak bisa duplikat, jadi 30 20 dan 10 yang double diatas akan dihilangkan
  
7. dict (data dalam pasangan key=value)
```Python
my_dict = {
	"nama" : "yanda", 
	"umur" : 19, 
	"kampus" : "poliban"}
	
print(my_dict["nama"])
#Output = yanda
print(my_dict["umur"])
#Output = 19
print(my_dict["kampus"])
#Output = poliban
```

### tipe data khusus:

1. Complex (angka kompleks)

```python
data_compex = complex (5,6)
print (data_compex)
```

dipakai buat bilangan kompleks (yang punya bagian real dan imajiner).
Biasanya, ini dipakai di matematika, fisika, dan teknik yang butuh perhitungan kompleks.