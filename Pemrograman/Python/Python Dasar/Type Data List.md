#programming 
type data list merupakan sebuah type data yang banyak menyimpan berbagai jenis tipe data lagi di dalamnya, list memiliki address atau alamat yang digunakan untuk mempermudah pemanggilan isi dari data tersebut, aadress itu di sebut dengan "index".
index dari list dimulai dari 0 dan seterusnya.
contoh:
```python
list = ["satu", 2, 3.0, "empat"]
```
"satu" berindex 0, jadi jika ingin memanggilnya kita bisa menggunakan
```python
print (list[0])
```
value 2 beindex 1, 
3.0 berindex 2
"empat" berindex 3
dan seterusnya...

selain meletakan type data tetap, kita juga bisa meletakan function ke dalamnya:
```python
list4 = ["satu", 2, 3.0, "empat", list(range(1, 10))]
```
output ketika dipanggil:
`['satu', 2, 3.0, 'empat', [1, 2, 3, 4, 5, 6, 7, 8, 9]]`

# Addition & Deletion
seperti data yang lain, list juga bisa kitaq tambahkan datanya, ada beberapa cara untuk menambahkan data dalam list,
yang pertama dengan +
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print (list3)
```
output:
`[1, 2, 3, 4, 5, 6]`

selain dengan +, bisa juga dengan `append()`, untuk menambahkan data langsung ke dalamnya.
```python
list1 = [1, 2, 3]
list1.append(4)
print (list1)
```
output:
1, 2, 3, 4

selain menambahkan bisa juga menghapusnya dengan syntax `del` dimuka variable list
```python
n_list = [11,22,33,44,55,66]
print(n_list) # print seluruh items

del n_list[3] # delete 44
print(n_list)

#output
[11,22,33,44,55,66]
[11,22,33,55,66]
```
tapi dengan syntax  `remove()` kita bisa menghapus valuenya langsung berdasarkan datanya tanpa mengindex-kan terlebih dahulu

```python
n_list = [11,22,33,44,55,66]
print(n_list)

n_list.remove(44)
print(n_list)

#output
[11,22,33,44,55,66]
[11,22,33,55,66]
```

kita tidak inginmenghapusnya tapi ingin memindahkannya ke variable lain? ada yang namanya `pop()`
```python
n_list = [10,20,30]
print(n_list) # print seluruh items

n = n_list.pop()
print('n = ',n)
print('n_list =',n_list)

#output
[10,20,30]
n = 30
n_list = [10,20]
```

pop() berfungsi untuk memindahkan data yang ada di dalam list ke dalam variable lain, tetapi yang di list tersebut bakal hilang.

# Slicing List
Dalam bahasa pemrograman Python kita dapat melakukan _slicing_ terhadap _list_ yang kita punya. _Slicing_ sendiri berarti **mengiris bagian tertentu dari sebuah _list_**. Untuk melakukan _slicing_ kita dapat gunakan sintaks `list_name[start:end]` untuk menyatakan _section_ yang kita mau pisahkan.
contoh pengunaan:
```python
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print (list1[1:5])
#2, 3, 4, 5

print (list1[5:8])
#6, 7, 8
```

beberapa syntax untuk melakukan Slicing:

![[Pasted image 20260123213948.png]]


