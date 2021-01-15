def DFS(L, check, res):
    global answer
    used = [False]*10001
    if L == m:
        answer += res + '\n'
        return
    for i in range(n):
        if not check[i] and not used[a[i]]:
            used[a[i]] = True
            check[i] = True
            DFS(L+1, check, res+str(a[i])+' ')
            check[i] = False
if __name__=="__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    answer = ""
    check = [False]*n
    DFS(0, check, "")
    print(answer)