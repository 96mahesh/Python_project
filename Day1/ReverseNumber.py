a = [1, 2, 3, 4, 5, 6]
print("Before Reverse", a)

# for i in range(len(a) - 1, -1, -1):
#      print("After Reverse", a[i])

n = a[-1::-1]
for i in n:
    print(i,end=' ')
