n = int(input())
cows = [list(map(int, input().split())) for _ in range(n)]
cows.sort(key=lambda x: x[0])
tmp = cows.pop(0)
time = tmp[0]+tmp[1]

for x, y in cows:
    if time < x:
        time = x+y
    elif time >= x:
        time += y
print(time)
# for z in cows:
#     print(z)