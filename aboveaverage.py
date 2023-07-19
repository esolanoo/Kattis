for i in range(int(input())):
    x = [int(x) for x in input().split()]
    avr = sum(x[1::])/x[0]
    a = float(100*[s>avr for s in x][1::].count(True)/x[0])
    print('{0:.3f}%'.format(a))