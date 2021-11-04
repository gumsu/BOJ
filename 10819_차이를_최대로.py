from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))

def cal(tuple):
    total = 0
    for i in range(1, n):
        total += abs(tuple[i-1] - tuple[i])
    return total

result = -1e9

for i in permutations(arr):
    result = max(result, cal(i))

print(result)