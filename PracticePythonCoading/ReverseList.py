a = [1, 2, 3, 4]
res = []
for i in range(len(a) - 1, -1, -1):
    res.append(a[i])
print(res)

s = [1, 2, 3, 4]
r = []
l = len(s) - 1

while l >= 0:
    r.append(a[l])
    l = l - 1
print(r)

v = [1, 2, 3, 4]
print(v[::-1])

x = [1, 2, 3, 4]
y = [x[i] for i in range(len(x)-1, -1, -1)]
print(y)