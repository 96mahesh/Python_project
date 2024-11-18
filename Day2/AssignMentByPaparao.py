name = "hyderabad----is--a--big--city"

a = list(name)
res = "";
for i in range(len(a)):
    if 'a' <= a[i] <= 'z':
        res = res+a[i];
    else:
        if 'a' <= a[i - 1] <= 'z':
            res = res + " ";

print(res)