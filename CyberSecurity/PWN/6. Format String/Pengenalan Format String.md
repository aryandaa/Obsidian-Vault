#cybersecurity

Format string vulnerability muncul saat input user dimasukkan langsung ke fungsi format seperti `printf`, `sprintf`, `fprintf` sebagai **format string**.

## Kode aman vs rentan

```c
// AMAN - input sebagai data
printf("%s", user_input);

// RENTAN - input sebagai format string!
printf(user_input);
```

Saat user mengirim `%p`, program menampilkan nilai dari stack - bukan karakter `%p`. Semua specifier `%` dieksekusi.

## Specifier format yang penting

| Specifier | Output | Kegunaan |
|---|---|---|
| `%d` / `%i` | Integer | Probing |
| `%x` | Hex | Leak stack (4 byte) |
| `%p` | Pointer | Leak stack (8 byte di 64-bit) |
| `%s` | String | Baca memory di alamat argumen |
| `%n` | Tulis jumlah char | **Write** ke alamat argumen |
| `%hhn` | Tulis 1 byte | Write presisi |
| `%hn` | Tulis 2 byte | Write presisi |
| `%N$p` | Argumen ke-N | Positional parameter |
| `%N$s` | String dari argumen ke-N | Read arbitrary |
| `%N$n` | Write ke argumen ke-N | Write arbitrary |

## Contoh: leak stack

```python
# Kirim banyak %p, lihat isi stack
payload = b"%p.%p.%p.%p.%p.%p.%p.%p"
io.sendline(payload)
print(io.recvline())
# 0x7ffc... .0x7f... .0x... .0x... ...
```

Setiap `%p` mengambil 8 byte (64-bit) dari stack (atau register, sesuai posisi).

## Positional parameter

Daripada menebak, tunjuk langsung posisi:

```python
# %6$p = ambil argumen ke-6 (yang pertama biasanya isi buffer di posisi 6-8)
payload = b"%6$p"
```

Untuk mencari posisi buffer kita di stack, kirim penanda:

```python
payload = b"AAAA.%p.%p.%p.%p.%p.%p.%p.%p"
# cari posisi yang menampilkan 0x41414141 ("AAAA")
```

## Kenapa berbahaya?

1. **Read** - `%p`/`%x`/`%s` membocorkan alamat (libc, stack, canary) → bypass ASLR & canary ([[3. Mitigations (Proteksi Binary)]])
2. **Write** - `%n` menulis ke alamat yang kita tunjuk → GOT overwrite → RCE ([[Format String Write (GOT Overwrite)]])

## Deteksi

```bash
$ ./chall
Masukkan nama: %p%p%p%p
0x7fff123456780x7f1234567890...
```

Kalau muncul hex acak → format string vulnerability.

Atau:

```python
io.sendline(b"%p.%p.%p.%p")
if "0x" in io.recvline().decode():
    print("[+] Format string!")
```

## Catatan

- Fungsi lain yang rentan: `sprintf(buf, user)`, `snprintf`, `fprintf(stderr, user)`, `syslog(user)`.
- Di 64-bit, argumen pertama `printf` diambil dari register (RSI, RDX, ...), sisanya dari stack - jadi posisi payload di stack biasanya mulai di `%6$` sampai `%9$` tergantung konteks.
- `%s` pada alamat yang tidak valid → crash. Gunakan `%p` dulu untuk menemukan alamat yang aman.
- Format string + Partial RELRO = kombinasi GOT overwrite klasik.
