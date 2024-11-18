# def example_function(*args):
#     for arg in args:
#         print(arg)
#
#
# example_function(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def myFun(arg, *argv):
    print("First argument :", arg)
    for arg in argv:
        print("Next argument through *argv :", arg)



myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
