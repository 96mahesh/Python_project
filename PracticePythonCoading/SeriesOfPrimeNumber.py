l = 10
u = 100

for i in range(l, u + 1):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i)

lower = 10
upper = 100

for i in range(lower, upper + 1):
    count = 0
    for j in range(1, i + 1):
        if (i % j) == 0:
            count += 1
    if count == 2:
        print(i, end=" ")
