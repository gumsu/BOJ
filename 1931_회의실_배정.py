n = int(input())
meeting = [tuple(map(int, input().split())) for _ in range(n)]

meeting.sort(key= lambda x: (x[1], x[0]))

cnt = 0
tmp = 0

for start, end in meeting:
    if tmp <= start:
        cnt += 1
        tmp = end
print(cnt)