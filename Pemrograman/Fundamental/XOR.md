#programming 
XOR singkatan dari Exclusive OR. 
Jika sebelumnya dalam logika OR kita mengetahui jika salah satu input saja bernilai 1 (true), maka outputnya pasti bernilai 1 (true). 

Lain halnya dengan XOR yang hanya menghasilkan keluaran 1 (true) ketika kedua inputnya berbeda.

xor pada kebanyakan bahasa pemrograman di simbolkan dengan ^ atau caret

langsung saja saya contohkan dengan table kebenaran:
1 ^ 1 = 0 
1 ^ 0 = 1
0 ^ 1 = 1
0 ^ 0 = 0

berbeda dengan or biasa yang akan menghasilkan nilai true jika salah satunya saja terdapat true.
xor akan mengeluarkan true jika kedua masukan berbeda.

apa yang terjadi jika terdapat lebih dari 2 nilai yang akan di xor? maka akan dilakukan eksekusi dimulai dari kiri, contoh:
1 xor 1 xor 0 xor 0 xor 1

1 xor 1 = 0
0 xor 0 = 0
0 xor 0 = 0
0 xor 1 = 1
jadi jawaban dari 1 xor 1 xor 0 xor 0 xor 1 adalah 1