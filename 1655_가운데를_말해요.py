'''
left - 최대힙 (음수로 넣음)
right - 최소힙
left와 right 길이가 같으면 left로 넣기
개수가 짝수일 경우 작은 값을 꺼내야 하므로 힙에 있는 값 비교해서 바꿔주기
답은 left에서 꺼내면 된다.
'''
import heapq
import sys

n = int(sys.stdin.readline())
left = []
right = []

def printMiddleNumber(x):
    if len(left) == len(right):
        heapq.heappush(left, -x)
    else:
        heapq.heappush(right,x)
    if left and right and -left[0] > right[0]:
        left_temp = heapq.heappop(left) * -1
        right_temp = heapq.heappop(right)

        heapq.heappush(left, -right_temp)
        heapq.heappush(right, left_temp)
    print(-left[0])
for _ in range(n):
    printMiddleNumber(int(sys.stdin.readline()))