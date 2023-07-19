n = 0
for i in range(int(input())):
    s = input()
    n += int(s[:-1])**int(s[len(s)-1])
print(n)