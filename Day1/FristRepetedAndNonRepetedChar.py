a = "python is super"

fristrepetedchar = ''
fristnonrepetedchar = ''

for i in range(len(a)):
    for j in range(len(a)):
        if a[i] == a[j]:
            if fristrepetedchar == '':
                fristrepetedchar = a[i]
            elif fristnonrepetedchar == '':
                fristnonrepetedchar = a[i]

print(fristrepetedchar)
print(fristnonrepetedchar)