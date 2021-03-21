import math

m = int(input())
n = int(input())
arr = [True for _ in range(n+1)]

for i in range(2, int(math.sqrt(n))+1):
    if arr[i]:
        j = 2
        while i * j <= n:
            arr[i*j] = False
            j += 1
prime_sum = 0
prime_min = 2147483647
flag = False
for i in range(m, n+1):
    if i == 1: 
        continue
    if arr[i]:
        flag = True
        prime_sum += i
        prime_min = min(prime_min, i)
if flag:
    print(prime_sum)
    print(prime_min)
else:
    print(-1)