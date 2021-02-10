from collections import deque

n, m = map(int, input().split())
miro = [list(map(int, input())) for _ in range(n)]
distance = [[0]*m for _ in range(n)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
Q = deque()
Q.append((0,0))
distance[0][0] = 1

while Q:
    tmp = Q.popleft()

    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]

        if 0 <= x < n and 0 <= y < m and miro[x][y] == 1:
            miro[x][y] = 0
            distance[x][y] = distance[tmp[0]][tmp[1]] + 1
            Q.append((x,y))

# for z in miro:
#     print(z)

print(distance[n-1][m-1])