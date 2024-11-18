s = 'mahesh babu rampatruni'

res = []
a = ''

for i in s:
    if i == ' ':
        res.append(a)
        a = ''
    else:
        a = a+i;
res.append(a)
print(res)