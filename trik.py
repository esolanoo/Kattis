def change(arr, a, b):
    aux = arr[b]
    arr[b] = arr[a]
    arr[a]= aux
    
cups = [1, 0, 0]
instructions = [letter for letter in input()]
for letter in instructions:
    x = 0
    y = 1
    if letter == 'B':
        x = 1
        y = 2
    if letter == 'C':
        y = 2
    change(cups, x, y)

print(cups.index(1)+1)
    