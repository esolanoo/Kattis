n = int(input().split()[1])
problems = [int(x) for x in input().split()]
problems.sort()

for i in range(n):
    T, D = [int(x) for x in input().split()]
    if T == 1: aux = [x>D for x in problems]
    else: 
        aux = [x<=D for x in problems]
    if not(True in aux):
        print(-1)
    else:
        if T == 2: 
            problems.reverse()
            aux.reverse()
        print(problems[aux.index(True)])
        problems.pop(aux.index(True))
        if T == 2:
            problems.reverse()
            aux.reverse()
