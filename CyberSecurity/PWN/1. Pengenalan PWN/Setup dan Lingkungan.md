#cybersecurity

PWN butuh lingkungan yang tepat. Kamu tidak bisa main-main dengan memory di sembarang OS - setup yang benar akan menghemat banyak waktu.

## OS yang disarankan

- **Kali Linux** - sudah include kebanyakan tools (gdb, pwndbg bisa diinstall, python3, dll)
- **Ubuntu/Debian** - paling umum untuk target CTF (libc sama dengan banyak challenge)
- VM: VirtualBox/VMware dengan Ubuntu 22.04/24.04 (versi libc sering cocok dengan challenge)

## Tools wajib

```bash
# Python 3 + pip
sudo apt install python3 python3-pip

# pwntools - library exploit utama
pip3 install pwntools

# gdb + pwndbg (debugger dengan tampilan memory & stack)
git clone https://github.com/pwndbg/pwndbg
cd pwndbg && ./setup.sh

# checksec - cek proteksi binary (sudah include di pwntools)
checksec --file=./chall

# Binutils - objdump, readelf
sudo apt install binutils

# ghidra - decompiler (GUI)
# download dari https://ghidra-sre.org/
```

## Alat bantu lain

```bash
# strings - ekstrak string dari binary
strings chall
strings chall | grep -i flag

# ROPgadget - cari gadget ROP
ROPgadget --binary chall
# atau dari pwntools
python3 -c "from pwn import *; print(ROP(ELF('./chall')))"

# one_gadget - cari one gadget di libc
one_gadget /lib/x86_64-linux-gnu/libc.so.6
```

## Struktur folder kerja

Buat folder per challenge:

```
chall/
├── chall          # binary
├── libc.so.6      # libc yang dipakai (kalau diberikan)
├── solve.py       # exploit script
└── notes.md       # catatan analisis
```

## Menjalankan challenge remote

```bash
# Local
./chall

# Remote
nc host.ctf.com 1337
```

## Tips penting

1. **Match libc** - kalau challenge memberi `libc.so.6`, gunakan itu di exploit (`libc = ELF("./libc.so.6")`), bukan libc sistem.
2. **Versioning** - Python 3.8+ dan pwntools versi terbaru.
3. **Testing** - uji exploit di lokal dulu (kalau bisa), baru remote.
4. **Docker** - beberapa challenge butuh environment spesifik; pakai docker image yang disarankan CTF.
