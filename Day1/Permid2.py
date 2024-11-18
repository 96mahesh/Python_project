for i in range(1, 5+1):
    for s in range(i, 5):
        print(end=" ")
    for j in range(1, i+1):
        print("* ", end="")
    print()
for i in range(1, 5+1):
    for s in range(1, i):
        print(end=" ")
    for j in range(i, 5 + 1):
        print("* ", end="")
    print()
