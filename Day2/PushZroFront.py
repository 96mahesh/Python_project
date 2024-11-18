n = [1, 0, 2, 0, 3, 5, 0, 6, 0, 8, 0]
print(n)

j = 0

for i in range(len(n)):
    if n[i] == 0:
        temp = n[i]
        n[i] = n[j]
        n[j] = temp
        j = j + 1

for i in n:
    print(i)
