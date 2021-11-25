n, m = map(int, input().split())

graph = [[1e9]*n for _ in range(n)]

# b가 0 -> 일방통행, 1 -> 양방향
# 비용 그래프
for _ in range(m):
    u, v, b = map(int, input().split())
    u -= 1
    v -= 1

    # u -> v 는 무조건 갈 수 있음 비용 0
    # 일방통행 비용 1 양방향통행 비용 0
    graph[u][v] = 0
    graph[v][u] = 1 if b == 0 else 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j :
                 graph[i][j] = 0
            elif graph[i][j] > graph[i][k] + graph[k][j]:
                 graph[i][j] = graph[i][k] + graph[k][j]
# for z in graph:
#     print(z)

k = int(input())

for _ in range(k):
    s, e = map(int, input().split())
    s -= 1
    e -= 1
    if graph[s][e] == 1e9 or graph[s][e] == 0:
        print(0)
    else:
        print(graph[s][e])