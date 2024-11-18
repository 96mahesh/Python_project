str = 'mahesh babu rampatruni'
res = ''
l = len(str)-1
while l >= 0:
    res = res + str[l];
    l = l - 1
print(res)

for i in range (len(str)-1,-1,-1):
    print(str[i], end="")

