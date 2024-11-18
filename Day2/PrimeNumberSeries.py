lw, up = 900, 1000
for i in range(lw, up + 1):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i)
