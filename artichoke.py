from math import cos, sin

p, a, b, c, d, n = [int(x) for x in input().split()]
data = [p * (sin(a*(k+1)+b) + cos(c*(k+1)+d) + 2) for k in range(n)]
diff = 0
aux = data[-1]
for i in range(1, n+1):
    if data[-i] < aux:
        aux = data[-i]
    else:
        x = data[-i] - aux
        diff = max(diff, x)
print(diff)