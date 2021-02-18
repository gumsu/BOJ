import sys
sys.setrecursionlimit(10000)
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def DFS(x, y, h):
    check[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]

        if 0 <= xx < n and 0 <= yy < n and check[xx][yy] == 0 and board[xx][yy] > h:
            DFS(xx, yy, h) 
n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
res = 0 # 최대 개수

for k in range(max(max(board))+1):
    check = [[0]*n for _ in range(n)]
    cnt = 0 # 안전 영역의 개수

    for i in range(n):
        for j in range(n):
            if check[i][j] == 0 and board[i][j] > k :
                cnt += 1
                DFS(i, j, k)
    
    res = max(res, cnt)
    if cnt == 0:
        break
print(res)