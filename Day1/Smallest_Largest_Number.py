n = [-1, 2, 3, 4, 5, 6, 7, 8, 9, -10]
s, l = 0, 0

for i in n:
    if i > l:
        l = i
    if i < s:
        s = i
print(l, s)

def find_max_min(numbers):
    max_num = max(numbers)
    min_num = min(numbers)
    return (max_num, min_num)

numbers = [-1, 2, 3, 4, 5, 6, 7, 8, 9, -10]
result = find_max_min(numbers)
print(result)
