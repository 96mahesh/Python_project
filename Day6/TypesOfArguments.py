# Example 1

# def fun(i,j) :
#     print(i,j)
# fun(10,20) #Positional Arguments
# fun(j=20,i=10) # Keyword Arguments in this orguments change the position

#
# Example 2 #default value Assigned the positional arguments

# def cool(i,j=20):
#     print(i,j)
# cool(100,200) # By default value replaced the position value out put like come like this 100,200
# cool(100) # 100,20


# Example 4 Keyword Arguments

# def greeting(name,greetmsg) :
#     print(greetmsg+" "+name)
# greeting('mahesh','hello')
# greeting('hello','mahesh')

# Example 5

# def my_fun(a,b,c) :  #Positional parameters
#     print(a,b,c)
#
# my_fun(10,20,30)
# my_fun(a=10,b=20,c=30) #Keyword parameters
# my_fun(b=20,a=10,c=30) #Keyword parameters
# my_fun(10,20,c=30) # Combination Of position and keyword parameters
# my_fun(10,b=20,c=30) #This is having a logical error
# my_fun(10,30,b=20)
#my_fun(10,b=20,30) # This is incorrect statemnet positional argument must appear before any keyword argument

# Example 6 function can return multipple values
def largest(a,b):
    if a>b:
        return a,b
    else :
        return b,a

x = largest(100,200)
print(x)
print(largest(20,10)) # if anyn function contain multiple value that funcion come out put is tuple collection

print(type(x))


