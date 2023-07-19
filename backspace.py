s = input()
new_s = []

for char in s:
    if char == '<':
        if new_s:
            new_s.pop()
    else:
        new_s.append(char)

result = ''.join(new_s)
print(result)