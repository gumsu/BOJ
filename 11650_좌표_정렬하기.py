n = int(input())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x,y))

arr.sort(key=lambda x: (x[0], x[1]))
for a, b in arr:
    print(a, b)