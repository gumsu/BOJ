def DFS(L, start, res):
    if L == m:
        print(res)
        return
    tmp = 0
    for i in range(start, n):
        if a[i] == tmp:
            continue
        tmp = a[i]
        DFS(L+1, i, res + str(a[i])+' ')

if __name__=="__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    DFS(0, 0, "")