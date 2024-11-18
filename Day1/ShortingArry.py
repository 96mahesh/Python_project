a = [4, 6, 5, 2, 9]

for i in range(len(a)):
    for j in range(len(a)):
        if a[i] < a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

for i in a:
    print(i, end=" ")
