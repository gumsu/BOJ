from collections import deque

# 북 동 남 서
dx =[-1, 0, 1, 0]
dy =[0, 1, 0, -1]

n, m = map(int, input().split())

# 0-북 1-동 2-남 3-서
r, c, d = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

Q = deque()
Q.append((r,c))
cnt = 0
while Q:
    tmp = Q.popleft()
    if board[tmp[0]][tmp[1]] == 0:  # 현재 위치 청소
        board[tmp[0]][tmp[1]] = 2
        cnt += 1
    
    flag = False
    for _ in range(4):
        # if flag == True:    # 왼쪽 청소 완료
        #     break
        d = (d+3) % 4 
        x = tmp[0] + dx[d]
        y = tmp[1] + dy[d]
        if 0 < x < n and 0 < y < m and board[x][y] == 0:
            flag = True
            board[x][y] = 2
            cnt += 1
            Q.append((x,y))
            break
    else:
        nd = (d+2) % 4
        nx = tmp[0] + dx[nd]
        ny = tmp[1] + dy[nd]
        if 0 > nx or nx >= n and 0 > ny or ny >= m or board[nx][ny] == 1:
            break
        Q.append((nx,ny))

# for z in board:
#     print(z)
print(cnt)