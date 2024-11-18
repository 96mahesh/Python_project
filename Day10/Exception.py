# Example 1

# print("This is Starting point of Program")
# print("This is Starting point of Program")
# print("This is Starting point of Program")
#
# try:
#     print(x)
# except:
#     print("Exception Occure")
#
#
# print("This is Ending point of Program")
# print("This is Ending point of Program")
# print("This is Ending point of Program")

# Example 2


# print("This is Starting point of Program")
# print("programing process")
# print(10/2)
# print("Program is Completed")

# # Example 3
#
# print("This is Starting point of Program")
# print("programing process")
# try :
#     print(10/0)
# except:
#     print("ZeroDivisionError: division by zero")
# print("Program is Completed")


# Example 4

# print("This is Starting point of Program")
# print("programing process")
# try :
#     print(10/0)
# except ZeroDivisionError:
#     print("Exception Occured and handled")
#print("Program is Completed")

# Example 5 multiple Expect blocks try , expect ,else , finally

# try :
#     a , b = 10,5
#     res = a/b
#     print("result is :", res)
# except ZeroDivisionError:
#     print("thrown zero divisible Exception")
# except SyntaxError :
#     print("thrown SystexError")
# except :
#     print("Excption Handling")
# else : # it will executed no exception
#      print("Exception not occured")
# finally: # Exception is occure not occure Doesn't matter finally back always heare
#     print("always execute .....")


# Example 6 multiple Expect blocks try , expect ,else , finally

# try :
#     a , b = 10,0
#     res = a/b
#     print("result is :", res)
# except ZeroDivisionError:
#     print("thrown zero divisible Exception")
# except SyntaxError :
#     print("thrown SystexError")
# except :
#     print("Excption Handling")
# else : # it will executed no exception
#      print("Exception not occured")
# finally: # Exception is occure not occure Doesn't matter finally back always heare
#     print("always execute .....")

# Example 7 Faising our own Exception

# def enterAge(n) :
#     if(n<0) :
#         raise ValueError("Only Integers are allowed")
#     if n%2==0 :
#         print("Even Number")
#     else :
#         print("Odd Numberr")
#
# enterAge(10)
# enterAge(5)
# enterAge(-1)

# Example 8

def enterAge(n) :
    if(n<0) :
        raise ValueError("Only Integers are allowed")
    if n%2==0 :
        print("Even Number")
    else :
        print("Odd Number")

print("Checking number is Even or odd by calling Function...")
n = -1
try :
    enterAge(n)
except ValueError:
    print(" value error Exception occure")
print("program completed")

