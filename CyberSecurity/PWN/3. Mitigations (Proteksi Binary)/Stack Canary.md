#cybersecurity

Stack Canary adalah nilai acak yang ditaruh **di antara buffer dan return address**. Sebelum fungsi kembali, program memeriksa apakah canary masih utuh - kalau berubah (karena overflow menimpanya), program langsung exit dengan pesan "stack smashing detected".

## Cara kerja

```
+-------------------------+
| return address          |
+-------------------------+
| canary  (acak, 8 byte)  |  <-- kalau tertimpa -> program berhenti
+-------------------------+
| saved RBP               |
+-------------------------+
| buffer                  |  <-- overflow dari sini
+-------------------------+
```

```c
void vuln() {
    char buf[64];
    gets(buf);   // overflow -> menimpa canary
}                // cek canary dulu sebelum ret -> crash
```

Ciri khas:

```
*** stack smashing detected ***: terminated
```

## Cek

```bash
checksec --file=chall
# Stack: Canary found
```

## Bypass

### 1. Leak canary

Canary 64-bit berakhir dengan null byte (`\x00`) di byte paling signifikan - jadi isinya hanya 7 byte acak. Kalau bisa di-leak (format string, read overflow 1 byte), kirim balik:

```python
from pwn import *

# asumsi: leak canary lewat format string di posisi 6
io.sendline(b"%6$p")
canary = int(io.recvline(), 16)

payload = b"A"*offset + p64(canary) + b"B"*8 + p64(win)
io.sendline(payload)
```

Urutan payload dengan canary:

```
[buffer] [canary] [saved rbp (8 byte dummy)] [return address]
```

### 2. Brute force (byte by byte)

Kalau program fork (misal server yang menerima banyak koneksi), canary tidak berubah antar fork - bisa brute force per byte. Tools: `canary` dari pwntools, atau script manual.

### 3. Hindari menimpa canary

- Kalau overflow terjadi **sebelum** canary dan fungsi tidak punya path return yang kita kontrol... (jarang)
- **Partial overwrite** - timpa return address sebagian tanpa menyentuh canary (kasus spesifik)

### 4. Exploit tanpa return address

Beberapa teknik (format string, GOT overwrite, __stack_chk_fail overwrite) tidak menyentuh return address - canary tidak relevan.

- GOT overwrite: [[8. GOT dan PLT]]
- Format string: [[6. Format String]]

## Catatan penting

1. Canary 32-bit = 4 byte, 64-bit = 8 byte. Byte pertama (LSB di little endian) = `\x00` - itu yang mencegah leak via string.
2. Kalau program **fork setiap koneksi** (server), canary sama di semua child - brute force per byte feasible (256 percobaan per byte, 7 byte = 256^7... tapi dengan fork bisa 256 percobaan per posisi karena byte-by-byte).
3. `__stack_chk_fail` adalah fungsi yang dipanggil saat canary gagal. Di beberapa challenge, GOT-nya bisa di-overwrite dengan `win` → canary "gagal" malah memanggil win!
4. Canary biasanya **dimulai dengan 0x00** - kalau leak lewat `printf("%s")`, null byte memotong leak. Pakai `%p`/read byte mental untuk leak.

## Check apakah canary ada di fungsi tertentu

```bash
objdump -d chall | grep -A5 "fs:0x28"
# mov rax, qword ptr fs:[0x28]  -> canary dibaca
```
