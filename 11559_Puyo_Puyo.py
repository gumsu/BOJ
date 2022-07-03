from collections import deque
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
board = []
res = 0
'''
1. 보드 탐색하여 4개인 것 찾아 부수기
2. 다 뿌수면 count += 1 (동시에 터지는 것도 하나로 친다), 없으면 종료
3. 떨어뜨리기 -> 바닥에 .이 있으면 떨어져야 한다
4. 반복
'''
def bfs(a, b, graph):
    q = deque()
    q.append((a, b))
    
    visited = [[False] * 6 for _ in range(12)]
    puyo = [] # 터뜨릴 뿌요 모음

    visited[a][b] = True
    puyo.append((a, b))
    count = 1
    flag = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6 and not visited[nx][ny] and board[nx][ny] == graph:
                q.append((nx, ny))
                puyo.append((nx, ny))
                visited[nx][ny] = True
                count += 1
    
    if count >= 4:
        flag = 1
        for x, y in puyo:
            board[x][y] = '.'
    
    return flag

def down():
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if board[j][i] != "." and board[k][i] == ".":
                    board[k][i] = board[j][i]
                    board[j][i] = "."
                    break
    
    # print('-----')
    # for z in board:
    #     print(z)
    # print('-----')

for _ in range(12):
    board.append(list(input()))

while True:
    cnt = 0
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.':
                cnt += bfs(i, j, board[i][j])
    if cnt == 0:
        print(res)
        break
    else:
        res += 1
    
    down()