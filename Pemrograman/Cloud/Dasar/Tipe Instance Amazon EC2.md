#cloud 
Instance family di Amazon EC2 memiliki fungsi yang berbeda-beda. Di antaranya ada _general purpose_, _compute optimized_, _memory optimized_, _accelerated computing_ (komputasi terakselerasi), dan _storage optimized_. Berikut uraiannya:

- **General purpose instances** (Instance tujuan umum)  
    Tipe ini memberikan keseimbangan yang baik dari segi sumber daya komputasi, memori, dan jaringan. Selain itu, opsi ini juga dapat digunakan untuk berbagai beban kerja yang beragam seperti server aplikasi web atau repositori kode.  
      
    
- **Compute optimized instances** (Instance teroptimasi untuk komputasi)  
    Tipe yang satu ini ideal untuk tugas komputasi yang intensif dan berpusat pada prosesor dengan performa tinggi, seperti _server game_, HPC (high-performance computing/komputasi dengan performa tinggi), atau bahkan pemodelan ilmiah.  
      
    Anda juga bisa menggunakan tipe compute optimized instances untuk beban kerja _batch processing_ yang membutuhkan banyak proses transaksi di satu grup.  
      
    
- **Memory optimized instances** (Instance teroptimasi untuk memori)  
    Opsi ini didesain untuk memberikan performa tinggi untuk beban kerja yang memproses kumpulan data besar di dalam memori, seperti relasional dan nonrelasional database atau HPC (high-performance computing).  
      
    
- **Accelerated computing instances** (Instance terakselerasi untuk komputasi)  
    Tipe ini menggunakan perangkat keras akselerator untuk menjalankan beberapa fungsi secara lebih efisien dibandingkan dengan perangkat lunak yang berjalan pada CPU. Contohnya adalah penghitungan bilangan floating-point, pemrosesan grafik, dan _data pattern matching_ (pencocokan pola data).  
      
    
- **Storage optimized instance** (Instance teroptimasi untuk penyimpanan)  
    Opsi ini didesain untuk beban kerja yang membutuhkan akses _read_ (baca) dan _write_ (tulis) yang tinggi dan berurutan untuk kumpulan data yang besar di penyimpanan lokal.  
      
    Contoh beban kerja yang sesuai untuk tipe ini mencakup sistem file terdistribusi, aplikasi data warehousing (gudang data), dan sistem _online transaction processing_ (OLTP) berfrekuensi tinggi.  
      
    Dalam komputasi, istilah _input/output operation per second_ (IOPS) adalah metrik yang mengukur kinerja perangkat penyimpanan. Ini menunjukkan berapa banyak operasi _input_ atau _output_ yang dapat dilakukan oleh perangkat dalam satu detik.  
      
    Singkatnya, Anda dapat menganggap operasi input sebagai data yang dimasukkan ke dalam sistem, seperti data yang dimasukkan ke dalam database. Sedangkan operasi output adalah data yang dihasilkan oleh sistem. Contoh output adalah hasil analitik yang dilakukan pada data dalam database.  
      
    Jika Anda memiliki aplikasi yang memerlukan IOPS tinggi, _storage optimized instance_ dapat memberikan kinerja yang lebih baik dibandingkan dengan tipe lain yang tak teroptimasi untuk jenis kasus penggunaan ini.

Jika dianalogikan ke dalam skenario kedai kopi, kasir itu akan menjadi memory optimized instance, barista menjadi compute optimized instance, dan si pembuat seni pada _latte_ adalah accelerated computing instance. Itulah tipe instance pada Amazon EC2.

