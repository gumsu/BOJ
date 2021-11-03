n = int(input())

check = [False]*(n+1)
res = ""

def dfs(depth, res):
	if depth == n:
		print(res)
		return

	for i in range(1, n+1):
		if not check[i]:
			check[i] = True
			dfs(depth + 1, res+str(i)+' ')
			check[i] = False

dfs(0, res)