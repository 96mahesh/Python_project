name = ["John", "Remo", "Mixy", "Julie", "Ronny"]

temp = " "
print("Before shorting array")
for i in range(len(name)):
    print(name[i], end=" ")

for i in range(len(name) - 1):
    for j in range(i+1, len(name)):
        if name[i] > name[j]:
            temp = name[i]
            name[i] = name[j]
            name[j] = temp;

print()
print("After shorting array")
for i in range(len(name)):
    print(name[i], end=" ")