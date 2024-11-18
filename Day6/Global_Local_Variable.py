# Eaxmple

# global_var = 20  # global variable
#
# def fun() :
#     local_var = 10 # # Local variable
#     print(local_var)
#     print(global_var)
#
# fun()
# print(global_var)

#Example 2

# xy = 200
#
# def fun() :
#
#     xy = 100
#     print(xy)
# fun() #100

# # Example 3
#
# xy = 100  # global Variable
#
# def cool() :
#     global xy
#     xy = 200 #global
#     print(xy) #200
# cool()
# print(xy) #200

# Example 4

# xy = 100  # global Variable
#
# def cool() :
#     global xy
#     xy = 500 #global
#     print(xy) #200
# #
#
#
# cool() # 500 if it is commented then print global varialble invokes automtically
# print(xy) #100

# Example 5

def cool():
    global x
    x = 100
    print(x)
cool() #100
print(100)