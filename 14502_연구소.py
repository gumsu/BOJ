from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
safety = -1e9

# 0: 빈 칸 / 1: 벽 / 2: 바이러스
# 새로운 벽 3개
def barrier(depth):
	if depth == 3:
		# for z in board:
		# 	print(z)
		# print('-----')
		bfs()
		return

	for i in range(n):
		for j in range(m):
			if board[i][j] == 0:
				board[i][j] = 1
				barrier(depth+1)
				board[i][j] = 0

def bfs():
	global safety

	copy = [[0]* m for _ in range(n)]
	for i in range(n):
		for j in range(m):
			copy[i][j] = board[i][j]
			
	q = deque()
	for i in range(n):
		for j in range(m):
			if copy[i][j] == 2:
				q.append([i, j])
	
	while q:
		x, y = q.popleft()
	
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < n and 0 <= ny < m and copy[nx][ny] == 0:
				copy[nx][ny] = 2
				q.append([nx, ny])

	cnt = 0
	for i in copy:
		for j in i:
			if j == 0:
				cnt += 1
	safety = max(safety, cnt)

barrier(0)
print(safety)