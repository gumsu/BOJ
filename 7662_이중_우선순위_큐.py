import heapq

'''
최대힙, 최소힙에 모두 넣기
최대값 삭제 시 최대힙에서 빼기 -> 최소힙에서도 빼주어야 하므로 따로 저장
최소값 삭제 시 최소힙에서 빼기 -> 최대힙에서도 빼주어야 하므로 따로 저장
마지막에 값 하나 씩 꺼내기
1
12
I 9
I 7
I 9
I 6
I 7
I 7
I 9
D -1
D 1
I 8
D 1
D 1
'''
t = int(input())

for _ in range(t):
    k = int(input())
    exist = [0] * k

    maxH = []
    minH = []

    for key in range(k):
        o, n = map(str, input().split())

        if o == "I":
            heapq.heappush(maxH, (-int(n), key))
            heapq.heappush(minH, (int(n), key))
            exist[key] = 1
        else:
            if n == "1":    # 최대값 삭제
                while maxH and not exist[maxH[0][1]]:
                    heapq.heappop(maxH)
                if maxH:
                    exist[heapq.heappop(maxH)[1]] = 0
            else:   # 최소값 삭제
                while minH and not exist[minH[0][1]]:
                    heapq.heappop(minH)
                if minH:
                    exist[heapq.heappop(minH)[1]] = 0
    
    while maxH and not exist[maxH[0][1]]:
        heapq.heappop(maxH)
    while minH and not exist[minH[0][1]]:
        heapq.heappop(minH)
    
    # print(f'minH = {minH}, maxH = {maxH}')

    if not minH or not maxH:
        print("EMPTY")
    else:
        print(-maxH[0][0], minH[0][0])