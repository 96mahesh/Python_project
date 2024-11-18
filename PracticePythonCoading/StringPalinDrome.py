num = 1005
val = str(num)
res = val[::-1]
if res == num:
    print("palindrome")
else:
    print("not palindrome")


n = "mam"
v = str(n)
if v == v[::-1]:
    print("palindrome")

else:
    print("not palindrome")

str = 'mahesh'
r = ''
l = len(str)-1
while l >= 0:
    r = r + str[l];
    l = l - 1
print(r)
if res == str:
    print("palindrome")
else:
    print("not palindrome")