name = 'paparao'

a = list(name)
print(a)

for i in range(len(a), 1):
    count = 0
    for j in range(len(a), 1):
        if a[i] == a[j]:
            count = count + 1
            print(count)
    if count == 1:
        print(a[i])
