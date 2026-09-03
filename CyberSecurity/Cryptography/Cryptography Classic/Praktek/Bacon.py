BACON_DICT_26 = {
    format(i, '05b').replace('0', 'A').replace('1', 'B'): chr(i + ord('A'))
    for i in range(26)
}

BACON_INV_DICT_26 = {v: k for k, v in BACON_DICT_26.items()}

def bacon_encode(text):
    clean = [c for c in text.upper() if c.isalpha()]
    return " ".join(BACON_INV_DICT_26.get(c, "") for c in clean)

def bacon_decode_ab(text):
    clean = [c for c in text.upper() if c in ('A', 'B')]
    result = []
    for i in range(0, len(clean) - 4, 5):
        chunk = "".join(clean[i:i+5])
        result.append(BACON_DICT_26.get(chunk, '?'))
    return "".join(result)

def bacon_decode_case(text):
    ab_stream = []
    for ch in text:
        if ch.isalpha():
            ab_stream.append('B' if ch.isupper() else 'A')
    return bacon_decode_ab("".join(ab_stream))

if __name__ == "__main__":
    msg = "FLAG"
    encoded = bacon_encode(msg)
    print(f"Pesan       : {msg}")
    print(f"Bacon Encode: {encoded}")
    print(f"Bacon Decode: {bacon_decode_ab(encoded)}")
    
    stego = "fLaG iS HeRe"
    print(f"Stego Teks  : {stego}")
    print(f"Stego Decode: {bacon_decode_case(stego)}")
