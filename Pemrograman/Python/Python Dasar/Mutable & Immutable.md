#programming  
Ada 2 jenis type data yang bisa di kategorikan, Jenis ini di tentukan dari value type data tersebut apakah bisa diubah atau tidak.
1. immutable (Tidak dapat di ubah)
	1. int
	2. float
	3. string
	4. tuple
2. Mutable (Dapat di ubah)
	1. list
	2. set
	3. dict

jika setelah data di buat dan dapat di ubah, maka artinya data tersebut Mutable, dan jika sebaliknya tidak dapat di ubah, maka artinya Immutable.

list merupakan type data mutable atau bisa di ubha, saya bisa membuktikannya dengan:
```python
buah = ["banana", "strawberry", "cocomelon"]
print (buah)
buah.append("grape")
print (buah)
```
Output:
'banana', 'strawberry', 'cocomelon'
'banana', 'strawberry', 'cocomelon', 'grape'

bisa dilihat variable list diatas hanya menyimpan 3 buah dan saya dapat menambahkannya lagi menjadi 4 buah, hal ini juga bisa terjadi terhadap set dan dict.
tetapi tidak bisa dilakukan kepada yang jenisnya Immutable seperti integer float. string, dan tuple,
jika kita memaksa menambahkan data lagi ke dalam Immutable, maka code akan error.
