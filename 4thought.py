from math import floor

A = [" +", " -", " *", " //"]
aux = {}
for x in A:
    for y in A:
        for z in A:
            sen = '4 ' + str(x) + ' 4 ' + str(y) + ' 4 ' + str(z) + ' 4'
            n = floor(eval(sen))
            aux[n] = sen.replace(' //', ' /')
m = int(input())
for i in range(m):
    w = int(input())
    if -61<int(w)<257:
        try: print(aux[w] + ' = ' + str(w))
        except: print("no solution")
    else:
        print("no solution")
