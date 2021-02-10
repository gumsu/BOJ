from collections import deque

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
res = -2147000000
flag = False

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

Q = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            Q.append((i,j))
while Q:
    tmp = Q.popleft()
    for k in range(4):
        x = tmp[0] + dx[k]
        y = tmp[1] + dy[k]

        if 0 <= x < n and 0 <= y < m and box[x][y] == 0:
            box[x][y] = box[tmp[0]][tmp[1]] + 1
            res = max(res, box[x][y])
            Q.append((x, y))
            flag = True

for tomato in box:
    if 0 in tomato:
        print(-1)
        break
else:
    if flag == True:
        print(res-1)
    else:
        print(0)