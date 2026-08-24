#tools

gdb adalah debugger standar Linux. **pwndbg** (atau gef) adalah plugin yang membuatnya jauh lebih ramah untuk PWN: menampilkan stack, register, dan heap secara visual.

## Install pwndbg

```bash
git clone https://github.com/pwndbg/pwndbg
cd pwndbg && ./setup.sh
# alternatif: gef (https://github.com/hugsy/gef)
```

## Perintah gdb dasar

```bash
gdb ./chall

(gdb) info functions          # daftar fungsi
(gdb) info registers          # lihat semua register
(gdb) disassemble main        # disassembly main
(gdb) break *0x401236         # breakpoint di alamat
(gdb) break main              # breakpoint di fungsi
(gdb) run                     # jalankan
(gdb) run < <(python3 -c "print('A'*100)")   # jalankan dengan input
(gdb) continue                # lanjutkan
(gdb) nexti / stepi           # eksekusi instruksi
(gdb) x/20gx $rsp             # dump 20 qword dari stack
(gdb) x/20i $rip              # dump instruksi dari RIP
(gdb) p $rdi                  # print nilai register
(gdb) quit
```

## Fitur pwndbg

```bash
(gdb) stack 20          # lihat stack dengan label
(gdb) heap              # lihat heap chunks
(gdb) bins              # lihat bins (fastbin, tcache, unsorted)
(gdb) got               # lihat GOT
(gdb) plt               # lihat PLT
(gdb) rop               # cari gadget ROP
(gdb) cyclic 200        # generate pattern
(gdb) pie               # info PIE
(gdb) retaddr           # alamat return address
(gdb) vmmap             # peta memory (cari libc base)
```

## Alur debugging exploit

```bash
gdb ./chall
(gdb) break vuln        # break di fungsi vuln
(gdb) run
(gdb) stack 20          # lihat layout stack
(gdb) p $rbp            # base pointer
(gdb) x/20gx $rsp       # isi stack
(gdb) continue          # lanjut sampai crash
# pwndbg: "Program received signal SIGSEGV"
#         "RIP: 0x6161616c" -> cyclic_find(0x6161616c)
```

## Debug exploit pwntools di dalam gdb

```python
from pwn import *

io = gdb.debug("./chall", gdbscript="""
    break vuln
    continue
""")
io.sendlineafter(b": ", payload)
io.interactive()
```

Atau attach ke proses yang sedang jalan:

```python
io = process("./chall")
gdb.attach(io, "continue")
```

## Tips

1. `vmmap` - wajib untuk melihat base libc saat runtime.
2. `cyclic` di pwndbg - generate pattern langsung tanpa keluar gdb.
3. Core dump: `ulimit -c unlimited`, lalu `gdb ./chall core` untuk analisis crash.
4. Kalau exploit jalan di gdb tapi crash di luar gdb → biasanya masalah ASLR/alignment (bukan bug di exploit).
