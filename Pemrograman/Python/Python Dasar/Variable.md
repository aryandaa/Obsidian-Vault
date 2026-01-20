#programming
Fungsi variable di python sama saja dengan bahasa yang lain, yaitu wadah untuk menyimpan data. tetapi di dalam python jika membuat variable tidak memerlukan titik koma di ujung seperti php.

ini adalah variable nya

```python
i = "aku"
love = "suka"
you = "kamu"
```

untuk penamaan assignment kita bebas memberikan nama apa, tetapi ada peraturan yang tidak boleh di langgar.

peraturan penulisan assignment variable:
1. tidak boleh ada spasi
	Contoh salah: `"nilai y = 15"`
	jika ada spasi bisa diganti dengan underscore seperti ini `nilai_y = 15`
	
2. tidak boleh ada angka di depan
	Contoh salah : `1juta = 1000000`
	kita bisa menggantinya dengan huruf atau taruh angka di belakang
	`SatuJuta = 1000000`
	Atau
	`Juta1 = 1000000`

  
untuk mengeluarkan varialenya kita gunakan print, dan koma untuk pembatas antara variable atau text

kita bisa menaruh variablenya dimana saja, tanpa harus berurutan

```Python
print(i, love, you)
print("aku", love, "kamu")
print(i, love, "tempe")
print(you, "sedang" ,i, "sedang belajar")
```

## Assignment Indirect

```python
a = 7
print(a)
b = a
print(b)
```

maka outputnya menjadi 7 karena variable b memanggil variable a yang memiliki nilai 7.
