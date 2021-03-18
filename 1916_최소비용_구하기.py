import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))   # 거리 비용, 지금 현재 노드
    distance[start] = 0
    while q:
        dis, now = heapq.heappop(q)
        if distance[now] < dis:
            continue
        for x, y in graph[now]: # 현재 노드 now에서 x 노드까지 거리 비용 y
            cost = dis + y
            if cost < distance[x]:
                distance[x] = cost
                heapq.heappush(q, (cost, x))

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))  # a 노드에서 b 노드까지 거리 비용 c
first, last = map(int, input().split())
INF = int(1e9)
distance = [INF]*(n+1)

dijkstra(first)
print(distance[last])

# for z in graph:
#     print(z)