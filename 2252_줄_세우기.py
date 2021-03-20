from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
# 진입 차수
indegree = [0]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1 # b 앞에 a가 있음(선수과목 존재)

def topology_sort():
    result = []
    q = deque()
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입(선수과목이 없는 노드)
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        # 연결된 노드들 진입차수 -1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0인 노드를 큐에 넣기
            if indegree[i] == 0:
                q.append(i)
    
    for i in result:
        print(i, end= ' ')

topology_sort()
# for z in graph:
#     print(z)
# for z in indegree:
#     print(z)