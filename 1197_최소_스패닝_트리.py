import sys
sys.setrecursionlimit(100000)

# 부모 노드를 찾는 함수
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

# 두 부모 노드를 합치는 함수
def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [i for i in range(v+1)]

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort(key=lambda x: x[0])

result = 0
for cost, a, b in edges:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += cost

print(result)