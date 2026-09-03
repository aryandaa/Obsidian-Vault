def autokey_decrypt(cipher, primer):
    primer = primer.upper()
    cipher = [c for c in cipher.upper() if c.isalpha()]
    plain = []
    
    key_stream = [ord(k) - ord('A') for k in primer]
    
    for i, c in enumerate(cipher):
        c_val = ord(c) - ord('A')
        k_val = key_stream[i]
        p_val = (c_val - k_val) % 26
        plain.append(chr(p_val + ord('A')))
        key_stream.append(p_val)
        
    return "".join(plain)

def beaufort_cipher(text, key):
    text = [c for c in text.upper() if c.isalpha()]
    key = [c for c in key.upper() if c.isalpha()]
    result = []
    k_len = len(key)
    
    for i, ch in enumerate(text):
        c_val = ord(ch) - ord('A')
        k_val = ord(key[i % k_len]) - ord('A')
        out_val = (k_val - c_val) % 26
        result.append(chr(out_val + ord('A')))
        
    return "".join(result)

if __name__ == "__main__":
    # Test Autokey
    cipher_auto = "QNXEGUKXGD"
    primer = "QUEEN"
    print("Autokey Decrypt :", autokey_decrypt(cipher_auto, primer))
    
    # Test Beaufort
    pesan = "SECRET"
    kunci = "KEY"
    enc = beaufort_cipher(pesan, kunci)
    dec = beaufort_cipher(enc, kunci)
    print(f"Beaufort Encrypt: {enc}")
    print(f"Beaufort Decrypt: {dec}")
