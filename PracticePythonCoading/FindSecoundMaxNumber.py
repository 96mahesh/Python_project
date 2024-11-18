n = [5, 1, 9, 6, 7, 9]
max = n[0]
max1 = n[0]

for i in range(1, len(n)):
    if n[i] < max:
        max = max1
        max = n[i]
    elif n[i] < max:
        max = n[i]

print(max1)

