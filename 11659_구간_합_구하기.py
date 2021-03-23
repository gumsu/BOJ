import sys
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

sum_value = 0
prefix_sum = [0]

for i in arr:
    sum_value += i
    prefix_sum.append(sum_value)

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(prefix_sum[j]-prefix_sum[i-1])