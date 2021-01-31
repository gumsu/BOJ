def DFS(L):
    global cnt
    if L == n:
        cnt += 1
        return
    for i in range(n):
        if not (a[i] or b[L+i] or c[L-i+n-1]):
            a[i] = b[L+i] = c[L-i+n-1] = True
            DFS(L+1)
            a[i] = b[L+i] = c[L-i+n-1] = False

n = int(input())
a, b, c = [False]*n, [False]*(2*n-1), [False]*(2*n-1)

cnt = 0
DFS(0)
print(cnt)