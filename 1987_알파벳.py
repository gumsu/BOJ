def DFS(x, y, cnt):
    global res
    # print(x, y)
    # print(check)

    res = max(res, cnt)

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        
        if 0 <= xx < r and 0 <= yy < c and check[ord(board[xx][yy])-65] == 0:
            check[ord(board[xx][yy])-65] = 1
            DFS(xx, yy, cnt+1)
            check[ord(board[xx][yy])-65] = 0

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

res = 0
check = [0]*27
check[ord(board[0][0])-65] = 1
DFS(0, 0, 1)

print(res)

# for z in board:
#     print(z)