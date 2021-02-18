# f(x-1) + 1
# f(x/2) + 1
# f(x/3) + 1
# 함수들 중 최솟값을 구한다.
# f(x) = min(f(x/3), f(x/2), f(x-1)) + 1

n = int(input())
dp = [0]*(n+1)

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1 # 먼저 이전 단계 +1을 다 넣어준다.

    # 3의 배수이거나 2의 배수라면 바꾼다.
    if i%3 == 0:    # 3의 배수라면
        dp[i] = min(dp[i], dp[int(i/3)] +1) # 이전 단계 +1 과 3배수 + 1 중 더 작은 수 택한다.
    if i%2 == 0:
        dp[i] = min(dp[i], dp[int(i/2)] +1)

print(dp[n])