def DFS(L, sum):
    global cnt
    if L == n:
        return
    if sum+nums[L] == s:
        cnt += 1
    DFS(L+1, sum+nums[L])
    DFS(L+1, sum)


n, s = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
DFS(0, 0)
print(cnt)