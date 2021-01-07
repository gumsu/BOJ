n = int(input())
nArr = list(map(int, input().split()))
m = int(input())
mArr = list(map(int, input().split()))

nArr.sort()

for i in mArr:
    lt = 0
    rt = n-1
    res = 0

    while lt <= rt:
        mid = (lt + rt) // 2

        if nArr[mid] == i:
            res = 1
            break
        elif nArr[mid] > i:
            rt = mid - 1
        else:
            lt = mid + 1
    print(res)