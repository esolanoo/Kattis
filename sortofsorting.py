def sort_sort(a):
    data = [input() for _ in range(a)]
    data.sort(key=lambda x: x[:2])
    print()
    for item in data: print(item)

while True:
    n = int(input())
    if n == 0: 
        break
    sort_sort(n)