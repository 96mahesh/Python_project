s = "listen"
ss = "silent"

count = 0
for i in range(len(s)):
    val = s[i]
    for j in range(len(ss)):
        if s[i] == ss[j]:
            count += 1
print(count)
print(len(s))
if count == len(s):
    print("given words are anagram")
else:
    print("not anagram")
