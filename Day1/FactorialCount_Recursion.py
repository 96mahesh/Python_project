def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1) # it will convert disending order
    ## 5 , (5-1)=4, (4-1)=3 , (3-1)=2 , (2-1)=1, (1-1) = 0 == 5*4*3*2*1 = 120

num = 5
factcount = factorial(num)
print("Factorial of ",num, 'is', factcount)

def factorial1(n):

    return 1 if(n==0 or n==1) else n * factorial(n-1)

num = 5
factcount1 = factorial1(num)
print("Factorial1 of ",num, 'is', factcount1)