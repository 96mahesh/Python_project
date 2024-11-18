import calendar

my_list = [[1], [2, 3], [4, 5, 6, 7]]
res = []
for i in my_list:
    for j in i:
        res.append(j)
#print(res)

#### Callender###
year = 1989
month = 7

print(calendar.month(year,month))
