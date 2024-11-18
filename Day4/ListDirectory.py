# how to create List

# Mylist = [10,20,30,40]
# Mylist1 = ['apple','banana','cherry']
# Mylist2 = ['apple',10,'banana',20]
# Mylist3 = list() #Empty List
#
# print(Mylist)
# print(Mylist1)
# print(Mylist2)
# print(Mylist3)

#Example 2 Asscessing item from the list

# Mylist = ['apple','banana','cherry']
# print(Mylist[0])
# print(Mylist[1])
# print(Mylist[2])
# print(Mylist[-1])

#Example 3 Range of Index

# Mylist = ['apple','banana','cherry','orange','kiwi','mileon','mango']
# print(Mylist[2:5])#['cherry', 'orange', 'kiwi']
# print(Mylist[3:6])#['orange','kiwi','mileon']
# print(Mylist[-4:-1])#['orange', 'kiwi', 'mileon']

#Example 4 change item value
# Mylist = ['apple','banana','cherry']
# print(Mylist)
# Mylist[0]='orange' #this will change the value by index
# print(Mylist)

#Example 5 Read the list item using for loop

# Mylist = ['apple','banana','cherry','orange','kiwi','mileon','mango']
# for i in Mylist :
#     print(i)

#Example 6 check if the item is exitin the list or not
# Mylist = ['apple','banana','cherry']
# if 'apple' in Mylist :
#     print("yes Apple is present")
# else :
#     print("No apple is not preseny")

#Example 7 find the lenth of list items
# Mylist = ['apple','banana','cherry']
# print(len(Mylist))

#Example 8  Add new itens in List methods append(), insert()
# Mylist = ['apple','banana','cherry']
# Mylist.append('orange')
# print(Mylist)
# Mylist.insert(0,'mango')
# print(Mylist)

#Example 9 Remove item from list # pop() del function  clear ()
# Mylist = ['apple','banana','cherry']
# # Mylist.pop(0)
# # print(Mylist)
#
# # del Mylist[0] #This is a Keyword its not a function
# # print(Mylist)
#
# Mylist.clear()
# print(Mylist)

#Example 10 copy the list some Other list copy(function) list()
# Mylist = ['apple','banana','cherry']
# # Mylist2 = list(Mylist)
# # print(Mylist) #['apple','banana','cherry']
# # print(Mylist2) #['apple','banana','cherry']
#
# Mylist2 = Mylist.copy()
# print(Mylist2)

#Example 11 combain /join two list

#Using + Operator (concatulation)

# List1 = ['a','b','c']
# List2 = [1,2,3]
# List3 = List1 + List2
# print(List3)

#Using looping Statement

# List1 = ['a','b','c']
# List2 = [1,2,3]
# # for i in List2 :
# #     List1.append(i)
# # print(List1)
# for i in List2 :
#     List1.insert(1,i)
# print(List1)

#Using Extend

# List1 = ['a','b','c']
# List2 = [1,2,3]
#
# List1.extend(List2)
# print(List1)

# Exaple 12 compare tuple

# List1 = ['a','b','c']
# List2 = [1,2,3]
#
# if List1 == List2:
#     print("List are equals")
# else:
#     print("list is not equals")

List1 = ['a','b','c']
List2 = ['a','b','c']

if List1 == List2:
    print("List are equals")
else:
    print("list is not equals")







