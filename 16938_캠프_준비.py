n, l, r, x = map(int, input().split())
test = list(map(int, input().split()))
# 2 문제 이상 픽 / l <= 난이도 합 <= r / abs(가장 어려운 - 가장 쉬운) >= x

cnt = 0

def dfs(depth, idx, total_sum, min_num, max_num):
    global cnt
    if depth >= 2:
        if l <= total_sum <= r and max_num - min_num >= x:
            cnt += 1
            
    for i in range(idx, n):
        if total_sum + test[i] <= r:
            dfs(depth+1, i+1, total_sum + test[i], min(min_num, test[i]), max(max_num, test[i]))


dfs(0, 0, 0, 1e9, -1e9)
print(cnt)