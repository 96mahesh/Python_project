n = 10
a, b = 0, 1
print(a)
print(b)
for i in range(2,n+1):
    c = a + b
    a = b
    b = c
    if c > n:
        break
    print(c)