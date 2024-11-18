str1 = "hi mahesh"
str2 = "mahesh"

a = str1.split(" ")
b = str2.split(" ")
word = ""

for i in a:
    for j in b:
        if not (i == j):
            word = i;
print(word)
