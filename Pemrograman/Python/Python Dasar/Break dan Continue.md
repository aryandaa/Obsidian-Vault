#programming 
sebuah syntax tambahan yang berfungsi untuk membantu dalam loop.
`break` = menghentikan secara paksa program looping jika mendapatkan kondisi tertentu.
`continue` = melewatkan bagian eksekusi pada loop dengan kondisi yang sudah di tentukan.

contoh syntax break:
```python
st = 'Programming'
# fungsi akan di eksekusi selama huruf adalah konsonan
for ch in st:
    if ch in ['a','e','i','o','u']:
        break # stop loop jika menemukan huruf vokal
    print(ch)
print('The end')

#output
P
r
The end
```

contoh syntax continue:
```python
st = 'Programming'
# fungsi akan di eksekusi selama huruf adalah konsonan
for ch in st:
    if ch in ['a','e','i','o','u']:
        continue # skip eksekusi kode dibawah jika huruf vokal
    print(ch)
print('The end')

#output
P
r
g
r
m
m
n
g
The end
```
`continue` hanya melewatkan beberapa proses `print(ch)` dalam program di atas, dimana dalam _string_ `'Programming'` huruf vokal **(o,a, dan i)** tidak dieksekusi oleh `print()`. Berbeda dengan `break`, ketika bertemu dengan huruf vokal **(o,a, dan i)**, `break` langsung menghentikan proses _looping_.

source: https://skilvul.com/courses/python-dasar/lessons/loops/topics/break-vs-continue-keywords/
