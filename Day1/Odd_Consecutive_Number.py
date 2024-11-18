a, b = 60, 100
x = 1
res = []
while x + 2 < a:
    if x + (x + 2) > b:
        res.append((x, x + 2))
    x += 2
print(res)


a = 60
b = 100
if a > 0 and b > 0 and a > b / 2: # 60 > 0 and 100 > 0 and 60 > 100/2 = 50 condition true
    b //= 2
    while b <= a:
        if b % 2 != 0:
            x = b
            if x + 2 <= a:
                print(x, ',', x + 2)

        b += 1

