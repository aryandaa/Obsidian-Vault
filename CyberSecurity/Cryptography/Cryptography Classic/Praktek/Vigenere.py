def vigenere_decrypt(cipher, key):
    res, ki = "", 0
    for c in cipher.upper():
        res += chr((ord(c) - ord(key[ki % len(key)].upper())) % 26 + 65) if c.isalpha() else c
        ki += c.isalpha()
    return res

# Kalau kunci sudah ketahuan
cipher = "VFLQ HPEJ XWDB"
print(vigenere_decrypt(cipher, "KEY"))