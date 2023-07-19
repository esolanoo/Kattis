sum = lambda a: 'correct!' if a[0] + a[1] == a[2] else 'wrong!'
print(sum([int(x) for x in input().split()]))