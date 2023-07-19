a = input().split()
n, k = int(a[0]), int(a[1])
x = input().split()
print(' '.join([x[k*i-1] for i in range(1, int(n/k+1))]))