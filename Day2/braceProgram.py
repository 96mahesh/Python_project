str = "{{{{}}"

a = list(str)
# print(a)

uni = []
cou = []
for i in range(len(a)):
    count = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            count += 1
    # print(count,a[i])

    if len(uni) == 0:
        uni.append(a[i])
        cou.append(count)
    else:
        find = 0
        for k in range(0, len(uni)):
            if uni[k] == a[i]:
                find = find + 1
        if find == 0:
            uni.append(a[i])
            cou.append(count)

x = 0
for i in range(0, len(uni)):
    if len(a) / 2 < cou[i]:
        x = (len(a) - cou[i]) // 2
        print(x)

for i in range(0,len(uni)):
    if len(a) / 2 < cou[i]:
        cou[i] = cou[i] - x
        print(cou[i])

    else:
        cou[i] = cou[i] + x
        print(cou[i])

for i in range(0, len(uni)):
    for j in range(0,cou[i]):
        print(uni[i],end=" ")