def get_smallest_node():
    min_value = INF
    index = 0   # 가장 최단 거리가 짧은 노드
    for i in range(1, v+1):
        if distance[i] < min_value and not visited[i]:
             min_value = distance[i]
             index = i
    return index

def dijkstra(num):
    distance[num] = 0
    visited[num] = True
    for i, j in graph[num]:
        # print(i, j)
        distance[i] = min(j, distance[i])   # 중복 간선 중 작은 값 택
    # 시작 노드를 제외한 전체 n-1 노드에 대해 반복
    for i in range(v-1):
        now = get_smallest_node()   # 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
        visited[now] = True
        for x, y in graph[now]: # 현재 노드와 연결된 다른 노드 확인
            cost = distance[now] + y
            # 현재 노드를 거쳐 가는게 더 짧을 경우 갱신
            if cost < distance[x]:
                distance[x] = cost

v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int ,input().split())
    graph[a].append((b,c))
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정
visited = [False]*(v+1)
distance = [INF]*(v+1)

dijkstra(k)

# for z in graph:
#     print(z)
# for z in visited:
#     print(z)
for z in range(1, v+1):
    if distance[z] == INF:
        print('INF')
    else:
        print(distance[z])