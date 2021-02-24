n = int(input())
scale = list(map(int ,input().split()))
scale.sort()
weight = 1

for i in range(n):
    if weight < scale[i]:
        break
    weight += scale[i]

print(weight)