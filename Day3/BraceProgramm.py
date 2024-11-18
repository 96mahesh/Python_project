name = "{{{{}}"
print("before removing duplicates", name)
output = " "
for i in name:
    if i not in output:
        output = output + i
print(output)
l = len(name)
l = l // 2
for i in output:
    print(i * l, end=" ")
