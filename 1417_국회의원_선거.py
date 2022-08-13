import heapq
n = int(input())
dasom = int(input())

if n == 1:
    print(0)
else:
    member = []
    for _ in range(n-1):
        heapq.heappush(member, (int(input())) * -1 )

    cnt = 0

    while True:
        if -member[0] < dasom:
            break

        dasom += 1
        temp = heapq.heappop(member)
        heapq.heappush(member, temp+1)
        cnt += 1
    print(cnt)