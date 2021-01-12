def DFS(idx, res, ch, start):
    if idx == m:
        print(res)
        return
    for i in range(start, n+1):
        if not ch[i]:
            ch[i] = True
            DFS(idx+1, res+str(i)+' ', ch, i+1)
            ch[i] = False

if __name__ == "__main__":
    n, m = map(int, input().split())
    res = ""
    ch = [False for _ in range(n+1)]
    DFS(0, res, ch,1)