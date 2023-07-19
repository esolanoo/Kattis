from sys import stdin
for line in stdin:
    w = line.split()
    print(abs(int(w[1])-int(w[0])))