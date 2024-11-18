sum = 30
s = {-1, 2, 36, 10, 31, 42, 41, 45};
a = list(s)
for i in range(len(a)):
    for j in range(len(a)):
        if a[i] + a[j] == 30:
            print(a[i])
