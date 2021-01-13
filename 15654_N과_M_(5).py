def DFS(x, idx, res, check):
    if idx == m:
        print(res)
        return
    for i in range(n):
        if not check[i]:
            check[i]=True
            DFS(nlist[i],idx+1, res+str(nlist[i])+' ',check)
            check[i]=False

if __name__ == "__main__":
    n, m = map(int, input().split())
    nlist = list(map(int, input().split()))
    nlist.sort()
    res =""
    check = [False for _ in range(n+1)]
    DFS(nlist[0], 0, res, check)