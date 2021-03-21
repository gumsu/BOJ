import math

def isPrime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

n = int(input())
arr = map(int, input().split())
cnt = 0

for i in arr:
    if i == 1:
        continue
    if isPrime(i):
         cnt += 1
print(cnt)