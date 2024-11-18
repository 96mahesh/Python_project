for i in range(1, 7):
    for j in range(1, 10):
        if j == 1 and (1 < i < 5) or (i == 1 or i == 5) and (1 < j < 6) or j == 6 and 2 < i < 5 or i == 3 and (
                3 < j < 8) or j == 8 and i > 3:
            print('*', end=" ")
        else:
            print(" ", end=" ")
    print()
