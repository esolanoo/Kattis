import sys

def fun(x, y):
    numbers = []
    for _ in range(x):
        numbers.append(int(sys.stdin.readline()))
    for _ in range(y):
        numbers.append(int(sys.stdin.readline()))
    print(x + y - len(set(numbers)))

while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0:
        break
    elif a == 0 or b == 0:
        print(0)
    else:
        fun(a, b)