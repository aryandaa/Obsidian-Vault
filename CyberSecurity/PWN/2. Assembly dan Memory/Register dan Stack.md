#cybersecurity

Register adalah "variabel" milik CPU, dan stack adalah area memory tempat data & alamat kontrol disimpan. Buffer overflow pada dasarnya adalah **menulis melebihi batas di stack** sehingga register kontrol (return address) ikut tertimpa.

## Register penting

| Register | Fungsi |
|---|---|
| `RAX/EAX` | Return value, syscall number |
| `RDI/EDI` | Argumen ke-1 (x64) / operan umum (x86) |
| `RSI/ESI` | Argumen ke-2 (x64) |
| `RDX/EDX` | Argumen ke-3 (x64) |
| `RSP/ESP` | Stack pointer - puncak stack |
| `RBP/EBP` | Base pointer - dasar frame fungsi |
| `RIP/EIP` | Instruction pointer - **alamat instruksi berikutnya** |

**RIP adalah target utama exploit**: kalau kita bisa menimpa RIP, kita bisa memilih instruksi apa yang dieksekusi berikutnya.

## Stack

Stack tumbuh **ke bawah** (alamat mengecil). Setiap fungsi punya **stack frame**:

```
Alamat tinggi (0x7fff...)
+-------------------------+
|        argumen          |
+-------------------------+
| return address  <- RIP  |  <-- yang kita timpa!
+-------------------------+
| saved RBP               |
+-------------------------+
|   local variables       |
|   (buffer)              |  <-- input kita masuk sini
+-------------------------+  <- RSP
Alamat rendah
```

Ketika fungsi memanggil `ret`, CPU mengambil 8 byte di puncak stack sebagai **return address** dan memuatnya ke RIP. Kalau kita menimpa return address dengan alamat fungsi lain → alur program berubah.

## Ilustrasi buffer overflow sederhana

```c
void vuln() {
    char buf[64];          // buffer 64 byte di stack
    gets(buf);             // BUG: tidak batasi panjang input
}                          // ret -> pakai return address dari stack
```

Input 72+ byte:

```
72 byte pertama -> memenuhi buf[64] + saved RBP
8 byte berikut  -> menimpa return address
```

Kalau kita isi dengan alamat `win()` → saat `ret`, program lompat ke `win()`.

## Alamat stack vs alamat fungsi

- Fungsi punya alamat **tetap** di binary (kalau tanpa PIE): `0x401236` dst.
- Stack address (buffer, RSP) **acak** karena ASLR: `0x7fff...`

Ini menentukan teknik: ret2win (lompat ke fungsi) lebih mudah daripada ret2shellcode (butuh alamat stack yang bocor).

## Cara melihat stack di gdb

```bash
gdb ./chall
(gdb) break *vuln+20
(gdb) run
(gdb) stack 20          # pwndbg: lihat stack
(gdb) x/20gx $rsp       # dump 20 qword dari RSP
(gdb) info registers    # lihat semua register
```

## Konsep kunci

1. **Stack frame** = area milik satu fungsi (local vars + saved RBP + return address).
2. **Return address** berada **di atas** buffer - itu sebabnya menimpa buffer = menimpa kontrol alur.
3. Offset = jarak dari awal buffer ke return address. Hitung dengan pattern (lihat [[4. Buffer Overflow]]).
4. Alamat dalam payload harus **little endian**: `p64(0x401236)`.
