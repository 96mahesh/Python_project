for i in range(1, 5+1):
    for s in range(i, 5):
        print(end="  ")
    for j in range(1, 2*i):
        print("* ", end="")
    print()
for i in range(1, 5 + 1):
    for s in range(1, i):
        print(end="  ")
    for j in range(2 * i + 1, 12):
        print("* ", end="")
    print()
