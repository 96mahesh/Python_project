name = "Earth is the third planet from the sun and the only astronomical object known to harbour and support life."

print(ord('a'))
uc = ord('a')+5
print(chr(uc))

enc_char = ''

for c in name:
    if c == ' ':
        enc_char = enc_char+c
    else:
        enc_char = enc_char+chr(ord(c)+5)

print(enc_char)