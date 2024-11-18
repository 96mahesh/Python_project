name = "Please like & subscribe for more coding videos"

a = name.split(" ");
res = []
print(type(res))
for i in a:
    if len(i) > 4:
        res.append(i)
print(res)