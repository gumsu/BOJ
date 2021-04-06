from collections import deque

def fire_bfs():
    q = deque()
    time = 1

    while flame:
        x, y = flame.popleft()
        q.append((x, y))
        fire[x][y] = 1
    while q:
        for _ in range(len(q)):
            a, b = q.popleft()
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0 <= nx < h and 0 <= ny < w and fire[nx][ny] == 10e9 :
                    fire[nx][ny] = time + 1
                    q.append((nx, ny))
        time += 1

def user_bfs(x, y):
    global isPossible
    q = deque()
    q.append((x, y))
    user[x][y] = 1
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w :
                isPossible = True
                print(user[a][b])
                return
            else:
                if user[nx][ny] == '.' and user[a][b]+1 < fire[nx][ny]:
                    user[nx][ny] = user[a][b] + 1
                    q.append((nx, ny))
                    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    fire = [item[:] for item in board]
    user = [item[:] for item in board]

    human = []
    flame = deque()
    isPossible = False

    for i in range(h):
        for j in range(w):
            if board[i][j] == '@':
                human.append(i)
                human.append(j)
            elif board[i][j] == '*':
                flame.append((i, j))

    for i in range(h):
        for j in range(w):
            if fire[i][j] == '#':
                continue
            fire[i][j] = 10e9

    fire_bfs()
    user_bfs(human[0], human[1])

    if not isPossible:
        print("IMPOSSIBLE")