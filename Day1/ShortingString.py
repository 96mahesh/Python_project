name = "mahesh"

a = list(name)
print(a)

for i in range(len(a)):
    for j in range(len(a)):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

for i in a:
    print(i, end=" ")
