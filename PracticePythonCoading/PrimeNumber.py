n = 0;
count = 0;
if n == 0:
    for i in range(1, 3):
        if (n % i) == 0:
            count = count + 1

if count == 2:
    print("prime number")
else:
    print("Not prime number")
