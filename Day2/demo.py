
# x = int(input("enter x : "))
# y = int(input("enter y : "))
# for i in range(x,y):
#     print(i, end=' ')
# print()
# print('mahesh')

#####Pattren python####

a = int(input("enter row : "))
for i in range(a):
    for s in range(a-i-1):
     print(" ",end="")
    for j in range(i+1):
       print("*",end=" ")
    print()

######Pattren 2 #####5

for i in range(1,a):
    for s in range(i):
     print(" ",end="")
    for j in range(a-i):
       print("*",end=" ")
    print()




