def DFS(idx, res, ch):
    if idx == m:
        print(res)
        return
    for i in range(1,n+1):
        ch[i] = True
        DFS(idx+1, res+str(i)+' ', ch)
        ch[i] = False

if __name__=="__main__":
    n, m = map(int, input().split())
    res =""
    ch = [False for _ in range(n+1)]
    DFS(0, res, ch)
