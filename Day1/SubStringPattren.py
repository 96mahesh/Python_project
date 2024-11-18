name = "mahesh"
a = list(name)

for i in range(len(a)):
    for j in range(i+1):
        print(a[j], end=" ")
    print()

print()
name = "mahesh"
a = list(name)

for i in range(len(a)):
    for j in range(i,len(a)):
        for k in range(i, j+1):
            print(a[k], end=' ')
        print()
