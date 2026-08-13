#cybersecurity 

Digital Forensics atau forensik digital adalah proses untuk **menemukan, mengamankan, memeriksa, menganalisis, dan menjelaskan bukti yang berasal dari perangkat atau sistem digital.** Sederhananya, kalau sebuah komputer diduga digunakan untuk melakukan sesuatu yang mencurigakan, forensic analyst bertugas menjawab pertanyaan seperti **apa yang terjadi, kapan terjadi, bagaimana terjadinya, siapa atau akun apa yang terlibat, file apa yang digunakan, dan bukti apa yang mendukung kesimpulan tersebut**.

Yang perlu kamu pahami sejak awal adalah bahwa Digital Forensics bukan sekadar kegiatan “mencari file mencurigakan”. Ini merupakan proses investigasi. Misalnya ada sebuah komputer yang diduga terkena malware. Orang yang baru mengenal forensic mungkin langsung membuka folder dan mencari file bernama `malware.exe`. Masalahnya, malware modern tidak terlalu peduli dengan kenyamanan hidup manusia. Namanya bisa dibuat seperti file biasa, disembunyikan, dihapus setelah digunakan, dijalankan dari temporary directory, atau bahkan hanya terlihat jelas ketika kita memeriksa memory. Karena itu forensic analyst harus membangun **cerita berdasarkan evidence**, bukan berdasarkan tebakan.

Bayangkan kamu mendapatkan sebuah laptop yang diduga digunakan seseorang untuk mencuri data perusahaan. Kamu tidak tahu apa yang dilakukan pengguna tersebut. Kamu hanya mendapatkan laptop atau forensic image-nya. Di dalamnya mungkin terdapat ribuan bahkan jutaan file. Ada browser history, dokumen, gambar, log sistem, registry, cache, temporary files, deleted files, USB history, dan berbagai artefak lainnya. Tugasmu bukan membaca semuanya satu per satu seperti manusia yang sedang mencari makna hidup di dalam folder Downloads. Tugasmu adalah menentukan **evidence mana yang relevan terhadap kasus**, kemudian menghubungkan evidence tersebut.

Misalnya kamu menemukan sebuah file `invoice.pdf`. Sendirian, file tersebut tidak terlalu berarti. Tetapi kemudian kamu menemukan metadata yang menunjukkan file itu dibuat pada pukul 02:14. Kemudian Windows Prefetch menunjukkan sebuah aplikasi tertentu dijalankan pada waktu yang berdekatan. Browser history menunjukkan pengguna mengunjungi website tertentu. Event Log menunjukkan adanya aktivitas login. Kemudian dari filesystem kamu menemukan bahwa sebuah USB device terhubung beberapa menit setelah dokumen tersebut dibuka. Sekarang masing-masing evidence mulai membentuk hubungan. Inilah inti dari forensic investigation: **satu artefak mungkin tidak berarti banyak, tetapi beberapa artefak yang saling berkorelasi dapat membentuk sebuah timeline kejadian.**

## Digital Forensics bukan hacking

Ini bagian yang penting karena kamu belajar Cyber Security dan kemungkinan besar otakmu akan otomatis menganggap semua aktivitas cyber sebagai “serang sistem”. Digital Forensics mempunyai tujuan yang berbeda.

Dalam penetration testing, misalnya, kamu mencoba menemukan vulnerability dan membuktikan bahwa vulnerability tersebut dapat dieksploitasi. Dalam incident response, kamu berusaha memahami dan menangani insiden yang sedang atau baru saja terjadi. Sedangkan dalam Digital Forensics, fokusnya adalah **mengumpulkan dan menganalisis evidence untuk merekonstruksi kejadian digital**.

Ketiganya memang saling berhubungan. Bahkan dalam dunia nyata, seorang security analyst bisa saja menemukan indikasi serangan, incident responder menangani insiden tersebut, lalu forensic analyst melakukan pemeriksaan evidence untuk mengetahui bagaimana serangan terjadi dan apa saja yang dilakukan attacker.

Untuk lomba, batasnya kadang lebih kabur. Challenge bisa memberikan disk image, memory dump, PCAP, atau file hasil kompromi lalu meminta kamu menemukan flag atau menjawab pertanyaan tertentu. Karena itu kamu perlu mempunyai pola pikir investigatif, bukan sekadar hafalan tools.
	
## Apa yang dimaksud Digital Evidence?

Sebelum membahas forensic tools, kamu harus memahami benda yang sebenarnya sedang kita periksa, yaitu **digital evidence**.

Digital evidence adalah informasi digital yang dapat digunakan untuk membantu membuktikan atau menjelaskan suatu kejadian. Evidence dapat berasal dari berbagai sumber. Sebuah komputer dapat memberikan file, metadata, registry, event log, browser history, process information, dan banyak artefak lainnya. Smartphone dapat memberikan informasi aplikasi, pesan, foto, lokasi, database, dan metadata. Network capture dapat memberikan traffic jaringan. Memory dump dapat memberikan informasi mengenai proses, koneksi jaringan, command, dan data yang sedang berada di RAM.

Jadi ketika nanti kita membuka Autopsy, FTK Imager, Volatility, Wireshark, atau tools lainnya, jangan berpikir bahwa tools tersebut adalah inti forensic. **Tools hanyalah alat untuk membaca evidence.**

Misalnya kamu diberikan file `memory.raw`. File tersebut bukan “hasil forensic”. Itu adalah **evidence**. Volatility kemudian digunakan untuk melakukan examination terhadap evidence tersebut. Dari sana kamu mungkin menemukan proses mencurigakan, koneksi jaringan, command line, atau artefak lain. Hasil analisis itulah yang kemudian digunakan untuk menjawab pertanyaan investigasi.

Pemisahan antara **evidence**, **artifact**, dan **finding** akan sangat berguna.

Evidence adalah sumber data yang kamu miliki. Artifact adalah informasi atau struktur tertentu yang ditemukan di dalam evidence. Finding adalah hasil interpretasi yang relevan terhadap kasus.

Contohnya begini. Kamu mendapatkan `disk.img`. Itu adalah evidence. Di dalamnya terdapat Windows Prefetch dengan record untuk `powershell.exe`. Itu adalah artifact. Setelah dianalisis bersama timestamp dan evidence lain, kamu menyimpulkan bahwa PowerShell kemungkinan digunakan pada waktu tertentu untuk menjalankan aktivitas tertentu. Itu menjadi finding.

Memahami perbedaan ini akan membuat laporan forensic kamu jauh lebih rapi.

## Cara berpikir seorang forensic analyst

Forensic analyst harus selalu mempunyai sikap **skeptis terhadap evidence**. Bukan berarti semua bukti dianggap palsu, tetapi setiap kesimpulan harus memiliki dasar.

Misalnya kamu menemukan file `passwords.txt`. Kamu tidak boleh langsung berkata:
> “Attacker mencuri password.”

Itu adalah kesimpulan yang terlalu jauh.

Pertanyaan yang lebih tepat adalah: kapan file tersebut dibuat? Siapa owner-nya? Apakah file pernah dibuka? Apakah ada aplikasi yang mengaksesnya? Apakah terdapat aktivitas network yang berhubungan dengannya? Apakah file tersebut berada di lokasi normal atau mencurigakan? Apakah file tersebut masih ada atau sudah dihapus? Apakah timestamp-nya konsisten dengan evidence lain?

Kemudian kamu mencari evidence tambahan.

Misalnya kamu menemukan bahwa `passwords.txt` dibuat pukul 01:15. Pada pukul 01:16 terdapat aktivitas PowerShell. Pada pukul 01:17 terdapat koneksi network menuju IP tertentu. Pada pukul 01:18 sebuah archive `.zip` dibuat. Pada pukul 01:20 USB device terhubung.

Sekarang kamu memiliki rangkaian peristiwa yang jauh lebih menarik.

Tetapi bahkan di sini kamu tetap harus berhati-hati. **Korelasi bukan otomatis berarti kausalitas.** Hanya karena dua aktivitas terjadi berdekatan waktunya bukan berarti aktivitas pertama pasti menyebabkan aktivitas kedua. Ini salah satu kebiasaan berpikir yang harus kita bangun selama belajar.

## Empat tahap utama Digital Forensics

Dalam praktik forensic, proses investigasi biasanya dapat dipahami sebagai beberapa tahap besar: **collection, examination, analysis, dan reporting**. NIST SP 800-86 menggunakan kerangka ini sebagai panduan untuk mengintegrasikan teknik forensic ke dalam incident response.

Tahap pertama adalah **collection**. Pada tahap ini kita mengidentifikasi dan mengumpulkan evidence yang relevan sambil menjaga agar evidence tersebut tidak berubah. Misalnya kita memiliki sebuah hard disk yang diduga berisi bukti. Kita tidak ingin sembarangan membuka dan mengubah file di dalam hard disk asli. Biasanya dibuat forensic image sehingga analisis dilakukan terhadap salinan yang dapat diverifikasi.

Kemudian terdapat **examination**. Di sini evidence diproses agar informasi yang relevan dapat ditemukan. Kita mungkin melakukan filesystem analysis, parsing registry, ekstraksi metadata, recovery deleted files, parsing browser artifacts, atau teknik lainnya.

Setelah itu masuk ke **analysis**. Ini bagian ketika evidence mulai diberi konteks. Kita mencari hubungan antar-artifact, membuat timeline, mengidentifikasi aktivitas mencurigakan, melakukan correlation, dan menyusun hipotesis tentang apa yang sebenarnya terjadi.

Tahap terakhir adalah **reporting**. Hasil investigasi harus dapat dijelaskan. Kamu harus mampu mengatakan evidence apa yang ditemukan, bagaimana evidence tersebut dianalisis, apa yang dapat disimpulkan, dan apa batasan dari kesimpulan tersebut.

Dalam lomba, bagian reporting mungkin tidak selalu terlihat seperti laporan formal. Bisa saja soal hanya bertanya:
> “What was the attacker’s IP?”

atau:
> “When was the malicious executable first executed?”

Tetapi proses berpikirmu tetap harus mengikuti workflow tersebut.

## Mengapa integrity sangat penting?

Sekarang kita masuk ke konsep yang akan terus muncul sepanjang belajar forensic, yaitu **integrity**.

Bayangkan kamu memiliki sebuah file evidence bernama `disk.img`. Kemudian kamu melakukan analisis selama beberapa jam. Setelah itu ukuran file berubah. Atau isi file berubah. Bagaimana kamu tahu bahwa evidence yang kamu analisis masih sama dengan evidence awal?

Di sinilah hashing digunakan.

Hash adalah nilai yang dihasilkan oleh fungsi hash berdasarkan isi data. Algoritma seperti SHA-256 dapat menghasilkan representasi berupa nilai hexadecimal. Jika isi file berubah, nilai hash hampir pasti berubah juga.

Misalnya secara sederhana:

`disk.img` → SHA-256 → `abc123...`

Setelah kamu membuat salinan:

`disk_copy.img` → SHA-256 → `abc123...`

Jika kedua hash sama, itu memberikan verifikasi bahwa kedua file memiliki isi yang sama berdasarkan algoritma hash tersebut.

Nanti kita akan mempraktikkan hashing secara langsung menggunakan Linux command line dan tools forensic. Untuk sekarang cukup pahami konsepnya: **hash membantu kita memverifikasi integrity evidence.**

Jangan sampai nanti kamu menjadi orang yang menemukan evidence penting lalu mengeditnya sebelum melakukan hashing. Itu cara tercepat untuk membuat investigator lain memandangmu seperti melihat orang membawa bensin ke ruang server.

## Mengapa timestamp sangat penting?

Salah satu kemampuan paling penting dalam forensic adalah memahami waktu.

Sebuah filesystem biasanya menyimpan berbagai timestamp. File dapat memiliki informasi seperti waktu dibuat, dimodifikasi, atau diakses, tergantung filesystem dan platform. Windows juga memiliki berbagai artefak yang menyimpan timestamp aktivitas.

Namun timestamp bukan kebenaran absolut.

Misalnya sebuah file memiliki timestamp:

`2026-08-12 01:30:00`

Jangan langsung menganggap:

> “Berarti attacker membuat file jam 01:30.”

Timestamp dapat dimanipulasi. Timezone dapat menyebabkan interpretasi berbeda. Clock system bisa salah. Beberapa aplikasi juga memiliki cara sendiri dalam mencatat waktu.

Karena itu timestamp harus dikorelasikan dengan evidence lain.

Misalnya:

`01:30` → file dibuat  
`01:31` → PowerShell dijalankan  
`01:32` → network connection muncul  
`01:34` → archive dibuat

Ketika beberapa sumber evidence menunjukkan pola yang konsisten, confidence terhadap timeline menjadi lebih kuat.

Konsep inilah yang nantinya akan membawa kita ke **timeline analysis**, salah satu skill penting dalam Digital Forensics.

## Artifact adalah harta karun forensic

Ketika melakukan forensic, kamu akan sering mendengar istilah **artifact**.

Artifact adalah data atau jejak yang ditinggalkan oleh aktivitas pengguna, sistem operasi, aplikasi, atau proses tertentu. Aktivitas digital hampir selalu meninggalkan jejak di suatu tempat.

Ketika seseorang membuka browser, browser dapat menyimpan history, cache, cookies, downloads, dan database lainnya.

Ketika seseorang menjalankan program di Windows, sistem dapat meninggalkan berbagai artefak seperti Prefetch atau informasi lainnya.

Ketika seseorang menggunakan USB, sistem dapat meninggalkan informasi mengenai perangkat yang pernah terhubung.

Ketika seseorang menghapus file, file tersebut mungkin hilang dari directory listing tetapi sebagian data atau metadata-nya masih dapat ditemukan.

Ketika sebuah proses melakukan koneksi network, informasi tersebut dapat muncul di memory atau network capture.

Jadi prinsip yang harus kamu tanamkan adalah:

**User activity → system/application behavior → artifacts**

Aktivitas pengguna menghasilkan perubahan atau jejak pada sistem. Jejak tersebut kemudian dapat kita gunakan untuk merekonstruksi aktivitas.

Ini juga alasan mengapa Digital Forensics sangat menarik. Kamu sebenarnya sedang membaca **jejak sejarah yang ditinggalkan komputer**.

## Contoh kasus sederhana

Bayangkan dalam sebuah lomba kamu mendapatkan sebuah Windows disk image. Pertanyaannya:
> “Determine whether the user executed the suspicious program `update.exe`.”

Kamu menemukan `update.exe` di dalam filesystem.

Apakah itu cukup? Belum.

Kamu kemudian menemukan artifact yang menunjukkan `update.exe` pernah dieksekusi. Lalu kamu menemukan timestamp yang menunjukkan waktu eksekusi. Kemudian kamu menemukan evidence tambahan dari Windows Event Logs atau artefak lain yang konsisten dengan aktivitas tersebut.

Sekarang kamu memiliki beberapa evidence yang mendukung hipotesis bahwa program tersebut memang dieksekusi.

Perhatikan perubahan cara berpikirnya.

Awalnya: **“File ada.”**

Kemudian: **“File ada dan terdapat evidence bahwa file dieksekusi.”**

Lalu: **“File dieksekusi pada waktu tertentu dan aktivitas tersebut berkorelasi dengan evidence lainnya.”**

Inilah perkembangan dari sekadar **file hunting** menjadi **forensic analysis**.

## Prinsip paling penting untuk lomba

Mulai sekarang, setiap kali kamu melihat sebuah artifact, biasakan bertanya menggunakan pola:

**What?** Apa yang ditemukan?

**Where?** Di mana ditemukan?

**When?** Kapan aktivitas terjadi?

**Who?** User atau proses apa yang terkait?

**How?** Bagaimana aktivitas tersebut terjadi?

**Why?** Apa kemungkinan tujuan aktivitas tersebut?

Pertanyaan “why” harus paling hati-hati. Evidence biasanya lebih mudah membuktikan **apa, kapan, dan bagaimana** daripada niat seseorang. Jangan mengarang motivasi attacker hanya karena sebuah file terlihat menyeramkan.

Kemudian tambahkan satu pertanyaan lagi:

**What evidence supports this conclusion?**

Pertanyaan terakhir ini yang akan menjaga kamu dari membuat kesimpulan berdasarkan feeling.

## Hubungannya dengan lomba Cyber Security

Dalam kompetisi Digital Forensics, challenge biasanya memberikan suatu sumber evidence seperti **disk image, memory dump, PCAP, file system, log, archive, atau kumpulan file**. Kamu kemudian diberikan pertanyaan yang harus dijawab berdasarkan evidence tersebut.

Misalnya challenge memberikan `image.E01`. Kamu mungkin perlu menentukan filesystem, mencari user, menganalisis browser, menemukan file yang dihapus, melihat metadata, mencari suspicious executable, membuat timeline, kemudian menemukan flag.

Challenge lain mungkin memberikan `memory.raw`. Kamu harus mencari proses mencurigakan, command line, network connection, DLL, credential artifact, atau informasi lain dari memory.

Challenge network dapat memberikan `.pcap`. Di sana kamu mungkin perlu mencari DNS query, HTTP request, suspicious TCP connection, file transfer, credential leakage, atau komunikasi command-and-control.

Jadi walaupun semuanya disebut Digital Forensics, sumber evidence-nya bisa sangat berbeda. Karena itulah roadmap kita nanti akan bercabang ke **Disk Forensics, Windows Forensics, Memory Forensics, Network Forensics, Browser Forensics, dan akhirnya Advanced Forensics**.