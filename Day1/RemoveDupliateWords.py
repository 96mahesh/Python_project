name = "i am  mahesh i am an automation engineer"
a = name.split(" ")
uni = []
for i in range(len(a)):
    if len(uni) == 0:
        uni.append(a[i])
    else:
        f = 0
        for k in range(len(uni)):
            if uni[k].__eq__(a[i]):
                f = f + 1
        if f == 0:
            uni.append(a[i])

for i in range(len(uni)):
    print(uni[i], end=" ")
