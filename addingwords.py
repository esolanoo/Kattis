from sys import stdin
d = {}
for line in stdin:
    w = line.split()
    if w[0] == 'clear':
        d = {}
    elif w[0] == 'def':
        d[w[1]] = w[2]
    elif w[0] == 'calc':
        s = ''
        s = w[1::]
        print(' '.join(s), end=' ')
        s = [i if (i == '+' or i == '-') else d[i] if i in d else 'unknown' for i in s[:-1]]
        if 'unknown' in s:
            print('unknown')
        else:
            x = str(eval(' '.join(s)))
            if x in list(d.values()):
                print(list(d.keys())[list(d.values()).index(x)])
            else:
                print('unknown')