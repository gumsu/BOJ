n = int(input())
arr = [(input()) for _ in range(n)]
books = dict()
for i in arr:
    if i not in books:
        books[i] = 1
    else:
        books[i] += 1
best = max(books.values())
bestseller = []
for book, count in books.items():
    if count == best:
        bestseller.append(book)
bestseller.sort()
print(bestseller[0])