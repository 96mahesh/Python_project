name = "Earth is the third planet from the sun and the only astronomical object known to harbour and support life."

odd_index = []

for i in range(0, len(name)):
    if i % 2 == 1:
        odd_index.append(name[i])

print(odd_index)
