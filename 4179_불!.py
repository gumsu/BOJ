from collections import deque
r, c = map(int, input().split())
# # 벽 . 지나갈 수 있는 공간 J 초기 위치 F 불이 난 공간
# 불이 갈 수 있는 거리 체크, 지훈이가 갈 수 있는 거리 체크
miro = [list(input()) for _ in range(r)]
# 불 BFS 탐색용, 지훈이 BFS 탐색용
fire = [item[:] for item in miro]
jihoon = [item[:] for item in miro]
visited = [[False]*c for _ in range(r)]
isPossible = False
embers = deque()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(r):
    for j in range(c):
        if fire[i][j] == '.' or fire[i][j] == 'J':
            fire[i][j] = 10e9

def user_bfs(x, y):
    global isPossible
    q = deque()
    q.append((x, y))
    # visited[x][y] = True
    jihoon[x][y] = 1
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            # 지훈이의 위치가 가장자리 도달하면 끝
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                isPossible = True
                print(jihoon[a][b])
                return
            else:   # 불 속도보다 빨리 탈출해야함
                if miro[nx][ny] == '.' and jihoon[nx][ny] == '.' and jihoon[a][b] + 1 < fire[nx][ny]:
                    # visited[nx][ny] = True
                    jihoon[nx][ny] = jihoon[a][b] + 1
                    q.append((nx, ny))

def fire_bfs():

    q = deque()
    time = 1
    while embers:
        x, y = embers.popleft()
        q.append((x, y))
        fire[x][y] = 1
    while q:
        for _ in range(len(q)): # 여러 불꽃 동시에 카운트 시작
            a, b = q.popleft()
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0 <= nx < r and 0 <= ny < c and fire[nx][ny] == 10e9:
                    fire[nx][ny] = time + 1
                    q.append((nx, ny))
        time += 1

for i in range(r):
    for j in range(c):
        if miro[i][j] == 'J':   # 지훈이 위치
            a, b = i, j
        if miro[i][j] == 'F':   # 불 위치
            embers.append((i, j))

fire_bfs()
user_bfs(a, b)

if not isPossible:
    print("IMPOSSIBLE")

# print('---------------')
# for z in jihoon:
#     print(z)
# print('---------------')
# for z in fire:
#     print(z)
# print('---------------')