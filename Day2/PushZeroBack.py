a = [1, 0, 2, 0, 3, 5, 0, 6, 0, 8, 0]
j = 0
for i in range(len(a)):
    if not (a[i] == 0):
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
        j = j + 1
        

for i in a:
    print(i, end=" ")
