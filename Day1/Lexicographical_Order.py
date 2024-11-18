name = ["John", "Remo", "Mixy", "Julie", "Ronny"]

print("Before Sorting")
for i in range(len(name)):
    print(name[i])

for i in range(len(name)-1):
    for j in range(i + 1, len(name)):
        if name[i] > name[j]:
            temp = name[i]
            name[i] = name[j]
            name[j] = temp

print("\nAfter performing lexicographical order: ")
for i in range(len(name)):
    print(name[i])

