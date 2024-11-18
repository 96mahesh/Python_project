test_list = [2, 6, 6, 6, 6, 5, 4, 6, 6, 8, 4, 6, 6, 6, 2, 6]
print("The original list is : " + str(test_list))
K, N = 6, 3
res = []
a, end = 0, 0
prev = 1
for idx, ele in enumerate(test_list):
    if ele == K:
        end = idx # 1 2 3 4 7 8 11 12 13 15
        if prev != K:
            print(prev)
            a = idx # 1 7 11 15
    else:

        if prev == K and end - a + 1 >= N:
            res.append((a, end))
    prev = ele

# printing result
print("The extracted ranges : " + str(res))
