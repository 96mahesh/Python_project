max = 10
a, b, c = 0, 1, 0
print(a, b)
while c <= max:
    c = a + b
    if c > max:
        break
    print(c, end=" ")
    a = b
    b = c
