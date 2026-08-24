#cybersecurity

Endianness adalah urutan penyimpanan byte dalam memory. x86/x64 memakai **little endian** - byte paling kecil (least significant) disimpan di alamat paling rendah. Semua payload pwn harus dalam little endian.

## Contoh

Nilai `0x401236` dalam little endian (8 byte):

```
Alamat rendah  ->  tinggi
36 12 40 00 00 00 00 00
```

Yang tertulis di file/memory: `\x36\x12\x40\x00\x00\x00\x00\x00`

## p32 vs p64

pwntools mengurus ini otomatis:

```python
from pwn import *

p32(0x401236)  # b'\x36\x12\x40\x00'   (32-bit)
p64(0x401236)  # b'\x36\x12\x40\x00\x00\x00\x00\x00'  (64-bit)

u64(b'\x36\x12\x40\x00\x00\x00\x00\x00')  # 0x401236 (unpack)
u32(b'\x36\x12\x40\x00')                  # 0x401236
```

## Null byte - masalah besar

Alamat 64-bit biasanya mengandung null byte:

```
0x0000000000401236 -> \x36\x12\x40\x00\x00\x00\x00\x00
```

Null byte mematikan fungsi yang berhenti di `\x00`:

- `strcpy`, `strcat` → berhenti di null byte
- `gets` → aman (tidak berhenti di null, tapi tidak bisa baca newline)
- `read` → aman (baca byte mentah)

Kalau input lewat `strcpy`, payload dengan null byte terpotong. Solusinya: **kurangi null byte** atau pakai fungsi yang aman (`read`, `fgets`).

## Mengurangi null byte

```bash
# Contoh: butuh alamat 0x0000000000401236
# Cari alamat alternatif yang tidak mengandung null:
#   0x0000000000401236  -> banyak null
#   lebih baik cari gadget/fungsi di alamat tanpa null byte
```

Atau urutkan operasi supaya null byte ada di akhir payload (masih terpotong di `strcpy`, tapi kadang cukup).

## Membaca nilai dari leak

Saat program membocorkan alamat (format string / puts), kita dapat bytes mentah. Ubah jadi angka:

```python
leak = u64(io.recv(6).ljust(8, b"\x00"))  # 6 byte alamat 64-bit
# atau
leak = u64(io.recvline().strip().ljust(8, b"\x00"))
```

## Contoh lengkap dalam payload

```python
from pwn import *

offset = 72
win = 0x401236

payload = b"A" * offset + p64(win)
# b'AAA...A' + b'\x36\x12\x40\x00\x00\x00\x00\x00'
```

## Catatan

- Selalu `p64`/`p32` untuk alamat, jangan string hex mentah.
- `u64` butuh 8 byte - kalau leak cuma 6 byte, padding dengan `ljust(8, b"\x00")`.
- Alamat yang dimulai `0x7f...` (libc) atau `0x7fff...` (stack) tidak mengandung null di awal - lebih mudah dipakai di payload yang lewat `strcpy`.
