s = input("Enter String Value : ")
c = input("Enter char value : ")
count = 0
for i in s:
    for j in c:
        if i == j:
            count = count + 1

print(count)

##### using while loop #####

m = "mahesh"
n = "h"
i, count = 0, 0
while i < len(m):

    if m[i] == n:
        count = count + 1
    i = i+1
print(count)


