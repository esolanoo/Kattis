n, q = [int(x) for x in input().split()]
d = {}
aux = 0
for i in range(q):
    s = input().split()
    if s[0] == "SET": d[int(s[1])] = int(s[2])
    elif s[0] == "PRINT": 
        if int(s[1]) in d: print(d[int(s[1])])
        else: print(aux)
    else:
        aux = int(s[1])
        d = {}