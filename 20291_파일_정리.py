n = int(input())
ext = dict()
for i in range(n):
    a, b = input().split('.')
    if b not in ext:
        ext[b] = 1
    else:
        ext[b] += 1
ext = dict(sorted(ext.items(), key=lambda x: x[0]))
for i, j in ext.items():
    print(i, j)