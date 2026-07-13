#jaringan 
**Thread** adalah unit terkecil dari proses yang dapat dijadwalkan dan dijalankan oleh CPU. Sebuah thread berisi rangkaian instruksi yang merupakan bagian dari sebuah program atau proses.

Satu program dapat memiliki satu atau beberapa thread. Dengan membagi pekerjaan menjadi beberapa thread, sebuah program dapat mengerjakan beberapa tugas secara bersamaan atau membagi pekerjaan ke beberapa core CPU yang tersedia.

Sebagai contoh, sebuah web browser dapat menggunakan thread yang berbeda untuk menangani beberapa pekerjaan, seperti menampilkan halaman web, menjalankan JavaScript, menangani komunikasi jaringan, dan melakukan proses lainnya.

Sistem operasi menggunakan komponen yang disebut **CPU Scheduler** untuk menentukan thread mana yang akan dijalankan, kapan thread tersebut dijalankan, dan core atau logical processor mana yang akan digunakan.

### Multithreading

**Multithreading** adalah teknik yang memungkinkan sebuah program atau sistem menjalankan beberapa thread.

Sebuah pekerjaan besar dapat dibagi menjadi beberapa thread yang menangani tugas berbeda. Jika CPU memiliki beberapa core, beberapa thread dapat dijalankan secara paralel pada core yang berbeda.

Sebagai contoh, sebuah aplikasi memiliki empat thread:

**Thread 1 → Membaca data**

**Thread 2 → Memproses data**

**Thread 3 → Menangani komunikasi jaringan**

**Thread 4 → Memperbarui tampilan aplikasi**

Pada CPU multi-core, beberapa thread tersebut dapat diproses secara bersamaan. Hal ini dapat meningkatkan performa dan membuat aplikasi lebih responsif.

Namun, tidak semua pekerjaan dapat dibagi menjadi banyak thread. Beberapa tugas memiliki ketergantungan terhadap hasil pekerjaan sebelumnya sehingga harus dijalankan secara berurutan.

### Hyper-Threading

**Hyper-Threading** adalah teknologi multithreading pada hardware yang dikembangkan oleh Intel. Secara umum, konsep ini termasuk dalam teknologi **Simultaneous Multithreading (SMT)**.

Hyper-Threading memungkinkan **satu core fisik dikenali oleh sistem operasi sebagai dua logical processor**.

Sebagai contoh:

**4 Core / 4 Thread**

Sistem operasi melihat 4 logical processor.

Sedangkan CPU dengan:

**4 Core / 8 Thread**

Sistem operasi dapat melihat 8 logical processor.

Dengan Hyper-Threading, satu core fisik dapat menangani instruksi dari dua thread secara lebih efisien. Ketika satu thread sedang menunggu suatu proses, seperti menunggu data dari cache atau memori, core dapat memanfaatkan sebagian sumber daya pemrosesan yang tersedia untuk mengerjakan thread lainnya.

Namun, Hyper-Threading **tidak berarti satu core berubah menjadi dua core fisik**. Kedua logical processor tetap berbagi sumber daya dari core yang sama.

Oleh karena itu, CPU dengan **4 core dan 8 thread tidak memiliki performa yang sama dengan CPU 8 core fisik**. Peningkatan performanya bergantung pada jenis pekerjaan dan kemampuan software dalam memanfaatkan banyak thread.