n, m = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
end_point = 0
interval_sum = 0

for start_point in range(n):
    # end 이동
    while interval_sum < m and end_point < n:
        interval_sum += arr[end_point]
        end_point += 1
    # 부분합이 m일때 count 증가
    if interval_sum == m:
        cnt += 1
    interval_sum -= arr[start_point]

print(cnt)