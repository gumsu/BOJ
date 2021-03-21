import math

num = 123456
arr = [True for _ in range(num * 2 + 1)]
arr[0] = False
arr[1] = False
for i in range(2, int(math.sqrt(num*2))+1):
    if arr[i]:
        j = 2
        while i * j <= 2*num:
            arr[i*j] = False
            j += 1

while True:
    n = int(input())
    if n == 0:
        break

    cnt = 0
    for i in range(n+1, n*2+1):
        if arr[i]:
            cnt += 1
    print(cnt)