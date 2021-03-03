from collections import deque
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

m, n, k = map(int, input().split())
arr = [[0]*n for _ in range(m)]

for _ in range(k):
    x, y, z, w = map(int, input().split())
    for i in range(y, w):
        for j in range(x, z):
            arr[i][j] = 1

Q = deque()
cnt = 0
result = []
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            Q.append((i,j))
            cnt += 1
            area = 0
            while Q:
                tmp = Q.popleft()
                arr[tmp[0]][tmp[1]] = 2
                area += 1
                for r in range(4):
                    xx = tmp[0] + dx[r]
                    yy = tmp[1] + dy[r]
                    if 0 <= xx < m and 0 <= yy < n and arr[xx][yy] == 0:
                        arr[xx][yy] = 2
                        Q.append((xx, yy))
            # print(f' area -> {area}')
            result.append(area)
# for z in arr:
#     print(z)
print(cnt)
result.sort()
print(*result)