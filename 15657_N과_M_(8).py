def DFS(L, check, start):
    if L == m:
        print(*res)
        return
    for i in range(start, n):
        res[L] = a[i]
        check[i] = True
        DFS(L+1, check, i)
        check[i] = False

if __name__=="__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    check = [False for _ in range(n)]
    res = [0]*m
    DFS(0, check, 0)
