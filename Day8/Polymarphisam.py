# Example 1 Overloading
# class Human :
#
#     def sayHello(self,name = None):
#         if name is not None:
#             print("Hello"+' '+name)
#         else:
#             print('Hello')
#
# h = Human();
# h.sayHello("mahesh")
# h.sayHello()

# Example 2

class calculation:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)

obj = calculation()
obj.add() #0
obj.add(10,20) #30
obj.add(100,200,300) #300