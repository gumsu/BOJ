n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]
distance = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
    distance[a][b] = b
    distance[b][a] = a

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
                distance[a][b] = distance[a][k]

for a in range(1, n+1):
    for b in range(1, n+1):
        if distance[a][b] == INF:
            print('-', end=' ')
        else:
            print(distance[a][b], end=' ')
    print()

# for z in graph:
#     print(z)