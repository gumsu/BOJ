import heapq as hq
from collections import deque

n = int(input())
c = []
for _ in range(n):
    x, y = map(int, input().split())
    c.append((x,y))

c.sort(key=lambda x: x[0])
queue = [] # 현재 강의 중인 강의실 개수

hq.heappush(queue, c[0][1])
for i in range(1, n):
    if queue[0] > c[i][0]:
        hq.heappush(queue, c[i][1])
    else:
        hq.heappop(queue)
        hq.heappush(queue, c[i][1])

print(len(queue))