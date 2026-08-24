#cybersecurity

NX (No-eXecute) membuat **stack dan heap tidak bisa dieksekusi**. Kalau NX aktif, shellcode yang kita taruh di buffer tidak bisa dijalankan - CPU akan menolak eksekusi dari halaman yang ditandai non-executable.

## Cek

```bash
checksec --file=chall
# NX: NX enabled
```

```bash
# Lihat segmen juga
readelf -l chall | grep GNU_STACK
# GNU_STACK ... RWE  -> executable (NX off)
# GNU_STACK ... RW   -> non-executable (NX on)
```

## Efek pada exploit

- NX **off** → ret2shellcode bisa langsung (lompat ke buffer berisi shellcode)
- NX **on** → tidak bisa eksekusi dari stack. Gantinya: **ROP** ([[5. ROP (Return Oriented Programming)]]) dan **ret2libc** - kita "menyusun" eksekusi dari instruksi yang sudah ada di bagian executable (.text, libc).

## Analogi

NX seperti menandai "area data tidak boleh dijalankan". Kamu bisa menaruh senjata (shellcode) di stack, tapi tidak bisa "menembakkan" dari sana. ROP adalah cara memakai senjata yang sudah ada di gudang (.text/libc) dengan menyusun alur lompatan.

## Ret2win tetap jalan walau NX on

Lompat ke fungsi `win()` yang sudah ada di binary **tidak melanggar NX** - instruksinya memang executable:

```python
payload = b"A"*offset + p64(win_addr)
```

Jadi NX tidak menghalangi ret2win/ret2libc; hanya menghalangi menjalankan shellcode di stack.

## Cara bypass ringkas

| Situasi | Teknik |
|---|---|
| NX on, ada fungsi win | ret2win |
| NX on, no win, libc dynamic | ret2libc |
| NX on, no win, static | ROP murni (SROP, ret2dlresolve) |
| NX off, buffer diketahui | ret2shellcode |

## Catatan

- Beberapa CTF sengaja me-nonaktifkan NX untuk mengajarkan ret2shellcode. Selalu cek dulu!
- `execstack` di binary lama (dan Windows XP) tidak punya NX - itu zaman keemasan shellcode di stack.
