n = [10,60,20,40,30,50]
max = n[0]

for i in range(1,len(n)):
    if n[i]>max:
        max = n[i]
print(max)

##min number in array
print()
a = [10,60,20,40,30,50]
min = a[0]
for i in range(1,len(a)):
    if a[i]<min:
       min = a[i]

print(min)