import sys
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
m = int(input())

sum_value = 0
interval_sum = [0]

for i in arr:
    sum_value += i
    interval_sum.append(sum_value)

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(interval_sum[j] - interval_sum[i-1])
