for i in range(1, 8):
    for j in range(1, 65):
        if j == 1 and i > 1 or (i == 1 or i == 4) and 1 < j < 5 or j == 5 and 1 < i < 4:
            print("* ", end=" ")
        elif (i == 1 or i == 7) and 5 < j < 11 or j == 8 or i == 1 and 11 < j < 17 or j == 14:
            print("* ", end=" ")
        elif (j == 17 or j == 21) and i > 1 or (i == 1 or i == 4) and 17 < j < 21:
            print("* ", end=" ")
        elif j == 22 and i > 1 or (i == 1 or i == 4) and 22 < j < 26 or j == 26 and 1 < i < 4:
            print("* ", end=" ")
        elif (j == 27 or j == 31) and i < 7 or i == 7 and 27 < j < 31:
            print("* ", end=" ")
        elif j == 32 and i > 1 or (i == 1 or i == 4) and 32 < j < 36 or j == 36 and 1 < i < 4 or j == 28 + i and i > 3:
            print("* ", end=" ")
        elif (j == 37 or j == 41) and i > 1 or (i == 1 or i == 4) and 37 < j < 41:
            print("* ", end=" ")
        elif j == 42 or j == 48 or (j == 41 + i or j == 49 - i) and i < 5:
            print("* ", end=" ")
        else:
            print(" ", end="  ")
    print()

print()
print()
for i in range(1, 8):
    for j in range(1, 45):
        if j == 1 or j == 7 or (j == i or j == 8 - i) and i < 5 or j == 8 or i == 7 and 7 < j < 13 or (
                j == 13 or j == 17) and i > 1 \
                or (i == 1 or i == 4) and 13 < j < 17:
            print("* ", end=" ")
        elif (j == 20 and 1 < i < 6 or (
                i == 1 or i == 6) and 20 < j < 25 or j == 25 and 2 < i < 6
              or i == 3 and 22 < j < 27 or j == 27 and i > 2):
            print("* ", end=" ")
        elif (j == 28 or j == 32) and i > 1 or (i == 1 or i == 4) and 28 < j < 32:
            print("* ", end=" ")
        elif j == 33 and i > 1 or (
                i == 1 or i == 4) and 33 < j < 37 or j == 37 and 1 < i < 4 or j == 29 + i and i > 3 or (
                i == 1 or i == 7) and 37 < j < 43 or j == 40:
            print("* ", end=" ")
        else:
            print(" ", end="  ")
    print()

print()
print()

for i in range(1, 8):
    for j in range(1, 60):
        if i == 1 and j < 6 or j == 3 or (j == 6 or j == 10) and i > 1 or (i == 1 or i == 4) and 6 < j < 10:
            print("* ", end=" ")
        elif j == 11 or i == 7 and 11 < j < 16 or (j == 16 or j == 20) and i < 7 or i == 7 and 16 < j < 20:
            print("* ", end=" ")
        elif j == 21 or j == 26-i and i < 5 or j == 18+i and i > 3 or (j == 26 or j == 30) and i > 1 or (i == 1 or i == 4) and 26 < j < 30:
            print("* ", end=" ")
        else:
            print(" ", end="  ")
    print()
