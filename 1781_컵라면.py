import heapq
'''
q 길이가 데드라인보다 크면 빼기 (마감기한 안에 못하는 과제 뺴야함-최소힙)
'''
n = int(input())

awards = []
for _ in range(n):
    deadline, cup = map(int,input().split())
    awards.append((deadline, cup))

awards.sort()

q = []
for deadline, cup in awards:
    heapq.heappush(q, cup)
    if deadline < len(q):
        heapq.heappop(q)
print(sum(q))