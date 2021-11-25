n, k = map(int, input().split())

graph = [[1e9]*n for _ in range(n)]

# a -> b 순서로 사건이 일어났을 때 a가 b보다 먼저 일어남 -1
# b -> a 뒤에 사건이라면 1
for _ in range(k):
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

s = int(input())
for _ in range(s):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if graph[a][b] == 1:
        print(-1)
    elif graph[b][a] == 1:
        print(1)
    else:
        print(0)
        