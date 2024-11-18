# 5 = 1*2*3*4*5 = 120

n = 5
fact = 1

if n<0:
    print("The number doesn't nagitive number")
elif n==0:
    print('The number factorial is 1')
else:
    for i in range(1,n+1):
        fact = fact*i
print("factorial of ",n, 'is', fact)