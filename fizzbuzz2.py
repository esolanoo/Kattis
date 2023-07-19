x, n = [int(w) for w in input().split()]
s = list()
for i in range(n):
    if (i+1)%3==0 and (i+1)%5==0: s.append("fizzbuzz")
    elif (i+1)%3==0: s.append("fizz")
    elif (i+1)%5==0: s.append("buzz")
    else: s.append(str(i+1))
aux = list()
for i in range(x):
    a = input().split()
    aux.append(([s[idx]==a[idx] for idx in range(n)].count(True), a))
print(aux.index(sorted(aux, key = lambda x: x[0], reverse = True)[0])+1)