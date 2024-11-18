n = [10, 20, 30, 40, 50]
sum1 = 0;
res = [];
a = 0
for i in range(len(n)):
    sum1 = sum1+n[i]
print(sum1)
for i in n:
    res.append(sum1+i)
print(res)
