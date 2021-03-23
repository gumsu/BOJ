n = int(input())
m = int(input())
arr = list(map(int ,input().split()))
arr.sort()

lt, rt = 0, n-1
cnt = 0

while lt < rt:
    if arr[lt] + arr[rt] == m:
        cnt += 1
        lt += 1
        rt -= 1
    elif arr[lt] + arr[rt] < m:
        lt += 1
    else:
        rt -= 1

print(cnt)