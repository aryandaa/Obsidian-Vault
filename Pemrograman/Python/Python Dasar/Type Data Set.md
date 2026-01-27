#programming 
Type data set adalah type data yang mirip dengan List, tapi ada ketentuannya sendiri, yaitu:
1. Tidak boleh ada data yang sama/duplikat, yang artinya datanya bersifat uniqe.
2. set merupakan type data Unordered atau bisa muncul dalam urutan yang berbeda, jadi di type data ini tidak bisa menggunakan index seperti List atau Key seperti Dictionary.
3. Type data set juga bersifat Mutable, atau tidak bisa di ubah setelah membuatnya.

ada beberapa cara untuk membuat type data set:
```python
#1 : Empty set
set0 = set()

#2 : Basic set
set1 = (1, 2, 3)

#3 : From Tuple
tuple1 = (1, 2, 3)
settuple = set(tuple1)

#4 : From List
list1 = [1, 2, 3]
setlist = set(list1)
```

cara penerapan:
From List
```python
days_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat' , 'Sun' ] # list
days_set = set(days_list) # membuat set dari list
print(days_set)

#output
{'Sun', 'Sat', 'Wed', 'Fri', 'Thu', 'Mon', 'Tue'}
```

From Tuple
```python
fruits_tuple = ('apple','orange','water melon')
fruits_set = set(fruits_tuple) # membuat set dari tuple
print(fruits_set)

#output
{'water melon', 'apple', 'orange'}
```

# Syntax tambahan untuk set
Terdapat operator yang bisa kita gunakan untuk type data ini, yaitu
- | untuk Union
- & untuk Intersection
- - untuk difference of set,
- ^ untuk symmetric difference

contohnya disini saya memiliki 2 type data set:
```python
s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}
```

### | atau Union 
berfungsi untuk mengambil semua data dari set 1 dan set 2, 
cara menggunakannya seperti ini:
```python
s1.union(s2)
print(s1)
```
outputnya = {1, 2, 3, 4, 5, 6, 7, 8, 9}


### & atau Intersection 
berfungsi mengambil data yang terdapat pada set1 dan set2, atau cuman menampilkan persamaannya.
```python
s1.intersection(s2)
print(s1)
```
output = {4, 5, 6}

### - atau difference
berfungsi mengambil data unik dari salah satu 2 variable set, tetapi penulisan untuk ini sangatlah harus di perhatikan, karena s1-s2 dengan s2-s1 samgatlah berbeda.
jika s1-s2 artinya program akan mengambil data yang hanya dari s1 dan tidak ada di s2, sedangkan
s2-s1 sebaliknya,
```python
s1.difference(s2)
```
output = {1, 2, 3}

### ^ atau Symmetric difference
ini adalah kebalikan dari Intersection, yaitu mengambil data yang uniq saja, atau mengabaikan data jika ada yang sama antara 2 set.
```python
s1.symmetric_difference(s2)
```
output = {1, 2, 3, 7, 8, 9}

# Superset dan Subset
- superset adalah sebutan untuk set apabila set Mengandung Semua element dari set lain.
- dan Subset apabila seluruh elemen Terkandung dari set lain.

untuk lebih jelas, perhatikan ini:
```python
A = {1,2}
B = {1,2,3}
```
`B` merupakan _superset_ dari `A` karena `B` mengandung seluruh elemen dari `A`.
sedangkan
`A` adalah _subset_ dari `B` karena semua elemen `A` terkandung dalam `B`.

ada beberapa syntax untuk melakukan validasi untuk superset dan subset ini
```python
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3}
s3 = {1, 2, 6}

s2.issubset(s1) #apakah s2 adalah subset dari s1?
True
#karena 1, 2, 3 (s2), ada di dalam 1, 2, 3, 4, 5

s3.issubset(s1)
False
#karena 6 di s3 tidak ada di s1

s1.issuperset(s2)
True
#karena ada 1, 2, 3 di s1 yang itu adalah data dari s2

s1.issuperset(s3)
False
#karena tidak ada 6 di data nya s1
```

