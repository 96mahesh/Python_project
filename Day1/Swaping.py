## Approch 1

x ,y = 100,200
print('before swaping values',x,y)
c = x
x = y
y = c
print("afetr swaping values",x,y)

## Approch 2

x , y = 100 , 200
print()
print('before swaping value ', x,y)
x,y=y,x
print('After swaping value ', x,y)

## Approch 3

x , y =  100 , 200
print()
print('before swaping value ', x,y)
x = x + y
y = x - y
x = x - y
print('After swaping value ', x,y)