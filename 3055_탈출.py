from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
r, c = map(int, input().split())
forest = [list(input()) for _ in range(r)]
flood = [item[:] for item in forest]
animal = [item[:] for item in forest]
# . 빈 칸 * 물 X 돌 D 비버굴 S 고슴도치
# 물, 고슴도치 돌 통과X / 비버굴에 물 통과 X
stone = []
water = deque()
beaver_cave = []
hedgehog = []
isPossible = False

for i in range(r):
    for j in range(c):
        if forest[i][j] == 'X':
            stone.append((i, j))
        elif forest[i][j] == '*':
            water.append((i ,j))
        elif forest[i][j] == 'D':
            beaver_cave.append(i)
            beaver_cave.append(j)
        elif forest[i][j] == 'S':
            hedgehog.append(i)
            hedgehog.append(j)

for i in range(r):
    for j in range(c):
        if flood[i][j] == '.' or flood[i][j] == 'S':
            flood[i][j] = 10e9

def flood_bfs():
    q = deque()
    time = 1
    while water:
        x, y = water.popleft()
        q.append((x, y))
        flood[x][y] = 1
    while q:
        for _ in range(len(q)):
            a, b = q.popleft()
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0 <= nx < r and 0 <= ny < c and flood[nx][ny] == 10e9 :
                    flood[nx][ny] = time + 1
                    q.append((nx, ny))
        time += 1

def hedgehog_bfs(x, y):
    global isPossible
    q = deque()
    q.append((x, y))
    animal[x][y] = 1
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if beaver_cave[0] == nx and beaver_cave[1] == ny:
                isPossible = True
                print(animal[a][b])
                return
            else:
                if 0 <= nx < r and 0 <= ny < c and animal[nx][ny] == '.' and animal[a][b] +1 < flood[nx][ny]:
                    animal[nx][ny] = animal[a][b] + 1
                    q.append((nx, ny))

flood_bfs()
hedgehog_bfs(hedgehog[0], hedgehog[1])

if not isPossible:
    print("KAKTUS")
    
# print('-------------')
# for z in flood:
#     print(z)
# print('-------------')
# for z in animal:
#     print(z)
# print('-------------')