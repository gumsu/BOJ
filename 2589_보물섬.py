from collections import deque
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

def BFS(x, y):
    Q = deque()
    cnt = 1
    check = [[0]*m for _ in range(n)]
    Q.append((x, y))
    check[x][y] = 1

    while Q:
        tmp = Q.popleft()
        for k in range(4):
            xx = tmp[0] + dx[k]
            yy = tmp[1] + dy[k]
            if 0 <= xx < n and 0 <= yy < m and check[xx][yy] == 0 and board[xx][yy] == 'L':
                check[xx][yy] = check[tmp[0]][tmp[1]] + 1
                cnt = max(cnt, check[xx][yy])
                Q.append((xx,yy))
    
    # print('----------')
    # for z in check:
    #     print(z)
    # print('----------')
    return cnt-1

res = -1
for i in range(n):
    for j in range(m):
        if board[i][j] == 'L':
            max_cnt = BFS(i, j)
            res = max(max_cnt, res)
            
# for z in board:
#     print(z)
# for z in check:
#     print(z)
print(res)