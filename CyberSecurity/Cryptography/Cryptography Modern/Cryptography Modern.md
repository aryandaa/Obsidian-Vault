#roadmap 

Kriptografi modern lahir setelah komputer ada. Bedanya dengan kriptografi klasik: cipher klasik bisa dipecahkan dengan pena dan kertas, sedangkan cipher modern dirancang untuk aman meskipun diserang dengan komputer yang sangat kuat. Rahasianya ada di matematika, dan kamu sudah mempelajari matematika yang dibutuhkan di sesi Modular Arithmetic.

Kriptografi modern terbagi menjadi dua keluarga besar:

1. [4. Symmetric key](Symmetric%20key/4.%20Symmetric%20key.md): satu kunci untuk mengunci dan membuka. Seperti gembok yang satu anak kuncinya untuk semua.
2. [5. Asymmetric key](Asymmetric%20key/5.%20Asymmetric%20key.md): dua kunci berbeda, satu untuk mengunci dan satu untuk membuka. Seperti kotak surat: siapa pun bisa memasukkan surat, tapi hanya pemilik kunci yang bisa membukanya.

Kebanyakan sistem di dunia nyata memakai keduanya sekaligus (disebut hybrid). Misalnya HTTPS: asymmetric dipakai untuk bertukar kunci rahasia, lalu symmetric dipakai untuk mengenkripsi data sebenarnya karena lebih cepat.

Urutan belajar:

1. Symmetric key: DES (sejarah), AES (standar sekarang), mode operasi, stream cipher.
2. Asymmetric key: RSA (paling sering muncul di CTF), Diffie-Hellman dan ElGamal, ECC.

Mulai dari sini: [4. Symmetric key](Symmetric%20key/4.%20Symmetric%20key.md)
