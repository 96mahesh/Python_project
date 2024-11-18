name = "1ab23$#@km4"

a = list(name)
alp = []
num = []
spl = []
for i in range(len(a)):
    if 'a' <= a[i] <= 'z':
        alp.append(a[i])
    elif '0' <= a[i] <= '9':
        num.append(a[i])
    else:
        spl.append(a[i])
for i in range(len(alp)):
    print(alp[i],end=' ')
print()
for i in range(len(num)):
    print(num[i],end=' ')
print()
for i in range(len(spl)):
    print(spl[i],end=' ')