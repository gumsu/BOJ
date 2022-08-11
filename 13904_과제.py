import heapq
'''
내림차순 정렬해서 마지막 날짜부터 과제할 수 있게 하기
날짜에 맞게 할 수 있는 과제를 꺼내서 q에 담기
q에 넣을 때는 과제 점수를 우선으로 최대힙
6
5 3
5 3
5 3
4 2
4 1
4 2
'''

n = int(input())
homework = []
res = 0

for _ in range(n):
    d, w = map(int, input().split())
    homework.append((d, w))

homework.sort(key=lambda x: (-x[0], -x[1]))

q = []
date = homework[0][0]
while True:
    if date == 0:
        break

    while homework and homework[0][0] >= date:
        d, w = homework.pop(0)
        heapq.heappush(q, (-w, -d))

    date -= 1

    if not q:
        continue

    # print(q)

    a, b = heapq.heappop(q)
    res += -a
    # print(res)
print(res)