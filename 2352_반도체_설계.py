from bisect import bisect_left

n = int(input())
port = list(map(int, input().split()))
res = []

for i in port:
    if not res or res[-1] < i:
        res.append(i)
    else:
        idx = bisect_left(res, i)
        res[idx] = i
print(len(res))