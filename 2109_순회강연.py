import heapq

'''
날짜 기준 내림차순 정렬, 돈 기준 내림차순 정렬
뒤에서부터 가능한 강의 시작하기
가능한 강의들 모두 pop 해서 q에 heappush 하기 (이때 돈 기준으로 최대힙으로 넣어야 함)
최대힙에 넣어서 가장 큰 값 빼서 res 에 합치기
3
1 1
10 2
10 2
'''
n = int(input())
lecture = []
res = 0

if n == 0:
    print(res)
else:
    for _ in range(n):
        p, d = map(int,input().split())
        lecture.append((p,d))

    lecture.sort(key=lambda x: (-x[1],-x[0]))

    day = lecture[0][1]
    q = []
    while True:
        if day == 0:
            break

        while lecture and lecture[0][1] >= day:
            p, d = lecture.pop(0)
            heapq.heappush(q, (-p, -d))
        day -= 1

        # print(q)

        if not q:
            continue
        a, b = heapq.heappop(q)
        res += -a

    print(res)