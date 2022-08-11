import heapq
'''
보석 무게대로 오름차순 정렬
가방 무게대로 오름차순 정렬

가방에 담을 수 있는 모든 보석들을 최대힙에 넣기
최대힙에서 제일 가치 큰 보석 꺼내기
4 2
4 100
5 110
6 90
7 80
5 
7
'''
n, k = map(int, input().split())

jem = []
bags = []
value = 0
for _ in range(n):
    m, v = map(int, input().split())
    jem.append([m, v])
for _ in range(k):
    c = int(input())
    bags.append(c)

jem.sort()
bags.sort()

temp_bag = []

for bag in bags:
    while jem and bag >= jem[0][0]:
        heapq.heappush(temp_bag, -jem[0][1])
        heapq.heappop(jem)
    
    if temp_bag:
        value += heapq.heappop(temp_bag) * -1

print(value)