for i in range(1, 5 + 1):
    for s in range(i, 6):
        print(end="  ")
    for j in range(1, i * 2):
        if j == 1 or j == i:
            print("* ", end="  ")
        else:
            print("  ", end="  ")
    print()


for i in range(1, 5+1):
    for s in range(1, i+1):
        print(end="  ")
    for j in range(2*i+1, 12):
        if j == 2*i+1 or j == 10:
            print("* ", end="  ")
        else:
            print(" ", end=" ")
    print()