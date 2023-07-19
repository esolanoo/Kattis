attempts = {}
score = 0
while True:
    s = input()
    if s == '-1':
        print(([attempts[i][1]==1 for i in attempts.keys()].count(True)), score)
        break
    else:
        m, test, res = [x for x in s.split()]
        if not(test in attempts):
            attempts[test] = [0,0]
        if attempts[test][1] == 0:
            if res == 'wrong':
                attempts[test][0] += 1
            elif res == 'right':
                attempts[test][1] = 1
                score += attempts[test][0]*20 + int(m)