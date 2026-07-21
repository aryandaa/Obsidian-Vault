#jaringan 
**Graphics Processing Unit (GPU)** atau **Unit Pemrosesan Grafis** adalah prosesor khusus yang dirancang untuk melakukan pemrosesan grafis dan berbagai perhitungan secara paralel dengan sangat cepat.

GPU dapat ditemukan pada berbagai perangkat, seperti kartu grafis (_graphics card_), motherboard, laptop, smartphone, konsol permainan, dan komputer pribadi.

Awalnya, GPU dikembangkan untuk mempercepat proses pembuatan dan pengolahan gambar. GPU melakukan berbagai perhitungan yang diperlukan untuk menghasilkan tampilan visual, seperti menentukan posisi objek, mengolah warna, tekstur, pencahayaan, dan akhirnya menghasilkan gambar yang ditampilkan pada layar.

Salah satu keunggulan utama GPU adalah kemampuannya melakukan **banyak perhitungan secara paralel**. GPU memiliki banyak unit pemrosesan yang dapat menjalankan operasi serupa terhadap sejumlah besar data secara bersamaan.

Kemampuan tersebut membuat GPU tidak hanya digunakan untuk pemrosesan grafis. Saat ini, GPU juga digunakan untuk berbagai pekerjaan komputasi seperti **Machine Learning (ML), Artificial Intelligence (AI), simulasi ilmiah, pengolahan video, dan beberapa jenis komputasi blockchain**.

### Perkembangan GPU

Sebelum GPU modern berkembang pada tahun 1990-an, pemrosesan grafis komputer banyak bergantung pada CPU dan berbagai perangkat keras grafis khusus yang memiliki kemampuan lebih terbatas.

CPU merupakan prosesor utama yang bertugas menjalankan instruksi program dan mengendalikan berbagai proses dalam sistem komputer. Namun, CPU dirancang sebagai prosesor serbaguna dan tidak selalu efisien untuk melakukan sejumlah besar operasi grafis yang serupa secara bersamaan.

Perkembangan permainan komputer dan teknologi **Computer-Aided Design (CAD)** meningkatkan kebutuhan terhadap pemrosesan grafis yang lebih cepat.

Untuk menghasilkan sebuah gambar digital, komputer harus melakukan perhitungan terhadap sejumlah besar titik gambar atau **pixel**. Semakin tinggi resolusi gambar, semakin banyak pixel yang harus diproses.

Sebagai contoh, layar dengan resolusi **1920 × 1080** memiliki lebih dari **2 juta pixel**. Jika sebuah permainan berjalan pada 60 frame per second (FPS), sistem harus menghasilkan hingga 60 gambar baru setiap detik.

Kebutuhan tersebut mendorong perkembangan prosesor khusus yang dapat melakukan banyak perhitungan secara bersamaan. Dari sinilah GPU modern berkembang.

### GPU dan Parallel Computing

Perbedaan penting antara CPU dan GPU terletak pada cara keduanya menangani pekerjaan.

CPU biasanya memiliki jumlah core yang relatif lebih sedikit, tetapi setiap core dirancang untuk menjalankan instruksi yang kompleks dan beragam.

Sebaliknya, GPU memiliki banyak unit pemrosesan yang lebih sederhana dan dirancang untuk menjalankan sejumlah besar operasi secara paralel.

Sebagai contoh, jika komputer harus melakukan operasi yang sama terhadap satu juta data, GPU dapat membagi pekerjaan tersebut ke banyak unit pemrosesan.

Kemampuan ini dikenal sebagai **parallel computing atau komputasi paralel**.

### CUDA

Pada tahun **2007**, Nvidia memperkenalkan **CUDA (Compute Unified Device Architecture)**.

CUDA adalah platform perangkat lunak dan Application Programming Interface (API) yang memungkinkan developer menggunakan kemampuan komputasi paralel GPU Nvidia untuk menjalankan pekerjaan selain pemrosesan grafis.

Sebelum teknologi seperti CUDA berkembang, GPU terutama digunakan untuk menghasilkan gambar dan grafis. Dengan CUDA, developer dapat menulis program yang memanfaatkan GPU untuk melakukan berbagai perhitungan umum.

Konsep ini dikenal sebagai **General-Purpose Computing on Graphics Processing Units (GPGPU)**.

GPU kemudian mulai digunakan dalam berbagai bidang seperti simulasi ilmiah, pengolahan data, Machine Learning, dan Artificial Intelligence.

### Ray Tracing dan Tensor Cores

Pada perkembangan berikutnya, GPU memperoleh berbagai kemampuan khusus.

Salah satunya adalah **ray tracing**, yaitu teknik rendering yang mensimulasikan perjalanan cahaya dalam sebuah lingkungan virtual.

Ray tracing menghitung bagaimana cahaya bergerak, mengenai objek, dipantulkan, atau menghasilkan bayangan. Teknik ini dapat menghasilkan pencahayaan dan refleksi yang terlihat lebih realistis.

GPU modern juga mulai dilengkapi dengan unit pemrosesan khusus seperti **Tensor Cores**.

Tensor Cores dirancang untuk mempercepat operasi matematika yang banyak digunakan dalam Machine Learning dan Deep Learning, terutama operasi yang melibatkan matriks.

Karena Artificial Intelligence dan Machine Learning membutuhkan sejumlah besar operasi matematika terhadap data, kemampuan pemrosesan paralel GPU sangat sesuai untuk pekerjaan tersebut.

### Penggunaan GPU Saat Ini

Saat ini, GPU tidak hanya digunakan untuk menjalankan permainan atau aplikasi pengolahan grafis.

GPU digunakan dalam berbagai bidang seperti:

- Gaming dan rendering grafis.
- Video editing dan animasi.
- Machine Learning dan Artificial Intelligence.
- Deep Learning.
- Simulasi ilmiah.
- Pengolahan data dalam jumlah besar.
- Beberapa jenis komputasi blockchain dan cryptocurrency.

Kemampuan melakukan sejumlah besar perhitungan secara paralel membuat GPU menjadi salah satu komponen penting dalam perkembangan teknologi komputasi modern.