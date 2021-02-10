from collections import deque

def DFS(level):
    print(level, end=' ')
    visit[level] = 1
    for i in range(1, n+1):
        if board[level][i] == 1 and visit[i] == 0:
            DFS(i)

def BFS(level):
    Q = deque()
    Q.append(level)

    visit[level] = 0

    while Q:
        level = Q.popleft()
        print(level, end=' ')

        for i in range(1, n+1):
            if visit[i] == 1 and board[level][i] == 1:
                Q.append(i)
                visit[i] = 0

n, m, v = map(int, input().split())
visit = [0]*(n+1)
board = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    x, y = map(int,input().split())
    board[x][y] = board[y][x] = 1

DFS(v)
print()
BFS(v)