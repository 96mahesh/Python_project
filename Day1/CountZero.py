n = 10204050
a = str(n)
print(a)
count = 0
for i in a:
    if i == '0':
        count = count + 1
print(count)