#programming 
DIctionary adalah sebuah type data yang memiliki pasangan antara Key dan Value.
Dict mirip dengan List, bedanya DIct memiliki Key setiap Value nya yang berfungsi jika melakukan pemanggilan maupun modifikasi, Key di Dict bersifat Uniqe yang artinya tidak boleh sama dengan Key yang lain. 

cara mendeklarasikan Dict dengan cara berikut:
`Dict {key : value, key : value}`

kita bisa menyimpan berapapun data di dalamnya:
contoh:
```python
person = {
	'Name' : 'Jhon Doe', 
	'Age' : 26, 
	'Weight' : 82 
	}
```
untuk penulisan bisa dengan cara langsung menyambung, bisa juga dipisah dengan indentasi agar terlihat rapi.

untuk pemanggilan valuenya tidak seperti tuple atau list yang sudah memiliki address/index yang berurutan mulai dari 0, di Dictionary ini memanggilnya dengan cara menyebutkan keynya.
```python
print (person[Name])
#Jhon Doe

print (person[Age])
#26

print (person[Weight])
#82
```

# Modify
kita juga bisa memanifulasi Dict seperti type data immutable yang lain...

pertama saya akan mencontohkan cara Menambahkan terlebih dahulu:
untuk menambahkan bisa dengan structure begini
`nama_dictionary[nama_key] = Value`

agar lebih jelas, langsung saya contohkan saja
```python
person = {'Name': 'David Doe', 'Age': 26, 'Weight' : 82}
person['Job'] = 'Data Scientist' # Key baru: masukkan nilai dari key tersebut
print(person)
#output
{'Name': 'David Doe', 'Age': 26, 'Weight' : 82, 'Job': 'Data Scientist'}
```


kedua ada untuk mengedit
```python
person = {'Name': 'David Doe', 'Age': 26, 'Weight' : 82}
person['Age'] = 27 # Ubah value dari key yang sudah ada 'Age' 
print(person)
#output
{'Name': 'David Doe', 'Age': 27, 'Weight' : 82}
```
konsepnya sama seperti menimpa variable, membuat dict yang baru, terus yang lama bakal tertimpa.

Yang terakhir ada menghapus
```python
person = {'Name': 'David Doe', 'Age': 26, 'Weight' : 82}
del person['Age'] # Delete value dari key yang sudah ada 'Age' 
print(person)
#output
{'Name': 'David Doe','Weight' : 82}
```
sama seperti list, menggunakan syntax del
