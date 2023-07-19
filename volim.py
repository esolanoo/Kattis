b = int(input())
q = int(input())
t = 0
for i in range(q):
    d = input().split()
    t += int(d[0])
    if d[1] == "T" and t<60*3.5:
        if b == 8: b = 1
        else: b += 1
print(b)