import heapq
import sys

n = int(input())
q = []
total = 0
for _ in range(n):
    x = int(sys.stdin.readline())
    q.append(x)
heapq.heapify(q)
while len(q) > 1:
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    total += a+b
    heapq.heappush(q, a+b)
print(total)