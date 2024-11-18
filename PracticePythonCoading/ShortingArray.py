n = [40, 30, 10, 20, 50]

for i in range(len(n)):
    for j in range(len(n)):
        if n[i] > n[j]:
            temp = n[i]
            n[i] = n[j]
            n[j] = temp

for i in n:
    print(i,end=" ")

print()
for i in range(len(n)):
    for j in range(len(n)):
        if n[i] < n[j]:
            temp = n[i]
            n[i] = n[j]
            n[j] = temp

for i in n:
    print(i,end=" ")


