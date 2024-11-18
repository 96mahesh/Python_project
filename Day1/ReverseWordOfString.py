str = 'welcome to python programming'

word = str.split(" ")
print(word) #['welcome', 'to', 'python', 'programming']
words = word[-1::-1]
print(words) #['programming', 'python', 'to', 'welcome']

outputString = ' '.join(words)
print(outputString)##programming python to welcome

print()

str = 'welcome'
for i in range(len(str)-1,-1,-1):
    print(str[i],end="")

print()
str = 'welcome to java'
a = str[-1::-1]
print(a)


S = 'MAHESH BABU RAMPATRUNI'
S1 = ""
l = len(S)-1
while l >= 0:
    S1 = S1 + S[l]
    l = l-1

print(S1)
