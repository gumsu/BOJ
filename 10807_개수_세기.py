n = int(input())
nList = list(map(int, input().split()))
v = int(input())

cnt = 0
for i in nList:
    if i == v:
        cnt += 1
print(cnt)