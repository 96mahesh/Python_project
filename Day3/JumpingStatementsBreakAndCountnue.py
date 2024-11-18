# break continue

for i in range(1,10) :
    if i==5:
      break
    print(i,end=' ') #1 ....9


#continue
print()
for i in range(1,10) :
    if i==5 or i==7:
      continue
    print(i,end=' ') #1 ....9

print()

for i in range(3,7,2) :
    print(i,end=' ')


