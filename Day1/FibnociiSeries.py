a,b = 0,1
print(a,b)
for i in range(2,7):
    c = a+b
    a = b
    b = c
    if c >= 7:
        break
    print(c)

    