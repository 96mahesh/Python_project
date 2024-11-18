n = 10
a, b = 0, 1
print(a,"\n",b)
while n >= 0:
    c = a + b
    if c > n:
        break
    print(c)
    a = b
    b = c


