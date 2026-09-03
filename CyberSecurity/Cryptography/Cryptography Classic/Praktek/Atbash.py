text = "SVOOL"
result = ""
for ch in text:
    if 'a' <= ch <= 'z':
        result += chr(ord('z') - (ord(ch) - ord('a')))
    elif 'A' <= ch <= 'Z':
        result += chr(ord('Z') - (ord(ch) - ord('A')))
    else:
        result += ch
print(result)  # HELLO