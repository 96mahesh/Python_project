s = 'welcomejava'
k = 3

max_sub = s[0:k]
min_sub = s[0:k]

for i in range(len(s)-k+1):
    sub = s[i:i+k]
    if sub<max_sub:
        max_sub = sub

    if sub>min_sub:
        min_sub = sub

print(max_sub)
print(min_sub)
