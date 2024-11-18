name = ["python","JavaScript","Java","SpringBoot"]
print(max(name,key=len))

maxStr = ""

for item in name:
    if len(item) > len(maxStr):
        maxStr = item


print(maxStr)

