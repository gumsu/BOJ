from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)

for _ in range(m):
    tmp = list(map(int, input().split()))
    for i in range(1, tmp[0]):
        graph[tmp[i]].append(tmp[i+1])
        indegree[tmp[i+1]] += 1

# print(indegree)
# for z in graph:
#     print(z)
def topology_sort():
    result = []
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    if len(result) == n:    # 모든 가수가 정상적으로 result안에 들어감
        for i in result:
            print(i)
    else:
        print(0)
topology_sort()