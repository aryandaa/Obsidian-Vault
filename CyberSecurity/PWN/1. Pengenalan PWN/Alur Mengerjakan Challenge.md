#cybersecurity

Ini alur standar yang bisa kamu ikuti setiap menghadapi challenge PWN. Semakin sering mengikuti alur ini, semakin cepat kamu menemukan bug dan menyusun exploit.

## 1. Analisis awal

```bash
# Jenis file & arsitektur
file chall

# Proteksi binary
checksec --file=chall

# String yang menarik
strings chall | grep -iE "flag|shell|win|admin|password"

# Symbol (nama fungsi yang tidak di-strip)
readelf -s chall | grep FUNC
```

Catat: arsitektur (x86/x64), proteksi apa yang aktif, ada fungsi menarik (`win`, `vuln`) atau tidak.

## 2. Jalankan & observasi

```bash
./chall
```

Perhatikan:
- Ada prompt? Berapa kali input?
- Input panjang → crash? (tanda buffer overflow)
- Ada output yang menampilkan alamat? (tanda leak)

## 3. Cari bug

| Gejala | Kemungkinan bug |
|---|---|
| Input panjang → crash | Buffer overflow |
| Input `%p` menampilkan alamat | Format string |
| Input angka besar → perilaku aneh | Integer overflow |
| Bebaskan lalu pakai lagi → crash | Use after free |
| Input panjang → "stack smashing detected" | Buffer overflow + canary |

Kalau source code diberikan, baca! Itu cheat code terbaik.

## 4. Analisis lebih dalam

```bash
# Disassembly fungsi
objdump -d chall | grep -A50 "<vuln>:"

# Decompile dengan Ghidra (kalau perlu)
# Atau di gdb:
gdb ./chall
```

Tentukan:
- Ukuran buffer & offset sampai return address
- Alamat fungsi/objek yang berguna (`win`, `system`, `puts@plt`)
- Proteksi apa yang harus di-bypass

## 5. Susun exploit dengan pwntools

```python
from pwn import *

context.binary = elf = ELF("./chall")
# io = process("./chall")          # local
# io = remote("host.ctf.com", 1337) # remote

payload = b"A" * offset + p64(win_addr)
io.sendlineafter(b": ", payload)
io.interactive()
```

## 6. Hitung offset (kalau buffer overflow)

```python
from pwn import *

io = process("./chall")
io.sendlineafter(b": ", cyclic(200))
io.wait()  # crash

# cari offset dari core / dengan gdb
core = io.corefile
offset = cyclic_find(core.fault_addr)  # 64-bit
print(offset)
```

Atau manual dengan pattern:

```python
# generate pattern
print(cyclic(200))
# kalau crash menunjukkan 0x6161616c -> cari offset
cyclic_find(0x6161616c)
```

## 7. Local → Remote

1. Exploit jalan di lokal? 
2. Ganti `process()` → `remote(host, port)`.
3. Remote sering butuh: `io.recvuntil(...)` yang tepat, handle buffering, dan libc yang sama.
4. Kalau remote pakai libc berbeda → sesuaikan offset system/`/bin/sh` (lihat [[Ret2libc]]).

## 8. Dapatkan flag

```bash
$ cat flag.txt
CTF{...}
```

Atau dari shell:

```python
io.sendline(b"cat flag.txt")
print(io.recvall())
```

## Checklist cepat

- [ ] `file` + `checksec`
- [ ] `strings`
- [ ] Jalankan manual
- [ ] Tentukan bug
- [ ] Hitung offset
- [ ] Susun payload
- [ ] Test lokal → remote
- [ ] Flag!
