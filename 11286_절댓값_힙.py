import heapq
import sys

n = int(input())
q = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if not q:
            print(0)
        else:
            a, b = heapq.heappop(q)
            # print(a, b, "꺼낸 수")
            print(b)
    else:
        heapq.heappush(q, (abs(x), x)) # 절댓값, 원래 수