s = 'pawan kalyan is a good politician'
res = []
a = ''
for c in s:
    if c == ' ':
        res.append(a)
        a = ''
    else:
        a = a+c
res.append(a)
print(res)

name = 'pawan kalyan is a good politician'
res = []
res.append(name)
print(res)