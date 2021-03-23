n = int(input())

lt, rt = 0, 1
cnt = 0
interval_sum = 1

while lt <= rt and rt <= n:
    if interval_sum == n:
        rt += 1
        interval_sum = interval_sum - lt + rt
        lt += 1
        cnt += 1
    elif interval_sum < n:
        rt += 1
        interval_sum += rt
    else:
        interval_sum -= lt
        lt += 1
print(cnt)