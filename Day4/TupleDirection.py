# Example 1 create a Tuple

# Mytuple = ('apple','banana','cherry')
# #print(Mytuple)
# Mytuple= () #Empty Tuple
# print(Mytuple)

# Example Access Tuple item

# Mytuple = ('apple','banana','cherry')
# print(Mytuple[1]) # banana
# print(Mytuple[-1]) # cherry

#Example 3 Range Of Index

# Mytuple = ('apple','banana','cherry','orange','melon','kiwi','mango')
# print(Mytuple[3:5]) #[''orange','melon']
# print(Mytuple[2:6]) #['cherry','orange','melon','kiwi']
# print(Mytuple[-4:-1]) #['orange','melon','kiwi']

#Example 4 changing  tupple item

# Mytuple = ('apple','banana','cherry')
# myList = list(Mytuple)
# myList[0] = "orange"
# Mytuple = tuple(myList)
# print(Mytuple) #('orange','banana','cherry')

#Example 5 Reading tuple item using loop

# Mytuple = ('apple','banana','cherry')
# for i in Mytuple :
#     print(i)

#Example 6 Check item exists

# Mytuple = ('apple','banana','cherry')
# if 'apple' in Mytuple :
#     print("yes Apple is present")
# else :
#     print("no Apple is Present")

# Example 7 Item Length count items in a tuple

# Mytuple = ('apple','banana','cherry')
# print(len(Mytuple)) #3

#  Example 8 Add items to tuple - not possible becouse touple is Immutable- cnanot change Values/items
# Mytuple = ('apple','banana','cherry')
# Mytuple[0] = "orange";
# print(Mytuple)  #TypeError: 'tuple' object does not support item assignment

# Example 9 Copy Tuple
# Mytuple = ('apple','banana','cherry')
# Mytuple1 = Mytuple
# print(Mytuple1) #('apple', 'banana', 'cherry')

#Example 10 From the tuple not posible - becouse of tupple is immutable

# Mytuple = ('apple','banana','cherry')
# #Mytuple.removie('apple') #invalid / it is not posible
# del Mytuple
# print(Mytuple)#name 'Mytuple' is not defined. Did you mean: 'tuple'? it s already Deleted


# Example 11 Join are combine tuple
# Mytuple = (10,30,50)
# Mytuple1 = (20,40,60)
# Mytuple2 = Mytuple+Mytuple1;
# print(Mytuple2)

# Example 12 Compare tuple Equal are not

# Mytuple = (10,30,50)
# Mytuple1 = (20,40,60)
# if Mytuple1==Mytuple1 :
#     print("My tupes are equal")
# else :
#     print("My tuple is not eqauals")

Mytuple = (10,30,50)
Mytuple1 = ('a','b','c')
if Mytuple==Mytuple1:
    print("My tupes are equal")
else :
    print("My tuple is not eqauals")






