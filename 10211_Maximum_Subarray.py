t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    sum_value = 0
    dp = [0]*n
    dp[0] = arr[0]
    
    for i in range(1, n):
        dp[i] = max(dp[i-1]+arr[i], arr[i])
    
    print(max(dp))