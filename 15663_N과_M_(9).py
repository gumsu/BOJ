def DFS(L, check, res, maxNum):
    global answer
    if L == m:
        answer += res + '\n'
        return
    for i in range(1, maxNum+1):
        if check[i] != 0:
            check[i] -= 1
            DFS(L+1, check, res+str(i)+' ', maxNum)
            check[i] += 1
if __name__=="__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    check = [0]*10001
    maxNum = max(a)
    for i in a:
        check[i] += 1
    answer = ""
    DFS(0, check, "", maxNum)
    print(answer)