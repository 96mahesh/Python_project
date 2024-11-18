# str = input("please enter a string : ")
# ch = input("please enter a character : ")
# print(str.replace(ch, ""))

s = "Quescol"
s1 = "e"
for i in s:
    for j in s1:
        if i == j:
            i = ""

    print(i,end="")
