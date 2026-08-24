#tools

checksec menampilkan proteksi yang aktif di binary - **langkah pertama wajib** sebelum menyusun exploit. Materi lengkap: [[3. Mitigations (Proteksi Binary)]].

## Menjalankan

```bash
# Versi mandiri
checksec --file=./chall

# Dari pwntools (CLI)
python3 -c "from pwn import *; print(ELF('./chall').checksec())"
```

## Contoh output

```
[*] '/home/user/chall'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      PIE disabled
```

## Membaca & menentukan strategi

| Output | Arti | Dampak |
|---|---|---|
| `No canary found` | Tidak ada canary | Overflow langsung menimpa return address |
| `Canary found` | Ada canary | Butuh leak canary / bypass |
| `NX enabled` | Stack tidak executable | Tidak bisa ret2shellcode; pakai ROP |
| `NX disabled` | Stack executable | Ret2shellcode bisa |
| `PIE disabled` | Alamat binary tetap | `elf.sym` langsung valid |
| `PIE enabled` | Alamat binary acak | Butuh leak PIE base |
| `Partial RELRO` | GOT writable | GOT overwrite bisa |
| `Full RELRO` | GOT read-only | GOT overwrite tidak bisa |

## Strategi cepat

```text
No canary + NX disabled + No PIE  -> ret2shellcode
No canary + NX enabled  + No PIE  -> ret2win / ret2libc
No canary + NX enabled  + PIE     -> leak PIE -> ret2libc
Canary   + ...                    -> leak canary dulu
```

## Cek ASLR (level OS)

```bash
cat /proc/sys/kernel/randomize_va_space
# 0 = off, 1 = sebagian, 2 = penuh (default)
```

## Catatan

- checksec membaca binary **lokal** - pastikan binary challenge sama dengan yang di server.
- Kalau hanya punya akses remote (nc), coba cari binary-nya di attachment CTF.
- `PIE disabled` + `NX disabled` + `No canary` = challenge paling ramah pemula.
