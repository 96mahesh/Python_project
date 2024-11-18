# for loop

# print 0 .... 9 numbers
# for i in range(10 ):
#     print(i,end=" ")

print()
# print 1 .... 10 numbers
# for i in range(1,11 ):
#     print(i,end=" ")
#
# print only even numbers between 1 ... 20

for i in range(2, 20, 2):
    print(i, end=" ")

print()

# print only odd numbers between 1 ... 20

for i in range(1, 20, 2):
    print(i, end=" ")

# Print 1.. 10 number descending order

print()
for i in range(10, 0, -1):
    print(i, end=" ")

# print 5,10,15,20 ......100
print()
# for i in range(5, 101, 5):
#     print(i, end=" ")
#
# # Reverse of String
# print()
# str = 'mahesh'
# string = [str[i] for i in range(len(str)-1, -1, -1)]
# print(string)


#str = input("enter value :")

# for i in range(len(str)-1,-1,-1) :
#     print(str[i],end=' ')
#
# a = [str[i] for i in range(len(str))]
#
# for i in range(len(a)-1,-1,-1) :
#      for j in range(len(a)-1,-1,-1) :
#         if a[i]==a[j]:
#               c  = a[i]
#               a[i] = a[j]
#               a[j] = c
#      print(a[i],end=' ')

# str = 'mahesh'
#Repeted Numbers
# for i in str :
#     for i in range(len(str)) :
#         count = 0
#         for j in range(len(str)) :
#             if str[i]==str[j]:
#                 count = count+1
# print(str[i]," ",count)

#Example 12 Revrese Of String
# s = 'welcome'
#
# str = ""
# for i in s :
#  str = i+str
# print(str,end=' ')

##count accurrence

# a = [str[i] for i in range(len(str))]
# for i in range(len(a)) :
#     count = 0
#     for j in range(len(a)) :
#         if a[i] == a[j] :
#             count = count+1
#     print(str[i]," ",count)

#Push Zero frient said

# a = [1,0,5,6,0,4,0,3,8]
# j = 0
# for i in range(len(a)) :
#     if a[i] == 0:
#         temp = a[i]
#         a[i] = a[j]
#         a[j] = temp
#         j = j+1
# for i in a :
#     print(i,end=' ')

#Pairs Values

# a = [11,9,7,5,15,8]
# sum = 20
# for i in range(len(a)) :
#     for j in range(len(a)) :
#         if a[i]+a[j]==sum :
#             print(a[i])


#nameing conventions

name = 'mahesh'  #mahish

for i in name:
    for j in name :
        if i == j :
          x=i
          print(x)