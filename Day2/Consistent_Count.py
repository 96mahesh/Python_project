s = "abcabbbccaabd"
t = ""
count = 1
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        count = count + 1
    else:
        t += s[i] + str(count)
        count = 1
t += s[-1] + str(count)
print(t)
