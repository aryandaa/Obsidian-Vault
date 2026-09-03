from collections import Counter

def calculate_ioc(text):
    if isinstance(text, list):
        text = "".join(text)
    clean_text = [c for c in text.upper() if c.isalpha()]
    N = len(clean_text)
    if N <= 1:
        return 0.0
    counts = Counter(clean_text)
    numerator = sum(f * (f - 1) for f in counts.values())
    denominator = N * (N - 1)
    return numerator / denominator

def find_vigenere_key_length(ciphertext, max_len=10):
    clean = [c for c in ciphertext.upper() if c.isalpha()]
    print(f"Total huruf: {len(clean)}")
    print(f"IoC teks utuh: {calculate_ioc(clean):.4f}\n")
    
    print("Mencoba perkiraan panjang kunci (rata-rata IoC):")
    for k in range(1, max_len + 1):
        slices = [clean[i::k] for i in range(k)]
        avg_ioc = sum(calculate_ioc(s) for s in slices) / k
        status = "<- KEMUNGKINAN KUNCI!" if avg_ioc >= 0.060 else ""
        print(f"Panjang k={k:2d}: IoC rata-rata = {avg_ioc:.4f} {status}")

if __name__ == "__main__":
    sample = "QPWKALVRXCQZIKGRBPWFAOMMYVGNKCLGHSJBYVGNKCLGHSJBY" * 2
    find_vigenere_key_length(sample, max_len=6)
