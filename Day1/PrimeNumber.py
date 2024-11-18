n = 7
count = 0
for i in range(1, n + 1):
    if (n % i) == 0:
        count = count + 1
if count == 2:
    print('This no is a prime')
else:
    print('This no is not a prime')
