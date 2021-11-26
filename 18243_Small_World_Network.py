n, k = map(int, input().split())

graph = [[1e9]*n for _ in range(n)]

for _ in range(k):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a][b] = graph[b][a] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = 0
            elif graph[i][j] > graph[i][k] + graph[k][j] :
                graph[i][j] = graph[i][k] + graph[k][j]

# for z in graph:
#     print(z)
flag = False
for i in range(n):
    for j in range(n):
        if graph[i][j] > 6:
            print("Big World!")
            flag = True
            break
    if flag:
        break
else:
    print("Small World!")