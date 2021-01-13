def DFS(x, res, check, start):
    if x == m:
        print(res)
        return
    for i in range(start, n+1):
        check[i] = True
        DFS(x+1, res+str(i)+' ', check, i)

if __name__ == "__main__":
    n, m = map(int, input().split())
    res =""
    check = [False for _ in range(n+1)]
    DFS(0, res, check, 1)