str = "this is a test string!!"  # THIS si A tset STRING!!
a = str.split(" ")
rev = ''
for i in range(len(a)):
    print(i)
    word = a[i]
    if i % 2 == 0:
        rev = rev + word.upper()+' '
    else:
        rev = rev+word[-1::-1]
    rev = rev + " "
print(rev)