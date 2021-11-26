n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                visited[i][j] = 0
            elif graph[i][j] == 'Y' or (graph[i][k] == 'Y' and graph[k][j] == 'Y'):
                visited[i][j] = visited[j][i] = 1

res = 0
for i in range(n):
    res = max(res, sum(visited[i]))

print(res)