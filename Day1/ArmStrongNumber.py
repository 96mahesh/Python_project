n = 153
rev = 0
temp = n
while (n>0):

    rem = n % 10;
    rev = rev + rem * rem * rem;
    n = n / 10;
    

print(n)
if temp==n:
    print("This no is armStrong number")
else:
    print("This no is not a armStrong number")