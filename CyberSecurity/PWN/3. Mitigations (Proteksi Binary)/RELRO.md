#cybersecurity

RELRO (RELocation Read-Only) mengontrol apakah **GOT bisa ditulis**. GOT adalah tabel alamat fungsi libc - kalau bisa ditulis, kita bisa mengubah arah panggilan fungsi (GOT overwrite).

## Dua mode RELRO

| Mode | GOT | Implikasi |
|---|---|---|
| **Partial RELRO** | `.got` writable, `.got.plt` writable | **GOT overwrite bisa!** |
| **Full RELRO** | Semua read-only | GOT overwrite tidak bisa |

```bash
checksec --file=chall
# RELRO: Partial RELRO   -> GOT overwrite mungkin
# RELRO: Full RELRO      -> GOT aman
```

## Mengapa Partial RELRO default?

Full RELRO butuh resolve semua fungsi di awal (lazy binding dimatikan) - sedikit lebih lambat. Banyak compiler memakai partial default, dan itu celah.

## GOT overwrite singkat

Idenya: panggilan `puts(x)` sebenarnya `puts@plt` → membaca alamat dari `puts@got` → lompat ke libc. Kalau isi `puts@got` kita ganti dengan `system`, maka `puts(x)` jadi `system(x)`.

```python
# payload (format string write atau overflow):
# tulis alamat system ke puts@got
# lalu panggil puts("/bin/sh") -> system("/bin/sh")
```

Lengkap di [[8. GOT dan PLT]].

## Bypass Full RELRO

Kalau GOT terkunci, alternatif:

1. **ret2libc / ROP** - tidak menyentuh GOT
2. **__free_hook / __malloc_hook** (glibc) - hook di libc yang writable; overwrite dengan system → `free("/bin/sh")` = system("/bin/sh")
3. **Overwrite function pointer lain** (vtable, callback)

## Catatan

- Full RELRO membuat GOT read-only **setelah program start** (masih writable saat dynamic linker resolve di awal - tapi sulit dieksploitasi).
- `checksec` wajib dijalankan: partial vs full mengubah seluruh strategi.
- Kombinasi umum: Partial RELRO + format string = GOT overwrite klasik ([[6. Format String]]).
