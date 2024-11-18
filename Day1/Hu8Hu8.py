name = "HH8gj87654bbvghuu8"
a = list(name)
sum1 = 0
for i in range(len(a)):
    if "0" < a[i] < "9":
       # print(a[i])
        #x = str(a[i])
        sum1 = sum1 + int(a[i])
print(sum1)