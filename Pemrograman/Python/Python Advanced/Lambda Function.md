#programming 
lambda function adalah function yang lebih singkat dari function biasa/reguler.
function reguler biasanya kita harus mendeklarasikan dengan menuliskan `def` di depannya lalu menuliskan parameter lalu body function, sedangkan lambda Functioon hanya menuliskan `lambda` di awal lalu parameter dan dilanjut dengan aksinya tanpa indentasi.

function reguler:
```python
def add(x, y):
	return x + y
	
print (add(10, 20))
```

function lambda
```python
add = lambda x, y : x+y

print (add(10, 20))
```

lihat, lebih simple dari function biasa, tetapi lambda ini juga memiliki kekurangan yaitu tidak bisa melakukan proses yang rumit seperti perulangan, percabangan, atau penugasan yang kompleks.

karena lambda ini sifatnya `anonym`, jadi ketika terjadi kesalahan susah untuk melakukan tracknya. 

karena banyak kekurangan dari function biasa, jadi kapan kita menggunakan lambda?
ketika membuat fungsi kecil yang hanya sekali pakai, karena lambda lebih sedikit memakan memori dari function reguler.

