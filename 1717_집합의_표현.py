import sys
sys.setrecursionlimit(100000)

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int,input().split())
parent = [i for i in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        union_parent(b, c)
    else:
        if find_parent(b) == find_parent(c):
            print("YES")
        else:
            print("NO")