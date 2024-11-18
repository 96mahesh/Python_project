# create String variable

# Example 1  ways of creating String variables
# s = 'mahesh'
# s = "mahesh"
# s = str('mahesh')
# s = str("mahesh")


#Example 2 Creating Empty String variables

name = ""
name=''
name = str()

# Example 3 Mutable - can change value of the varible
#Immutable - can not change value of the variable
#String is immutable

#str = 'mahesh'
#print(id(str)) #2366468242528

#str = str+'babu'
#print(id(str)) #2366471158448##
#print(str)

#example 4 + and * Operations of String
# * operator will perfrom in syrings print value mutltiple times
# str = 'welcome'
# str2 = 'python'
# print(str+str2) #welcome Python
#
# print(str*3)#welcomewelcomewelcome

#Example 4 Slicing []
#start index = 0
#Ending index = 1

# str = 'welcome'
# print(str[1:3]) #ah
# print(str[:6]) #welcom
# print(str[2:]) #lcome

# str = 'mahesh'
# print(str[1:-1]) #ahes

#Example 6 ord () and char ()
# print(ord('A')) #65
# print(ord('a')) #97
#
# print(chr(98)) #b
# print(chr(65)) #A

#Exmaple 7 max() min () len()
# print(max("abc"))#c
# print(min("abc"))#a
# print(len("abc"))#3

#Exmaple 8 in and not in operator

# s = 'mahesh'
# print('hesh' in s) #True
# print('hesh' not in s) #false
#
# print('come' in s) #false
# print('come' not in s)#true

#Example 8 compare Strings

# print('tim'=='tie') #flase
# print('free' != 'freedom') #true
# print('arrow' > 'aron') #true
# print('right'>='left')#true
# print('teeth'<'tee')#false
# print('yellow'<= 'fellow')#false
# print('abc'>' ')#true

#Exapmle 8 Testing String true false

# s = 'welcmoe to python'
# print(s.isalnum()) #flase
# print('welcom'.isalpha()) #true
# print('1996'.isdigit())#true
# print('frist number'.isidentifier())#false
# print(s.islower()) #true
# print("WELCOME".isupper()) #true
# print(" ".isspace())

#Example 9 searching for subString

# s = 'welcome to python'
# print(s.endswith('thon')) #true
# print(s.startswith('good')) #false
# print(s.find('come')) #3
# print(s.find('become'))#-1
# print(s.count('o')) #3

#Example 10 convert String
s = 'string in python'
print(s.capitalize()) #String in python
print(s.title()) #String In Python
print(s.islower()) #true
print(s.upper()) #STRING IN PYTHON
print(s.swapcase())#STRING IN PYTHON swap upper to lower lower to upper
print(s.replace('in' , 'on'))