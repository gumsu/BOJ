from collections import deque
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[False]*m for _ in range(n)]
drawing = []
def BFS(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    cnt = 1
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = True
                board[nx][ny] = -1
                q.append((nx, ny))
                cnt += 1
    return cnt

for i in range(n):
    for j in range(m):
        if not visited[i][j] and board[i][j] == 1:
            area = BFS(i, j)
            drawing.append(area)
print(len(drawing))
if len(drawing) == 0:
    print(0)
else:
    print(max(drawing))
# print(*drawing)