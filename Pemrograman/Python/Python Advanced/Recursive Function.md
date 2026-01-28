#programming 
Recursive Function adalah teknik dimana function memanggil dirinya di dalam function untuk melakukan proses, ini biasanya digunakan untuk membuat program yang ribet dan mengharuskan memiliki banyak proses di dalamnya...
contoh:
```python
def factorial(n): # membuat function untuk factorial
  if n <= 1: # untuk melakukan termination/pemutusan recursive function
    return 1
  else:
    return n * factorial(n-1) # implementasi dari recursive function 

n = 5
print(f"factorial dari {n} adalah {factorial(n)}")

#output
factorial dari 5 adalah 120
```
