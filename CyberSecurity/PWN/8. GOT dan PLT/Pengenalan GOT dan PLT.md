#cybersecurity

Saat program dynamic memanggil fungsi libc (misal `puts`), dia tidak langsung tahu alamat puts di libc (karena ASLR). Dia memakai **PLT** dan **GOT**.

## Alur panggilan fungsi

```text
program memanggil puts("hi")
        |
        v
puts@plt  (stub kecil di binary)
        |
        v
puts@got  (tabel berisi alamat puts di libc)
        |
        v
alamat puts di libc (ASLR, diisi dynamic linker)
```

- **PLT** - potongan kode di binary untuk setiap fungsi yang dipanggil
- **GOT** - tabel berisi **alamat sebenarnya** fungsi di libc

## Lazy binding

Awalnya `puts@got` menunjuk balik ke PLT (untuk resolve). Saat pertama kali `puts` dipanggil, dynamic linker mencari alamat puts di libc, **mengisi `puts@got`**, lalu eksekusi berjalan normal. Panggilan berikutnya langsung lewat GOT.

## Kenapa ini penting untuk PWN?

1. **Leak** - isi `puts@got` = alamat puts di libc. Kalau kita bisa membuat program mencetak isi GOT (misal `puts(puts@got)`), kita leak libc → hitung base ([[Ret2libc]]).
2. **GOT overwrite** - kalau GOT writable (Partial RELRO), kita ubah isi `puts@got` jadi `system` → semua panggilan `puts(x)` jadi `system(x)`.

## Lihat PLT & GOT

```bash
# symbol
readelf -s chall | grep -E "puts|system"

# relokasi (GOT)
readelf -r chall

# disassembly PLT
objdump -d chall | grep -A5 "<puts@plt>"
```

Dengan pwntools:

```python
from pwn import *
elf = ELF("./chall")
elf.plt["puts"]   # alamat stub PLT
elf.got["puts"]   # alamat entri GOT
```

## Contoh leak via GOT

```python
# panggil puts(puts@got) - cetak isi GOT = alamat puts di libc
payload = b"A"*offset + p64(elf.plt.puts) + p64(elf.sym.main) + p64(elf.got.puts)
```

Lihat alur lengkap di [[Ret2libc]].

## GOT overwrite singkat

```python
# timpa puts@got dengan system (via format string / overflow)
payload = fmtstr_payload(pos, {elf.got.puts: libc.sym.system})
```

Lengkap di [[GOT Overwrite]].

## Istilah

| Istilah | Arti |
|---|---|
| PLT | Stub pemanggil fungsi (di binary) |
| GOT | Tabel alamat fungsi libc |
| GOT entry | Satu entri per fungsi |
| Resolve | Proses mengisi GOT pertama kali |
| Lazy binding | Resolve saat fungsi pertama dipanggil |

## Catatan

- `puts@plt` → alamat untuk **memanggil** puts.
- `puts@got` → alamat yang **isinya** alamat puts di libc.
- GOT writable hanya kalau **Partial RELRO** (lihat [[RELRO]]). Full RELRO → GOT read-only.
