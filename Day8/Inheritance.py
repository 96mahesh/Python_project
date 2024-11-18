# Example 1 Single level Inheritance  One parent one child class

# class A :
#     def m1(self):
#         print("This is m1 method from a class")
#
# class B(A) :
#     def m2(self):
#         print("This is m1 method from class b")
#
# # a = A();
# # a.m1()
# # b = B()
# # b.m2()
# obj = B()
# obj.m1() # this satement is comming from class A
# obj.m2() # this satement is comming from class B


# Example 2 Single level Inheritance  One parent one child class

# class A:
#     x,y = 10,20
#     def m1(self):
#         print(self.x + self.y)
#
# class B(A):
#     a,b = 100,200
#     def m2(self):
#         print(self.a + self.b)
# obj = B()
# obj.m1()
# obj.m2()

# #Example 3 Single level Inheritance  One parent one child class
#
# class A:
#     x,y = 10,20
#     def m1(self,m,n):
#         print(self.x + self.y)
#         print(m*n)
#
# class B(A):
#     a,b = 100,200
#     def m2(self,c,d):
#         print(self.a + self.b)
#         print(c*d)
# obj = B()
# obj.m1(25,25) # 625
# obj.m2(5,5) # 25

#Example 4 Single level Inheritance  One parent one child class

# P , Q = 1000 , 2000
# class A:
#     x,y = 10,20
#     def m1(self,m,n):
#         print(self.x + self.y)
#         print(m*n)
#         print(globals()['P']+globals()['Q']) # 3000
#
# class B(A):
#     a,b = 100,200
#     def m2(self,c,d):
#         print(self.a + self.b)
#         print(c*d)
#         print(globals()['P'] + globals()['Q'])# 3000
# obj = B()
# obj.m1(25,25) # 625
# obj.m2(5,5) # 25


# Example 5 Multi level inheritance one parent multiple children inosence grand father

# class A :
#     x,y = 10,20
#     def m1(self):
#         print(self.x + self.y)
#
# class B(A):
#     i,j = 30 , 40
#     def m2(self):
#         print(self.i + self.j)
#
# class C(B):
#     m,n  = 50,60
#     def m3(self):
#         print(self.m * self.n)
#
# obj = C()
# obj.m1() # 30
# obj.m2() # 70
# obj.m3() # 3000


# # Example 6 hierarchy inheritance one parent two children inosence grand father
#
# class A :
#     x,y = 10,20
#     def m1(self):
#         print(self.x + self.y)
#
# class B(A):
#     i,j = 30 , 40
#     def m2(self):
#         print(self.i + self.j)
#
# class C(A):
#     m,n  = 50,60
#     def m3(self):
#         print(self.m * self.n)
#
# # create c class object
# obj = C()
# obj.m1() # 30
# obj.m3() # 3000
#
# # create b class object
#
# pobj = B()
# pobj.m1() # 30
# pobj.m2() # 70


# # Example 7 multiple  inheritance Two parent two children
#
# class A :
#     x,y = 10,20
#     def m1(self):
#         print(self.x + self.y)
#
# class B:
#     i,j = 30 , 40
#     def m2(self):
#         print(self.i + self.j)
#
# class C(A,B):
#     m,n  = 50,60
#     def m3(self):
#         print(self.m * self.n)
#
# # create c class object
# obj = C()
# obj.m1() # 30
# obj.m3() # 3000
# obj.m2() # 70


#EXample 8  over raiding method
# class A:
#     def m1(self):
#         print("this is m1 method for class A")
#
# class B(A):
#     def m1(self):
#         print("this is m1 method for class B")
#         super().m1() # to invoke the parrent class method through chaild class
#
# obj = B() #this is m1 method for class B
# obj.m1()


#Example 9

# class A:
#     a,b = 10,20
#
# class B(A):
#     i,j = 100,200
#     def m(self,x,y):
#         print(x+y)
#         print(self.i+self.j) # 300
#         print(self.a+self.b) # 30
#
# obj = B()
#obj.m(1000,2000) # 3000

# Example 10 Over ride methodes
# class parrent :
#     name = 'Mahesh'
#
# class chaild:
#     name = "Pawan" # Over raiding the variable
#
# obj = chaild()
# print(obj.name)

# # Example 11
#
# class parrent :
#     name = 'Mahesh'
#
# class chaild (parrent):
#     name = "Pawan" # Over raiding the variable
#     def test(self):
#         print(super().name)
#
# obj = chaild()
# print(obj.name) #Pawan
# obj.test() #Mahesh

# Example 12  Over raiding the methodes

class Bank:
    def rateOfInterest(self):
        return 0

class XBank(Bank):
    def rateOfInterest(self):
        return 10

class YBank(Bank):
    def rateOfInterest(self):
        return 12

objx = XBank()
x = objx.rateOfInterest()
print(x)

objy = YBank()
y =objy.rateOfInterest()
print(y)






