#programming 
pass keyword adalah keyword penyelamat ketika kita membuat sebuah function seperti if, fo, while, def, mapun class, tetapi bingung mau di isi oleh action apa.

pass = null, yang artinya code tetap mengeksekusi code tersebut tetapi tidak muncul output apapun ketika di jalankan, karena secara default ketika function tidak berisi action apapun, code akan error, contoh penggunaan:
```python
for i in range(5):
    pass
```
code tersebut tetap bisa di jalankan, tetapi tidak ada outputnya.
contoh lain:

```python
def func():
    pass

func()
```

