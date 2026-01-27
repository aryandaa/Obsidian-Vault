#programming 
List 2D adalah list dimana bentuknya bercabang yaitu list berasa di dalam list yang membuatnya seperti berbentuk 2D. sebagai contoh sederhana:
```python
list_array = [[1,2,3],
              [4,5,6],
              [7,8,9]]
```
disini 1-3, 4-6 dan 7-9 berupakan list yang berbeda yang letaknya di dalam 1 list utama.

untuk penyebutan 2D nih dengan row dan Column, dan index-nya juga dimulai dari 0
```
yang menyamping adalah column/kolom:
1,2,3 (kolom 0)
4,5,6 (kolom 1)
7,8,9 (kolom 2)

sedangkan yang menurun adalah row:
1,4,7 (row 0)
2,5,6 (row 1)
3,6,9 (row 2)
```
mengetahui itu sangat penting untuk kita bisa memanggilnya berdasarkan column dan row,
contoh:
```python
list_array[0]

#output
[1,2,3]
```
karena yang dipanggilnya adalah semua isi dari column 0, bagaimana jika ingin mengambil data yang lebih spesifik? kita panggil juga row nya.

```python
list_array[0][2]

#output
3
```
ini artinya "pertama ambil kolom 0 (1,2,3). lalu dari kolom 0 tersebut ambil row 2 (3)", dan yang keluar adalah "3".

