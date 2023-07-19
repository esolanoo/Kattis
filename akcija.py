books = []
for i in range(int(input())):
    books.append(int(input()))

books.sort()
price = 0
n = len(books)-1
i = 1
while n-(3*i-1) >=0:
    books.pop(n-(3*i-1))
    i += 1
print(sum(books))