from math import ceil

x = int(input())
i = 0
m = x
while (x/2**i)+i<=x:
    if (x/2**i)+i < m:
        m = (x/2**i)+i
    i += 1
print(int(ceil(m)))