import sys
sys.setrecursionlimit(50000)

def DFS(x, y):
    cabbage[x][y] = 0
    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]
        if 0 <= a < n and 0 <= b < m and cabbage[a][b] == 1:
            DFS(a,b)

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())
    cabbage = [[0]*m for _ in range(n)]

    cnt = 0

    for _ in range(k):
        a, b = map(int,input().split())
        cabbage[b][a] = 1

    for x in range(n):
        for y in range(m):
            if cabbage[x][y] == 1:
                DFS(x,y)
                cnt += 1
    print(cnt)


    # for x in cabbage:
    #     print(x)