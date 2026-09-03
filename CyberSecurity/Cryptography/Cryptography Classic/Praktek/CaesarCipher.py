cipher = "L ORYH FUBSWR"

def caesar_shift(text, shift):
    result = ""
    for ch in text:
        if 'a' <= ch <= 'z':
            result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        elif 'A' <= ch <= 'Z':
            result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += ch
    return result

for shift in range(26):
    print(f"shift {shift:2d}: {caesar_shift(cipher, shift)}")