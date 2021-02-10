from collections import deque

n = int(input())
house = [list(map(int, input())) for _ in range(n)]
cnt = 0
res = []

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

Q = deque()

for i in range(n):
    for j in range(n):
        if house[i][j] == 1:
            house[i][j] = 0
            Q.append((i,j))
            cnt = 1
            while Q:
                tmp = Q.popleft()
                for k in range(4):
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]

                    if 0 <= x < n and 0 <= y < n and house[x][y] == 1:
                        house[x][y] = 0
                        Q.append((x,y))
                        cnt += 1
            res.append(cnt)

print(len(res))
res.sort()
for z in res:
    print(z)
# for z in house:
#     print(z)