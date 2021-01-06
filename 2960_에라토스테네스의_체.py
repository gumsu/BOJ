n, k = map(int,input().split())

arr = list(range(2,n+1))
ch = [0]*(n+1)
cnt = 0

for i in range(2, n+1):
    for j in range(i, n+1, i):
        if ch[j] == 0 :
            ch[j] = 1
            cnt += 1
            if cnt == k:
                print(j)
                break