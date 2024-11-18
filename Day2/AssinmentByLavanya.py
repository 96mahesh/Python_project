str1 = "hi mahesh"
str2 = "mahesh"

a = str1.split(" ")
b = str2.split(" ")
word = "";
for i in range(len(a)):
    for j in range(len(b)):
        if not (a[i] == b[j]):
            word = a[i]

print(word)
