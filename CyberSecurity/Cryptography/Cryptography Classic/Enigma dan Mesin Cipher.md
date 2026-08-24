#cybersecurity 

Sebelum komputer ada, cipher paling canggih di dunia bukan berupa rumus matematika, melainkan **mesin**. Yang paling terkenal adalah Enigma, dipakai militer Jerman pada Perang Dunia II. Materi ini menceritakan bagaimana mesin itu bekerja dan mengapa pemecahannya mengubah sejarah.

Di CTF, Enigma jarang muncul, tetapi kalau muncul biasanya sebagai soal sejarah atau simulasi kecil. Yang lebih penting: cerita Enigma mengajarkan pola pikir yang dipakai terus dalam kriptografi sampai sekarang.

## Mesin Enigma itu seperti apa

Bayangkan sebuah mesin tik kecil dalam kotak kayu. Setiap kali kamu menekan sebuah huruf, sebuah lampu menyala menampilkan huruf hasil enkripsi. Ada tiga komponen utama:

1. **Keyboard dan lampu**: tempat menekan huruf dan membaca hasilnya.
2. **Rotor**: tiga roda bergigi yang memetakan huruf secara acak, dan berputar setiap kali tombol ditekan.
3. **Plugboard (papan colokan)**: di bagian depan, bisa menghubungkan pasangan huruf dengan kabel, mirip papan operator telepon jaman dulu.

## Cara kerja sederhana

Setiap kali tombol ditekan, sinyal listrik melewati:

```text
Keyboard → Plugboard → Rotor 1 → Rotor 2 → Rotor 3 → reflektor
         → Rotor 3 → Rotor 2 → Rotor 1 → Plugboard → Lampu
```

Sinyal itu dipetakan berkali-kali, lalu dikembalikan lagi, lalu dipetakan sekali lagi sebelum menyalakan lampu.

Yang membuat Enigma kuat: **rotor berputar setiap kali tombol ditekan**. Jadi huruf A yang ditekan pertama kali menghasilkan huruf tertentu, tetapi A yang ditekan kedua kali menghasilkan huruf yang berbeda. Ini adalah cipher polialfabetik versi mesin, jauh lebih rumit daripada Vigenere manual.

## Kenapa sulit dipecahkan

- Ada 3 rotor yang bisa ditukar urutannya.
- Setiap rotor bisa dipasang di 26 posisi awal.
- Plugboard bisa menghubungkan sampai 10 pasang huruf.
- Total kombinasi kunci sekitar 150 triliun lebih.

Pada zamannya, angka itu terasa mustahil untuk dipecahkan secara manual.

## Kelemahan Enigma

Sehebat apa pun, Enigma punya kelemahan yang akhirnya dieksploitasi:

1. **Sebuah huruf tidak akan pernah menjadi dirinya sendiri.** Huruf A tidak akan pernah terenkripsi menjadi A. Ini aturan yang dipakai pemecah kode untuk menyaring kemungkinan.
2. **Kata-kata yang bisa ditebak.** Pesan Jerman selalu dimulai dengan pola cuaca atau frasa standar seperti "Heil Hitler" dan "Keine besonderen Ereignisse" (tidak ada kejadian khusus). Pemecah kode menyebutnya **crib**, potongan plaintext yang sudah diketahui.
3. **Kesalahan operator.** Operator yang malas memakai pengaturan yang sama, atau mengirim pesan dengan pola yang berulang, memberi banyak petunjuk.

## Peran Alan Turing dan Bombe

Alan Turing bersama tim di Bletchley Park (Inggris) membangun mesin bernama **Bombe** untuk mencari pengaturan rotor yang mungkin, berdasarkan crib dan aturan "huruf tidak akan pernah menjadi dirinya sendiri". Bombe menyaring miliaran kemungkinan sampai tinggal sedikit yang masuk akal, lalu diuji manual.

Pemecahan Enigma diperkirakan memperpendek Perang Dunia II beberapa tahun. Setelah perang, pemerintah Inggris merahasiakan seluruh pekerjaan ini sampai tahun 1970-an.

## Pelajaran untuk kriptografi modern

Cerita Enigma mengajarkan tiga hal yang masih berlaku sampai sekarang:

1. **Kriptografi tidak bergantung pada kerahasiaan algoritma, tapi pada kerahasiaan kunci.** Mesin Enigma sudah diketahui cara kerjanya, tetapi selama kunci tidak ketahuan, pesan tetap aman. Prinsip ini disebut Kerckhoffs's principle.
2. **Kelemahan selalu ada di manusia dan implementasi**, bukan hanya di matematika. Operator yang malas, protokol yang bisa ditebak, dan kesalahan kecil semuanya bisa menghancurkan keamanan.
3. **Jangan pernah meremehkan crib dan pola.** Sedikit plaintext yang diketahui bisa menjadi awal dari pemecahan total.

## Enigma di CTF

Kalau soal Enigma muncul, biasanya seperti ini:

- Diberikan ciphertext, pengaturan rotor, dan posisi awal. Tinggal enkripsi/dekripsi pakai simulator.
- Python: `pip install pyenigma`

```python
from enigma.machine import EnigmaMachine

machine = EnigmaMachine.from_key_sheet(
    rotors='I II III',
    reflector='B',
    ring_settings='1 1 1',
    plugboard_settings='AV BS CG DL FU HZ JK NM QW RX'
)

machine.set_display('QEO')
plain = machine.process_text('CIPHERTEXT')
print(plain)
```

- Ada juga simulator online seperti [Enigma Museum](https://www.101computing.net/enigma-machine-emulator/) untuk mencoba-coba.

## Ringkasan

- Enigma adalah mesin cipher polialfabetik dengan rotor dan plugboard.
- Total kombinasi kunci sangat besar, tetapi kelemahan desain dan kebiasaan operator membuatnya bisa dipecahkan.
- Turing dan Bombe memecahkannya dengan crib dan penyaringan otomatis.
- Pelajaran utamanya: algoritma boleh diketahui publik, kunci yang harus rahasia. Prinsip ini dipakai semua cipher modern.
