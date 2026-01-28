#programming 
default parameter adalah parameter yang sudah terlebih dahulu di penuhi argumentnya, jadi ketika kita lupa mendeklarasikan argument pada pemanggilan, code akan mengeksekusi default tersebut dan tidak akan error, cara pengunannnya dengan cara berikan = di samping parameter lalu berikan default valuenya.

```python
def star(a=1)
	for x in range(a):
		print(x)
		
star()
```
output = `1`

Code akan tetap mengeluarkan outputnya bahkan tanpa di deklarasikan argumentnya, karena kita sudah mendeklarasikan value dafault dari parameter tersebut.

default ini juga bisa digunakan apabila parameternya banyak
```python
def nama(orang1="yanda", orang2="adit", orang3="hipni"):
```
