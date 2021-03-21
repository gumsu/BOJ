import math

m, n = map(int, input().split())
arr = [True for _ in range(n+1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화

for i in range(2, int(math.sqrt(n))+1):
    if arr[i] == True:
        j = 2
        while i * j <= n:
            arr[i*j] = False
            j += 1

for i in range(m, n+1):
    if i == 1:
        continue
    if arr[i]:
        print(i)

# print(*arr)