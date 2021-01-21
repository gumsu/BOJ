import sys
n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
# a = list(map(int, input().split()))
a.sort()

def DFS(L, res):
    if L == m:
        print(res)
        return
    tmp = 0
    for i in range(n):
        if tmp == a[i]:
            continue
        tmp = a[i]
        DFS(L+1, res + str(a[i])+' ')

DFS(0, "")