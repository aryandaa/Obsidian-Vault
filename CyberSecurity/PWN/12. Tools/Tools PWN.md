#tools

Tools yang membantu selama belajar PWN. Yang paling penting:

1. [pwntools](pwntools.md) - library exploit Python (wajib!)
2. [gdb dan pwndbg](gdb%20dan%20pwndbg.md) - debugger untuk melihat memory & register
3. [checksec](checksec.md) - cek proteksi binary
4. [objdump dan readelf](objdump%20dan%20readelf.md) - baca struktur & disassembly binary
5. [Ghidra](Ghidra.md) - decompiler (membaca source code dari binary)
6. [ROPgadget dan ropper](ROPgadget%20dan%20ropper.md) - cari gadget ROP

Tools lain yang berguna:

- **strings** - ekstrak string: `strings chall | grep -i flag`
- **file** - identifikasi jenis binary: `file chall`
- **ldd** - lihat dependency libc: `ldd chall`
- **one_gadget** - cari one gadget di libc
- **seccomp-tools** - cek syscall yang diizinkan (seccomp)
- **gdb-gef** / **pwndbg** - alternatif plugin gdb
- **patchelf** - ganti interpreter/libc binary (untuk debugging)
- **pwninit** - otomatis setup challenge (patchelf + libc)
- **checksec.sh** - versi mandiri checksec
