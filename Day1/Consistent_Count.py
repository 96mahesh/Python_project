a = "abcabbbccaabd"
i = 0
while i < len(a):
    count = 1
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            count += 1
        else:
            break
    print(a[i], count)
    i += count


# a = "abcabbbccaabd"
# for i in range(len(a)):
#     count = 1
#     for j in range(i + 1, len(a)):
#         if a[i] == a[j]:
#             count += 1
#         else:
#             break
#
#     print(a[i], count)

