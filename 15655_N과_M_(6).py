def DFS(idx, res, check, start):
    if idx == m:
        print(res)
        return
    for i in range(start, n):
        if not check[i]:
            check[i] = True
            DFS(idx+1, res+str(nlist[i])+' ', check, i)
            check[i] = False

if __name__ == "__main__":
   n, m = map(int, input().split())
   nlist = list(map(int,input().split()))
   nlist.sort()
   res = ""
   check = [False for _ in range(n)]
   DFS(0, res, check, 0) 