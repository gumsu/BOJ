dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

r, c, k = map(int, input().split())
board = [list(input()) for _ in range(r)]
check = [[False]*c for _ in range(r)]

res = 0
def dfs(x, y, cnt, check):
	global res
	if x == 0 and y == c-1 and cnt == k:
		res += 1
		return

	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == '.' and not check[nx][ny]:
			check[nx][ny] = True
			dfs(nx, ny, cnt+1, check)
			check[nx][ny] = False

check[r-1][0] = True
dfs(r-1, 0, 1, check)
print(res)