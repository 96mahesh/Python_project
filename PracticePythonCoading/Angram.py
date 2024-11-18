m = "mahesh"
n = "hseham"

a = list(m)
b = list(n)

for i in range(len(a)):
    for j in range(len(a)):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

for i in a:
    print(i, end=" ")

for k in range(len(b)):
    for l in range(len(b)):
        if b[k] > b[l]:
            temp = b[k]
            b[k] = b[l]
            b[l] = temp

print()
for i in b:
    print(i, end=" ")

print()
if a == b:
    print("is Anagram")
else:
    print("Is not Anagram")