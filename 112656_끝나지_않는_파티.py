n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j :
                graph[i][j] = 0
            elif graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
# a 파티장에서 b 파티장으로 가려고 함, 다음 파티시간은 c
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1

    if graph[a][b] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")

# for z in graph:
#     print(z)