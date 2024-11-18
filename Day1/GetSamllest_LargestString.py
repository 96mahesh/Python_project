s = "welcometojava"
k = 3

min_sub = s[0:k]
max_sub = s[0:k]

for i in range(len(s) - k + 1):
    sub = s[i:i+k]
    if sub < min_sub:
        min_sub = sub
    if sub > max_sub:
        max_sub = sub

print(min_sub)
print(max_sub)