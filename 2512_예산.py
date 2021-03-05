from bisect import bisect_left, bisect_right
n = int(input())
city = list(map(int,input().split()))
m = int(input())

lt = 0
rt = max(city)
total = sum(city)
result = 0

if sum(city) == m:
    print(max(city))
else:
    while lt <= rt:
        mid = (lt + rt) // 2
        tmp = 0
        for i in city:
            tmp += min(i, mid)

        if tmp > m:
            rt = mid - 1
        else:
            lt = mid + 1
            result = max(tmp, result)

    print(rt)