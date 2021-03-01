x, y = map(int, input().split())
cnt = 0

if x > y:
    cnt = x
    cnt += y
    cnt += y//10
else:
    cnt = y
    cnt += x
    cnt += x//10
print(cnt)