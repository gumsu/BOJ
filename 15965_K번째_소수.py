import math

num = 7368788 # 500,000번째 소수는 7368787
arr = [True for _ in range(num+1)]
arr[0] = False
arr[1] = False
for i in range(2, int(math.sqrt(num))+1):
    if arr[i]:
        j = 2
        while i * j <= num:
            arr[i*j] = False
            j += 1

k = int(input())
cnt = 0
for i in range(len(arr)):
    if arr[i]:
        cnt += 1
        if cnt == k:
            print(i)
            break