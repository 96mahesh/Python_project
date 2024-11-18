# while loop

# print 1........10 numbers

# i = 1 #initlizition
#
# while i<=10:
#     print(i , end=" ")
#     i=i+1
#
# print()
#print('Done!!!')

# print 10........1 numbers descending order

# i = 10
#
# while i>=1 :
#     print(i , end=" ")
#     i= i-1
#
# print()
# print('Done !!!!!')


#Reverse of number do while loop
# n = 123
# temp = n
# rev = 0
#
# while n>0 :
#     rem = n%10
#     rev = rev*10+rem
#     n = n//10
# print(rev,end=" ")
# if temp==n :
#     print("is palindrome")
# else :
#     print("is not palindrome")

#Reverse of number do while loop

# num = 123
# s = 0
#
# while num>0 :
#     rem = num%10
#     s = s+rem
#     num = num//10
#
# print(s)

## Fibinocii serices
n = 10
a = 0
b = 1
print(a," ",b)
next_number = b
count = 1

while count <= n:
    print(next_number, end=" ")
    count += 1
    num1, a = b, next_number
    next_number = a + b
print()








