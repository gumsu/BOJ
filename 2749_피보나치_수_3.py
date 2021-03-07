mod = 15*100000
n = int(input())
new = n%mod
dp = [0,1]
for i in range(2, new+1):
    dp.append((dp[i-1]+dp[i-2])%1000000)
print(dp[new])