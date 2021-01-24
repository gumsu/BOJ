def DFS(L, number, start):
    if L == 6:
        print(number)
        return
    else:
        for i in range(start, k):
            if selected[i] == 0:
                selected[i] = 1
                DFS(L+1, number+str(S[i])+' ', i)
                selected[i] = 0

while True:
    S = list(map(int, input().split()))
    k = S.pop(0)
    if k == 0:
        break
    selected = [0]*k
    DFS(0, "", 0)
    print()