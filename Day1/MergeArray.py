a = [1,2,3]
b = [3,4,5]

length = len(a) + len(b);
print(length)

res = []
for i in range(len(a)):
    res.append(a)
for j in range(len(b)):
    res.append(a)

print(res)