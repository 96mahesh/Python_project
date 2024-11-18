n = 20
pre = 0

for i in range(1, n):
    fact = 0
    for j in range(1, i + 1):
        if (i % j) == 0:
            fact += 1
# print(fact)
# if fact == 2:
#     print("it is a prime number")
# else:
#     print("it is not a prime number")
if fact == 2:
    if pre < i:
        pre = i
print(pre)