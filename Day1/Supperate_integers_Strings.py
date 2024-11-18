import re

name = "mahesh@1234"
n = []
for c in name:
    if 'a' <= c <= 'z':
        n.append(c)
print(n)
x = ''.join(n)
print(x)

name = "mahesh@1234"
n = []
for char in name:
    if char.isdigit():
        n.append(char)
new_str = int(''.join(n))
print(new_str)


input_string = "abc123def456@#$"

# Separate digits and letters
letters = ''.join(re.findall(r'[A-Za-z]', input_string))
digits = ''.join(re.findall(r'\d', input_string))
spl = ''.join(re.findall(r'[^a-zA-Z0-9]', input_string))

print(f"Letters: {letters}")
print(f"Digits: {digits}")
print(f"spl: {spl}")
