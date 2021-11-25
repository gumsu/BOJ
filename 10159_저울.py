n = int(input())
m = int(input())
graph = [[1e9]*n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a][b] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j :
                graph[i][j] = 0
            elif graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1
# for z in graph:
#     print(z)

cnt = [0]*n
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1e9 and graph[j][i] == 1e9:
            cnt[i] += 1
for i in cnt:
    print(i)