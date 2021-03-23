n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()
lt, rt = 0, n-1
cnt = 0

while lt < rt:
    if arr[lt] + arr[rt] == x:
        cnt += 1
        lt += 1
        rt -= 1
    elif arr[lt] + arr[rt] < x :
        lt += 1
    else:
        rt -= 1
print(cnt)