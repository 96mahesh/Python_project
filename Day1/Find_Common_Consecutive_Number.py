#n = [4, 5, 5, 5, 3,8]
n = [1, 1, 1, 64, 23, 64, 22, 22, 22]
a = len(n)

for i in range(a-2):
    if n[i] == n[i+1] and n[i+1] == n[i+2]:
        print(n[i], i)
