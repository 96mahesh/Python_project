# #Example 1
# class Myclass:
#     def myfun(self):
#         pass
#     def display(self):
#         print("mahesh")
# #create calss boject
# #Myclass()
# m = Myclass()
# m.myfun()
# m.display()

#Example 2
# class Myclass:
#     def myfun(self):
#         pass
#     def display(self,name):
#         print(name)
# m = Myclass()
# m.myfun()
# m.display("mahesh")

# #Example 3  create instance method with create object
#
# class Myclass:
#     def m1(self):
#         print("this insatnce method")
#     @staticmethod
#     def m2(num):
#         print(num)
# #Myclass().m1()
# m = Myclass()
# m.m1()
# m.m2(100)

#Example 4  create instance method with create object

# class Myclass:
#     def m1(self): #Here self is a keyword it will refering to tha class
#         print("this insatnce method")
#     @staticmethod
#     def m2(self ,num): #Here self is a keyword it will refering the parameter
#         print(self ,num)
# #Myclass().m1()
# m = Myclass()
# m.m1()
# m.m2(100,200) #100 200
# Myclass().m2(10,20) #10 , 20

# Example 5 declaired the varibles

# class Myclass:
#     a,b = 10,20; # class variale this variables is access the insaid methos using self keyword
#     def add(self):
#         print(self.a + self.b)
#     def mul(self):
#         print(self.a * self.b)
#     def sub(self):
#         print(self.a - self.b)
#
# mc = Myclass()
# mc.add() #30
# mc.sub() # -10
# mc.mul() # 200

# #Example 6 combination of loacal , global and class variable name is different
# i,j = 15,25 # global variable
#
# class Myclass:
#     a,b = 10,20 # a ,b class variable
#     def add(self, x,y):
#         print(x+y) # x , y local variable # 300
#         print(self.a + self.b) # a ,b class variable # 30
#         print(i+j) # i ,j is global variable # 40
# Myclass().add(100 , 200)

#Example 7  combination of loacal , global and class variable name is same
a,b = 15,25 # global variable

# class Myclass:
#     a,b = 10,20 # a ,b class variable
#     def add(self, a,b):
#         print(a+b) # x , y local variable # 300
#         print(self.a + self.b) # It will threated is a class variable #30
#         print(globals()['a']+globals()['b']) # if we can access galobe variable when all variable name is same following syntax globlas()['a']+['b']
# Myclass().add(100 , 200)

# # Example 8 one single class have multiple objects
# class Myclass:
#     def diaplay(self,name):
#         print("display methods .....")
#         print(name)
#
# obj = Myclass()
# obj.diaplay("mahesh") #mahesh
#
# obj1 = Myclass()
# obj.diaplay("babu") # bubu

# Example 9 constructor example
# class Myclass:
#     def __init__(self):
#         print("this is constructor")
#     def m1(self):
#         print("hello")
#     def m2(self,x,y):
#         return (x+y)
# mc = Myclass() # in this statement invoke constrctor automatically
# mc.m1() # methos is called exiplicitly using object
# m = mc.m2(10,20)
# print(m)

# # Example 10 constructor with object parametor
#
# class Myclass:
#     name  = 'mahesh'
#     def __init__(self ,  name): # constructor excepting one argument
#         print(name)
#         print(self.name)
# mc = Myclass("pawan");  # passing parameter to the constractor

# Example 11
# Req emp class
# create one constructor with 3 objects eid , ename , sal
#Display() one method this method should print eid ename sal

# class emp:
#     eid = ""
#     ename = ""
#     sal = ""
#     def __init__(self,eid ,ename , sal):
#         self.eid =eid
#         self.ename = ename
#         self.sal = sal
#
#     def display(self):
#         print(self.eid,self.ename,self.sal)
# em = emp(101,"mahesh",50000)
# em.display(); #101 mahesh 50000
# el = emp(101,"Pawan",70000)
# el.display()

# # example 12 creater multiple constractor
#
# class emp:
#     eid = ""
#     ename = ""
#     sal = ""
#     def __init__(self,eid ,ename , sal):
#         self.eid =eid
#         self.ename = ename
#         self.sal = sal
#
#     def __str__(self): # this is one more type of constractor its return value it will invoke only string type data it will invoke autometically
#        return(self.ename)
#        # print(self.eid,self.ename,self.sal)
# em = emp(101,"mahesh",50000)

# print(em)

# example 13 known error purpose create multiple constractor

class emp:
    eid = ""
    ename = ""
    sal = ""
    def __init__(self,eid ,ename , sal):
        self.eid =eid
        self.ename = ename
        self.sal = sal

    def __str__(self): # this is one more type of constractor its return value it will invoke only string type data it will invoke autometically
       return(self.ename,self.sal)
       # print(self.eid,self.ename,self.sal)
em = emp(101,"mahesh",50000)
print(em)  #TypeError: __str__ returned non-string (type tuple) Because of it will take only String data
