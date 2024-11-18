print(ord('a'))
uc = ord('a') + 5
print(chr(uc))

data = "Earth is the third planet from the sun and the only astronomical object known to harbour and support life."

enc_data = ""
for c in data:
    if c == " ":
        enc_data = enc_data+c
    else:
        enc_data = enc_data+chr(ord(c)+5)

print(enc_data)