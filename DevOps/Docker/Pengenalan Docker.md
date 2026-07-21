#devops
![](img/Pasted%20image%2020260720172550.png)
Jika ingin mendeploay aplikasi kita ke production biasanya melakukan tahapan seperti diatas, pertama bikin aplikasinya terlebih dahulu, entah di java golang dan lain lain yang sudah siap untuk di aplikasikan.

Tapi sebelum di deploy, kita terlebih dahulu menginstall hal hal yang dibutuhkan seperti:
1. web server,
2. database,
3. library,
4. runtime app.
tapi cara tersebut manual dilakukan jika ingin mendeploy aplikasi.

lalu disinilah muncul Docker yang cara penggunaannya sangat berbeda:
![](img/Pasted%20image%2020260720173247.png)
cara deploy di docker akan sedikit berbeda dengan cara manual seperti sebelumnya, yang tadinya kita menginstall component-component yang dibutuhkan server secara manual, 
di docker kita akan membuat package yang sudah membandle semua component-component tersebut, dan ketika di deploy kita cukup packagenya saja yang di deploy ke server tersebut dan akan jadi lebih mudah, jadi di server tersebut kita tidak perlu menginstall 1 1 componentnya. 

apa kelebihannya? akan memudahkan kita untuk mendeploy di banyak node, tinggal deploy packagenya saja di banyak node tersebut tanpa menginstall 1 1 component dari banyak server itu. 

