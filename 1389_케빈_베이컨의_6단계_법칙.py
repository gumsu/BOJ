n, m = map(int, input().split())

arr = [[1e9]*n for _ in range(n)]
kevin = [0]*n

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    arr[a][b] = arr[b][a] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j :
                arr[i][j] = 0
            elif arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

for i in range(n):
    for j in range(n):
        kevin[i] += arr[i][j]

print(kevin.index(min(kevin))+1)
#print(min(kevin))