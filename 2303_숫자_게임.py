# 카드 3장 고르기
def dfs(depth, total, arr):
	global max_sum
	if depth == 3:
		if total >= 10:
			total = total%10
		max_sum = max(max_sum, total)
		return

	for i in range(len(arr)):
		if not check[i]:
			check[i] = True
			dfs(depth+1, total+arr[i], arr)
			check[i] = False

n = int(input())
people = []
for _ in range(n):
	person = list(map(int, input().split()))
	check = [False]*len(person)
	max_sum = -1e9

	dfs(0, 0, person)
		
	people.append(max_sum)

# for z in people:
# 	print(z)
res = 0
val = 0
for idx, value in enumerate(people):
	if value >= val :
		val = value
		res = idx

print(res+1)