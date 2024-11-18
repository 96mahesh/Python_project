name = "mahesh"
a = list(name)
count = 0
for i in range(len(a)):
    if a[i] == 'a' or a[i] == 'e' or a[i] == 'i' or a[i] == 'o' or a[i] == 'u':
        count = count+1
print(count)

n = "mahesh"
r = [a[i] for i in range(len(a)-1, -1, -1)]
print(r)

n = "mahesh"
ovwels = 'aeiou'
count = 0
for i in n:
    if i in ovwels:
        count+= 1;

print(count)

na = "mahesh"
b = list(na)
count = 0
for i in na:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count = count+1
print(count)