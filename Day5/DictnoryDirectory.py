# Dictonary is  a collection which is unordered changeble (mutable)  and index in python dictonary are
# Written curly brase  and they have key and value

#Create dictnory
# mydic = {101:'x', 102:'y', 103:3}
#print(mydic) #{101:'x', 102:'y', 103:3}
# mydic = {101:'x', 102:'y', 103:'z'}
# print(mydic) #{101:'x', 102:'y', 103:'z'}

# Example 2 Access item from dictonary usin get function
# mydic = {
#     "brand": "Hundai",
#     "model": "i10",
#     "year": 2033
# }
# print(mydic['brand']) #Hundai
# # mydic(['model'])
# # print(mydic)#TypeError: 'dict' object is not callable
# print(mydic['model']) #i10
#
# x = mydic.get('brand')
# print(x)#Hundai

# Example 3 chanhe values of in dictonary
# mydic = {
#     "brand": "Hundai",
#     "model": "i10",
#     "year": 2023
# }
# print(mydic) #{'brand': 'Hundai', 'model': 'i10', 'year': 2023} old value
# mydic['year'] = 2021
# print(mydic)#{'brand': 'Hundai', 'model': 'i10', 'year': 2021} new value

#Example 4 reading from dictnory using loop

# mydic = {
#     "brand": "Hyundai",
#     "model": "i10",
#     "year": 2023
# }
#
# # for i in mydic:
# #     print(i) # it will return keys from dictionary
# #
# # print()
# # for i in mydic:
# #     print(mydic[i]) # it will print only values
#
# # for i in mydic.values():
# #     print(i)
# # print()
# # for i in mydic.keys():
# #     print(i)
#
# # IN MY REQUIREMENT PRINT COMBINATION OF X AND Y VALUES
#
# for x,y in mydic.items():
#     print(x,y)

# Example 5 check keys is exiting dictionary are not
# mydic = {
#     "brand": "Hyundai",
#     "model": "i10",
#     "year": 2023
# }

# if "brand" in mydic :
#     print("Exit in distortion")
# else:
#     print("not exit in dictionary")

#print("model" in mydic) #true

# Example 6 find no of item in dictionary len()

# mydic = {
#     "brand": "Hyundai",
#     "model": "i10",
#     "year": 2023
# }

#print(len(mydic)) #3

#Example 7 Adding item to dictionary

# mydic = {
#     "brand": "Hyundai",
#     "model": "i10",
#     "year": 2023
# }
# print(mydic) #{'brand': 'Hyundai', 'model': 'i10', 'year': 2023}
# mydic['color'] = 'Red'
# print(mydic) #{'brand': 'Hyundai', 'model': 'i10', 'year': 2023, 'color': 'Red'}

#Exaple 8 Removie Item for dictinory #pop()

# mydic = {
#     "brand": "Hyundai",
#     "model": "i10",
#     "year": 2023
# }

# mydic.pop('year')
# print(
# mydic)#{'brand': 'Hyundai', 'model': 'i10'}

# del mydic['year']
# print(mydic)#{'brand': 'Hyundai', 'model': 'i10'}

# del mydic
# print(mydic) #NameError: name 'mydic' is not defined

#Example 9 clear item for dictionary

# mydic = {
#     "brand": "Hyundai",
#     "model": "i10",
#     "year": 2023
# }
#
# mydic.clear()
# print(mydic) #{}

# Example 10 copy for the dictionary

mydic = {
    "brand": "Hyundai",
    "model": "i10",
    "year": 2023
}

# mydic1 = mydic
# print(mydic1) #{'brand': 'Hyundai', 'model': 'i10', 'year': 2023}

mydic1 = mydic.copy()
print(mydic1) #{'brand': 'Hyundai', 'model': 'i10', 'year': 2023}