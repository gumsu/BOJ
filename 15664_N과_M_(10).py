def DFS(L, res, check, start):
    global answer
    if L == m:
        answer += res + '\n'
        return
    for i in range(start, maxNum+1):
        if check[i] == 0:
            continue
        check[i] -= 1
        DFS(L+1, res+str(i)+' ', check, i)
        check[i] += 1

if __name__=="__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    check = [0]*10001
    for i in a:
        check[i] += 1
    maxNum = max(a)
    answer = ""
    DFS(0, "", check, 1)
    print(answer)