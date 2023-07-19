aux = input().split()
n, s, m = int(aux[0]), int(aux[1]), int(aux[2])
board = [int(x) for x in input().split()]
h = 0
aux.clear()
while True:
    if s > n:
        print('right')
        break
    elif s < 1:
        print('left')
        break
    elif board[s-1] == m:
        print('magic')
        break
    elif s in aux:
        print('cycle')
        break
    else:    
        aux.append(s)
        h += 1
        s += board[s-1]
print(h)
