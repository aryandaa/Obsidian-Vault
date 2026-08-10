#devops 
![](Pasted%20image%2020260722155556.png)
apakah docker adalah virtual machine (VM)? tidak, docker adalah container manager. 
contoh: jika kita ingin menyewa server di hosting, kita biasanya akan menyewa VM nya itu, nah beda dengan docker, docker tidak menggunakan konsep Virtual Machine tetapi menggunakan konsep Kontainer.

jadi apa bedanya VM dengan Container? 
jika dilihat dari gambar diatas disitu terdapat perbedaaan, di Vm ada yang namanya Virtual Machine Manager atau Hypervisor, contoh dari Hypervisor ini seperti Virtual Box atau VMware. 
jadi jika kita menginstall Virtual Machine disitu terdapat Operating Sistem, App Dependency dan Application. jika kita ingin membuat 3 maka akan menginstall hal yang sama 3 kali.

Berbeda dengan container, dia tidak memiliki operating sistem di dalam Containernya itu, saat kita bikin container dia akan menggunakan sistem operasi bawaan dari container managernya. 
jadi saat kita membuat banyak contohnya 3, dia akan menggunakan operating sistem yang sama.

Jadi bagusnya adalah container akan di isolate oleh container manager tersebut yang jika ada perubahan di operating sistemnya maka containernya tidak akan berubah, jadi jika Sistem operasi bermasalah, sistem operasi di container itu akan tetap aman.

Jadi keunggulan Container dari VM adalah Container lebih ringan, karna di container itu menggunakan sistem operasi induk. 

salah satu implementasi Container saat ini yang paling Populer adalah Docker atau yang saat ini sedang di pelajari.

dan apakah Container bisa menggantikan fungsi VM di server? kalo tujuan kita untuk mendeploy aplikasi saja, maka bisa bahkan lebih bagus dan efisensi pake Container karna tidak butuh resource yang besar. 
Tapi jika tujuannya menginstall sistem operasi di server maka lebih baik pakai VM.

