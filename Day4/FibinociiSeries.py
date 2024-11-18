x,y=0,1
sum=0
n=int(input("enter n:"))
if n<=0:
    print("enter valid n")
elif n==1:
    print(x)
elif n>2:
    print(0)
    for i in range(n):
        x=y
        y=sum
        sum=x+y
        print(sum)
