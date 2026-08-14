#cybersecurity 


Setelah memahami apa itu Digital Forensics, sekarang kita masuk ke bagian yang sebenarnya menjadi pusat dari seluruh kegiatan forensic, yaitu **Digital Evidence**. Kalau forensic adalah proses investigasinya, maka evidence adalah bahan yang kita gunakan untuk membuktikan apa yang terjadi. Seorang forensic analyst tidak bekerja berdasarkan dugaan atau perasaan. Dia bekerja berdasarkan data yang ditinggalkan oleh sistem digital. Karena itu, sebelum belajar membongkar Windows Registry, membaca memory dump, atau mengejar paket jaringan dengan Wireshark seperti detektif yang kurang tidur, kamu harus memahami dulu jenis evidence yang sedang kamu hadapi.

Digital evidence dapat dipahami sebagai **informasi digital yang memiliki nilai dalam suatu investigasi**. Informasi tersebut dapat berasal dari komputer, smartphone, server, jaringan, cloud, aplikasi, database, memory, maupun media penyimpanan lainnya. Evidence tidak selalu berbentuk file yang bisa kamu buka dengan double-click. Bahkan banyak evidence penting justru berada di tempat yang tidak terlihat oleh pengguna biasa.

Misalnya seseorang menghapus sebuah file. Dari sudut pandang pengguna, file tersebut sudah tidak ada. Tetapi dari sudut pandang forensic analyst, belum tentu. Metadata file mungkin masih tersisa, filesystem mungkin masih menyimpan informasi mengenai file tersebut, sebagian data mungkin masih berada di disk, dan artefak lain mungkin menunjukkan bahwa file tersebut pernah ada. Jadi ketika seseorang mengatakan, “File-nya sudah dihapus,” forensic analyst biasanya belum terlalu terkesan. Komputer punya kebiasaan menyimpan jejak dari hal-hal yang menurut manusia sudah selesai.

## Evidence bukan hanya file

Kesalahan yang sering dilakukan pemula adalah menganggap digital evidence berarti “file yang ditemukan di komputer”. Padahal sebuah file hanyalah salah satu bentuk evidence.

Misalnya dalam sebuah kasus kamu menemukan `secret.zip`. Itu memang evidence. Tetapi informasi bahwa file tersebut dibuat pada pukul 02:13 juga bisa menjadi evidence. Informasi bahwa user tertentu mengaksesnya juga bisa menjadi evidence. Informasi bahwa archive tersebut kemudian dikirim melalui koneksi network juga bisa menjadi evidence.

Dengan kata lain, **evidence dapat berupa data maupun informasi mengenai aktivitas yang terjadi pada sistem**.

Bayangkan sebuah komputer sebagai tempat kejadian perkara. Di dunia fisik, investigator bisa menemukan sidik jari, CCTV, DNA, jejak kaki, barang yang dipindahkan, atau saksi. Dalam dunia digital, “jejak kaki” tersebut bisa berupa browser history, registry entries, event logs, file metadata, process information, network connections, dan berbagai artefak lainnya.

Karena itu kita akan sering menggunakan istilah **artifact**. Artifact adalah jejak atau struktur data yang ditinggalkan oleh sistem, aplikasi, atau aktivitas pengguna yang dapat membantu investigasi.

## Volatile dan Non-Volatile Evidence

Salah satu klasifikasi paling penting dalam Digital Forensics adalah membedakan evidence berdasarkan **seberapa mudah evidence tersebut hilang ketika sistem berubah atau dimatikan**.

Evidence yang mudah berubah atau hilang disebut **volatile evidence**. Contoh paling penting adalah RAM atau memory. Ketika komputer sedang menyala, RAM dapat berisi informasi mengenai proses yang sedang berjalan, koneksi jaringan aktif, command yang sedang digunakan, data aplikasi, dan berbagai informasi lain. Ketika komputer dimatikan, sebagian besar isi RAM akan hilang.

Inilah alasan memory forensics menjadi bidang tersendiri. Kalau investigator langsung mematikan komputer tanpa mempertimbangkan kebutuhan acquisition terhadap volatile evidence, beberapa informasi berharga mungkin hilang.

Sebaliknya, **non-volatile evidence** adalah evidence yang relatif tetap bertahan meskipun sistem dimatikan. Contohnya adalah data pada hard disk, SSD, USB storage, atau media penyimpanan lainnya. File, filesystem structures, browser databases, registry hives, dan log yang tersimpan di disk termasuk contoh evidence non-volatile.

Secara sederhana:

**RAM → volatile**

**Hard disk/SSD → non-volatile**

Tetapi jangan menganggap volatile berarti tidak penting dan non-volatile berarti selalu lebih penting. Keduanya menjawab pertanyaan yang berbeda.

Misalnya kamu sedang menangani komputer yang diduga sedang melakukan serangan. RAM mungkin memberikan informasi tentang proses yang sedang berjalan dan koneksi network aktif. Sementara disk dapat memberikan sejarah aktivitas yang sudah terjadi sebelumnya. Kalau kamu ingin mengetahui **apa yang sedang terjadi sekarang**, memory bisa sangat berharga. Kalau kamu ingin mengetahui **apa yang terjadi beberapa jam atau hari sebelumnya**, disk artifacts mungkin lebih berguna.

Inilah mengapa forensic analyst harus mempertimbangkan **order of volatility**, yaitu urutan berdasarkan seberapa cepat suatu data dapat hilang atau berubah.

## Order of Volatility

Konsep order of volatility pada dasarnya mengatakan bahwa ketika mengumpulkan evidence, kita harus memperhatikan evidence yang paling mudah berubah terlebih dahulu.

Contoh sederhananya adalah RAM. RAM dapat berubah hanya karena sistem terus menjalankan proses. Kalau kamu menunggu terlalu lama, isi memory bisa berubah.

Sementara data pada hard disk biasanya lebih persisten. Sebuah file tidak tiba-tiba menghilang hanya karena kamu menunggu beberapa menit, meskipun tentu saja ada pengecualian.

Dalam investigasi nyata, keputusan acquisition tidak sesederhana “selalu ambil RAM dulu”. Investigator harus mempertimbangkan kondisi perangkat, tujuan investigasi, risiko perubahan evidence, prosedur organisasi, dan kebutuhan kasus. Namun sebagai konsep dasar, kamu harus memahami bahwa **data yang lebih volatile membutuhkan perhatian lebih cepat**.

Ini akan menjadi sangat penting ketika kita nanti masuk ke **Memory Forensics**.

## Disk Evidence

Sekarang kita masuk ke salah satu evidence yang paling sering muncul dalam lomba Digital Forensics, yaitu **disk evidence**.

Disk evidence adalah data yang berada pada media penyimpanan seperti HDD, SSD, USB drive, memory card, atau media storage lainnya.

Di dalam disk kamu bisa menemukan filesystem, operating system, aplikasi, dokumen, gambar, browser data, log, registry, temporary files, deleted files, dan berbagai artefak lainnya.

Dalam kompetisi, kamu mungkin diberikan sebuah file seperti: `disk.img`

atau: `evidence.E01`

atau: `forensic.dd`

File tersebut bisa merupakan forensic image dari media penyimpanan.

Kita tidak seharusnya memperlakukan forensic image sebagai file biasa. Image tersebut merepresentasikan data dari media penyimpanan yang sedang kita investigasi. Nantinya kita akan belajar bagaimana memeriksa image tersebut tanpa mengubah evidence asli.

Misalnya: `evidence.E01`

berisi image dari sebuah Windows machine.

Dari sana kita mungkin menemukan: `C:\Users\Alice\Downloads\invoice.exe`

Kemudian kita menemukan Prefetch yang menunjukkan executable tersebut pernah dijalankan, Kemudian kita menemukan browser history yang menunjukkan user mengunduh file tersebut, Kemudian Event Logs menunjukkan aktivitas login pada waktu yang sama, Sekarang disk evidence telah menghasilkan beberapa artifact yang dapat dikorelasikan.

## Filesystem Evidence

Filesystem adalah struktur yang digunakan operating system untuk mengorganisasi data pada media penyimpanan. Contohnya NTFS pada Windows dan ext4 pada Linux.

Filesystem menyimpan lebih dari sekadar isi file. Ia juga dapat menyimpan informasi seperti nama file, lokasi file, ukuran, timestamps, permissions, dan struktur directory.

Ini sangat penting dalam forensic karena filesystem dapat memberikan informasi tentang bagaimana data berada pada disk.

Misalnya sebuah file: `C:\Users\Alice\Documents\secret.docx`

bisa memberi kita informasi mengenai nama file dan lokasinya. Kemudian metadata atau filesystem structures dapat memberikan timestamp dan informasi lainnya.

Nanti kita akan membahas **MFT pada NTFS**, inode pada filesystem Linux, filesystem timestamps, deleted file records, dan konsep file allocation secara lebih mendalam.

Untuk sekarang, tanamkan satu konsep:

**Filesystem bukan cuma tempat menyimpan file. Filesystem sendiri merupakan sumber evidence.**

## Application Evidence

Aplikasi juga meninggalkan banyak artefak.

Browser adalah salah satu contoh terbaik.

Ketika kamu menggunakan Chrome, Firefox, atau browser lainnya, aktivitasmu dapat meninggalkan berbagai data seperti history, cookies, cache, downloads, bookmarks, dan database aplikasi.

Misalnya investigator ingin mengetahui:
> “Apakah user pernah mengakses website tertentu?”

File dokumen mungkin tidak memberikan jawabannya.

Tetapi browser history mungkin memberikan evidence tersebut.

Kalau investigator ingin mengetahui:
> “Apakah user pernah mengunduh file tertentu?”

Browser download database dapat menjadi sumber evidence.

Kalau ingin mengetahui:
> “Apakah user pernah login ke website tertentu?”

Cookies atau session-related artifacts mungkin memberikan informasi tambahan.

Karena itu ketika kita nanti belajar Browser Forensics, kita akan membedah bagaimana aplikasi menyimpan informasi aktivitas user.

## Operating System Evidence

Operating system juga meninggalkan banyak jejak.

Pada Windows, misalnya, terdapat Windows Registry. Registry merupakan database konfigurasi yang digunakan Windows dan berbagai komponennya. Dari Registry, forensic analyst dapat memperoleh banyak informasi mengenai konfigurasi sistem, user, perangkat, software, dan aktivitas tertentu.

Windows juga memiliki Event Logs yang dapat mencatat berbagai event sistem.

Ada juga artefak seperti Prefetch, LNK files, Jump Lists, Recycle Bin artifacts, Windows Defender artifacts, dan lainnya.

Jangan khawatir kalau nama-nama tersebut sekarang terlihat seperti daftar mantra. Kita akan membahasnya satu per satu nanti. Yang penting kamu memahami bahwa **operating system sendiri terus meninggalkan jejak aktivitas**.

## Network Evidence

Evidence juga dapat berasal dari jaringan.

Misalnya kamu mendapatkan file: `traffic.pcap`

File tersebut bisa berisi packet capture yang merekam komunikasi jaringan.

Dengan Wireshark atau tools lainnya, kita bisa melakukan analysis terhadap traffic tersebut.

Misalnya kamu menemukan:
`DNS query → suspicious-domain.com`

Kemudian:
`TCP connection → 10.10.10.20:443`

Kemudian terlihat adanya HTTP request atau pola komunikasi lainnya.

Dari network evidence kita dapat mencoba mengetahui siapa berkomunikasi dengan siapa, kapan komunikasi terjadi, protocol apa yang digunakan, dan apakah terdapat aktivitas yang mencurigakan.

Network Forensics akan menjadi salah satu bagian penting dalam roadmap kita karena challenge CTF sering memberikan PCAP dan meminta kita menemukan informasi tertentu dari dalamnya.

## Memory Evidence

Memory atau RAM merupakan salah satu sumber evidence yang sangat menarik karena memberikan gambaran mengenai **state sistem pada saat memory tersebut diambil**.

Misalnya sebuah komputer sedang menjalankan malware. File malware mungkin sudah dihapus dari disk. Tetapi process atau informasi terkait malware masih berada di memory.

Dengan memory forensics, kita dapat mencari hal-hal seperti process, command line, network connection, loaded modules, memory regions, dan artefak lainnya.

Tool yang nantinya akan kita gunakan antara lain **Volatility**.

Misalnya kita mempunyai: `memory.raw`

Kita dapat melakukan analisis untuk menemukan process yang berjalan.

Kemudian menemukan: `powershell.exe`

yang memiliki command line mencurigakan.

Kemudian menemukan koneksi: `192.168.1.10 → 203.x.x.x:443`

Sekarang kita mempunyai evidence yang tidak harus terlihat jelas dari filesystem.

Ini salah satu alasan kenapa memory forensics cukup sering muncul dalam kompetisi.

## Metadata sebagai Evidence

Metadata adalah informasi mengenai suatu data.

Contohnya sebuah foto dapat memiliki metadata seperti waktu pengambilan, kamera yang digunakan, resolusi, dan informasi lain tergantung format dan sumber file.

Sebuah dokumen juga dapat mempunyai metadata seperti author, creation time, modification time, application yang digunakan, dan sebagainya.

Misalnya kamu menemukan: `confidential.pdf`

Kemudian metadata menunjukkan bahwa dokumen tersebut dibuat menggunakan aplikasi tertentu dan memiliki author tertentu.

Metadata tersebut belum tentu membuktikan siapa yang melakukan sesuatu. Tetapi metadata dapat menjadi **clue** yang kemudian dikorelasikan dengan evidence lainnya.

Karena itu nanti kita akan belajar menggunakan tools seperti `exiftool` untuk melakukan metadata analysis.

## Evidence yang sudah dihapus

Salah satu hal yang membuat Digital Forensics menarik adalah **deleted data**.

Ketika user menghapus file, operating system biasanya tidak langsung menghancurkan setiap byte file tersebut. Pada banyak kondisi, filesystem hanya menandai ruang tersebut sebagai available untuk digunakan kembali.

Artinya sebagian informasi mungkin masih dapat dipulihkan.

Namun recovery tidak selalu berhasil. Jika data sudah tertimpa oleh data baru, kemungkinan recovery dapat menurun. SSD juga memiliki mekanisme seperti TRIM yang membuat kondisi recovery berbeda dari HDD.

Nanti kita akan melakukan praktik deleted file recovery dan file carving. Di sana kamu akan mulai melihat bagaimana file yang secara normal sudah tidak terlihat dapat ditemukan kembali.

## Chain of Custody

Sekarang kita masuk ke konsep yang sangat penting dalam forensic, yaitu **Chain of Custody**.

Chain of custody adalah dokumentasi mengenai bagaimana evidence diperoleh, siapa yang menangani, kapan ditangani, bagaimana disimpan, dan bagaimana evidence tersebut diproses.

Bayangkan ada sebuah USB drive yang menjadi evidence.

Investigator A mengambil USB tersebut.

Kemudian diberikan kepada Investigator B.

Kemudian B melakukan imaging.

Kemudian image diberikan kepada Analyst C.

Semua perpindahan dan aktivitas tersebut harus dapat dicatat.

Tujuannya adalah menjaga **accountability dan integrity** evidence.

Dalam konteks lomba CTF, chain of custody mungkin tidak menjadi bagian yang harus kamu tulis secara formal. Tetapi konsepnya tetap penting karena membentuk kebiasaan bahwa evidence harus diperlakukan secara hati-hati.

## Evidence → Artifact → Finding

Sekarang kita satukan semua konsep tadi.

Misalkan kita mempunyai: `evidence.E01`
Itu adalah **evidence**.

Di dalamnya kita menemukan Windows Prefetch yang menunjukkan `malware.exe` pernah dijalankan.
Itu adalah **artifact**.

Kemudian kita menemukan bahwa timestamp eksekusinya sesuai dengan aktivitas network yang mencurigakan dan file tersebut berada di lokasi yang tidak biasa.
Gabungan informasi tersebut menghasilkan sebuah **finding**.

Dengan demikian pola berpikir kita adalah:
**Evidence → Artifact → Correlation → Finding → Conclusion**

Ini adalah pola yang akan terus kita gunakan sampai level Advanced.


Untuk mendalami lebih dalam kita akan melakukan latihan di sini : [Praktek 1](Praktek%201.md)

## Kesimpulan Materi 2

Digital Evidence adalah dasar dari seluruh investigasi forensic. Evidence dapat berasal dari berbagai sumber seperti storage, filesystem, operating system, application, network, memory, dan metadata. Setiap jenis evidence memiliki karakteristik dan nilai investigasi yang berbeda.

Hal yang paling penting untuk kamu bawa dari materi ini adalah bahwa **evidence tidak selalu berupa file**. Sebuah timestamp, registry entry, browser history, process, network connection, deleted file record, bahkan informasi yang ditemukan di memory dapat menjadi bagian dari evidence.

Kemudian biasakan membedakan:
- **Evidence** adalah sumber data yang kita periksa.
- **Artifact** adalah jejak atau informasi yang ditemukan dari evidence.
- **Finding** adalah hasil analisis yang relevan terhadap kasus.

Dan akhirnya:
**Finding + Correlation → Conclusion**

Kalau pola ini sudah mulai terasa natural, kamu sudah berada di jalur yang benar.