# set is a collection which is unordered ans unexisted. in python set are written with curlu brase {}
# set is a mutable
#Example 1 create a set
# Myset = {'apple','banana','cherry'}
# print(Myset)# {'banana', 'cherry', 'apple'}

# Example 2 Assinding item for set
# Myset = {'apple','banana','cherry'}
# for i in Myset:
#     print(i)

#Example 3 Value is esit set are not
# Myset = {'apple','banana','cherry'}
# print("banana" in Myset) #true
# print("banana1" in Myset) #false

#Example 4 Add Item in the set / Methods Add() update() in this update add multiple items
# Myset = {'apple','banana','cherry'}
# #Myset.add("orange")
# Myset.update(["orange" , 'grapes'])
# print(Myset)

#Example 5Find no of item in a set
# Myset = {'apple','banana','cherry'}
# print(len(Myset)) #3

#Example 6 removie item from the set removie() Discard()
# Myset = {'apple','banana','cherry'}
# #Myset.remove("apple")
# #print(Myset) #{'banana', 'cherry'}
# #Myset.remove("xyz")
# #print(Myset) #KeyError: 'xyz'
# # Myset.discard("apple")
# # print(Myset)##{'banana', 'cherry'}
# Myset.discard("xyz")
# print(Myset)# Will not thow any erroe


#Exapmle 7 clear all item for set

# Myset = {'apple','banana','cherry'}
# # Myset.clear()
# # print(Myset) #set()
#
# del(Myset)
# print(Myset) #NameError: name 'Myset' is not defined

#Example 8 join / combain set
# Here not sopported to coccatenation operation
# Using union operation

Myset = {'apple','banana','cherry'}
Myset1 = {"kiwi",'grapes','suppota'}
# Myset3 = Myset.union(Myset1)
# print(Myset3) #{'banana', 'grapes', 'apple', 'cherry', 'suppota', 'kiwi'}
Myset3 = Myset.update(Myset1)
#print(Myset3) #none
print(Myset) #{'suppota', 'grapes', 'banana', 'kiwi', 'apple', 'cherry'}