#programming
setiap hasil dari operasi komparasi adalah boolean jadi cuman ada true (1) atau false (0)
operator tersebut adalah:

# > (lebih besar dari)
	jika operant kiri LEBIH BESAR dari kanan = true
# < (lebih kecil dari)
	jika operant kiri LEBIH KECIL dari kanan = true
# >= (lebih besar sama dengan)
	jika operant kiri LEBIH BESAR atau SAMA DENGAN operant kanan = true
# <= (lebih kecil sama dengan)
	jika operant kiri LEBIH KECIL atau SAMA DENGAN operant kanan = true
# == (sama dengan)
	jika 2 operant bernilai SAMA = true
# != (tidak sama dengan)
	jika 2 operant bernilai TIDAK SAMA = true

```python
#<, >, >=, <=, ==, != itu sama seperti bahasa pemrograman lainnya dipakai dengan cara

hasil = 5 > 3
print (hasil) #hasilnya true

#dan yang lainnya
```

perbandingan untuk variable:
# is (sama dengan)

# is not (tidak sama dengan)
# in (di dalam)
  
"is" dan "is not" itu beda dengan bahasa pemrograman lainnya

"is" sebagai operator komparasi object identity

digunakan untuk memeriksa apakah dua variabel itu sama

```Python
x = 5
y = 5
hasil = x is y

print (hasil) #hasilnya true karena sama
```

``` Python
a = 5
b = 10
hasil = a is b

print (hasil) #hasilnya false karena tidak sama
```

is not adalah lawan dari is:
```Python
x = 5
y = 5
hasil = x is not y

print (hasil) #hasilnya false karena sama
```
 

is dan is not cuman bisa work untuk membandingkan 2 variable yang berbeda, tidak dengan str atau int seperti :

```Python
q = 15
hasil = q is 15

print (hasil) #hasilnya adalah "warning" karena tidak bisa
```

### Perbedaan is dengan ==
is untuk object nya, sedangkan == untuk value dari object tersebut, sebagai contoh:
```python
a = 1
b = 1.0

print(a == b)
# True karena 1 dan 1.0 itu sama
print(a is b)
#False karena object nya dianggap berbeda, karena a adalah variable yang menyimpan data integer, sedangkan b menyimpan data float.
```

sedangkan in digunakan untuk pengecekan apakah ada karakter yang cocok SEBAGIAN di dalam suatu string, contoh:
```python
print('aaa' in 'aaa-bbb-ccc')
print('bbb' in 'aaa-bbb-ccc')
print('ddd' in 'aaa-bbb-ccc')

#output
True
True
False
```

walaupun string yang dilakukan itu sangat panjang, tapi jika ada karakter yang dicari, maka hasilnya tetap true:
```python
print('yanda' in 'muhammadaryandasanggadiennata')
#output
True
```
