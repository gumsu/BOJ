n = int(input())
cnt = 0
tmp = 1
while True:
    if n >= 0:
        n -= tmp
        cnt += 1
        tmp += 1
    else:
        print(cnt-1)
        break