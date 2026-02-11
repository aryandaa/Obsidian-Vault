#programming #webdev
Sebelum mengembangkan software, kita butuh document yang namanya Software Requierement Specification (SRS) atau Spesifikasi Kebutuhan Perangkat Lunak (SKPL).

lalu apa itu RSR atau SKPL?

sebuah dokumen yang dibuat sebelum mengembangkan sebuah aplikasi perangkat lunak. Dokumen ini menjelaskan cara kerja dan kebutuhan fungsional maupun non-fungsional dari aplikasi yang digunakan pengguna nantinya. 

Bukan hanya itu saja, berikut keuntungan yang bisa didapatkan dari pembuatan dokumen Spesifikasi Kebutuhan Perangkat Lunak:

- Keuntungan pertama adalah seorang desainer UI/UX dalam tim akan mendapat gambaran sehingga mereka dapat mendesain sesuai kebutuhan aplikasi.
- Selain desainer, tim penguji aplikasi (tester) akan mendapatkan panduan untuk membuat studi kasus dalam proses pengujian aplikasi.
- Bukan hanya dari sisi internal tim saja, pengguna akhir (end user) juga akan mendapatkan gambaran umum terkait aplikasi yang akan dibuat.
- Bahkan, dari sisi investor juga akan mendapatkan gambaran umum terkait fitur apa saja yang ada di dalam aplikasi. Sehingga, membantu mereka untuk mengambil keputusan untuk investasi atau tidak.

kita telah mengetahui dokumen Spesifikasi Kebutuhan Perangkat Lunak (SKPL) memiliki banyak keuntungan bagi tim pengembang aplikasi, pengguna, hingga pihak investor. Sehingga, sebuah dokumen SKPL harus memiliki informasi yang cukup untuk memenuhi semua kebutuhan dari pihak-pihak yang memiliki kepentingan tersebut.

Berikut cakupan elemen yang ada dalam dokumen Spesifikasi Kebutuhan Perangkat Lunak:

- Mulai dari tujuan aplikasi;
- deskripsi umum;
- kebutuhan fungsional dan non fungsional;
- performa aplikasi dalam proses produksi;
- antarmuka eksternal atau bagaimana sebuah aplikasi berinteraksi dengan perangkat keras dan perangkat lunak lainnya;
- hingga batasan sistem aplikasi yang akan dibuat.

apa bedanya sih kebutuhan fungsional dan Non-Fungsional?
Kebutuhan Fungsional adalah fitur utama yang wajib ada di dalam aplikasi tersebut, dan harus menjadi prioritas dalam proses pembuatan.

Sedangkan kebutuhan non fungsional berguna untuk mendukung kebutuhan fungsional yang sudah ada. Tanpa adanya persyaratan non fungsional, sistem aplikasi masih bisa berjalan untuk memenuhi kebutuhan pengguna.

## Cara membuat dokumen SKPL

pertama saya akan membahas dari structure penulisan terlebih dahulu, mengingat banyaknya kontribusi dari berbagai macam stackholder, maka menjelaskan secara rinci akan membantu untuk tim pengembang dan penguji, serta menambahkan informasi tentang kemungkinan maintence aplikasi di masa mendatang.

| Bab                          | Deskripsi                                                                                                                                                                                                                        |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pengantar                    | Menjelaskan secara singkat fungsi dari sistem yang dibuat dan cara kerja aplikasi. Selain itu juga menjelaskan tujuan dari aplikasi yang akan dibuat.                                                                            |
| Glosarium                    | Berisi definisi istilah-istilah teknis yang ada dalam dokumen.                                                                                                                                                                   |
| Kebutuhan Pengguna           | Menjelaskan secara umum layanan yang disediakan sistem untuk pengguna. Deskripsi yang ada bisa menggunakan narasi biasa atau diagram supaya dapat dimengerti.                                                                    |
| Sistem Arsitektur            | Menjelaskan gambaran tingkat tinggi (high level overview) dari sistem arsitektur yang digunakan dalam aplikasi.                                                                                                                  |
| Spesifikasi Kebutuhan Sistem | Menjelaskan secara lebih rinci tentang kebutuhan fungsional dan non fungsional dari aplikasi yang akan dibuat. Selain itu jika sistem memiliki antarmuka dengan sistem atau perangkat keras lain juga dapat ditambahkan di sini. |
| Model Sistem                 | Menjelaskan object model, data-flow models, atau semantic data models yang digunakan dalam aplikasi.                                                                                                                             |
| Rencana Pengembangan Sistem  | Menjelaskan asumsi Anda terkait rencana pengembangan sistem di masa depan. Bagian ini akan berguna bagi desainer aplikasi untuk tidak membatasi idenya untuk kemungkinan pengembangan sistem.                                    |
| Apendiks                     | Menjelaskan detail tambahan yang mendukung pengembangan aplikasi                                                                                                                                                                 |


setelah memahami structure dari dokumen SKPL, next saya akan mencontohkan pembuatan dokumen SKPL dalam study kasus halaman login dan logout pada sesi ini: [[Pembuatan SKPL]]