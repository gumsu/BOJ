n, c = map(int, input().split())
wifi = [int(input()) for _ in range(n)]

wifi.sort()

def Count(mid):
    cnt = 1
    endPoint = wifi[0]

    for i in range(1, n):
        if wifi[i] - endPoint >= mid:
            cnt += 1
            endPoint = wifi[i]
    return cnt
lt = 1
rt = max(wifi)

while lt <= rt:

    mid = (lt + rt) // 2

    if Count(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)