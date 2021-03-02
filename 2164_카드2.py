from collections import deque
n = int(input())
arr = list(range(1,n+1))
arr = deque(arr)
card = 0
while len(arr)!=1:
    arr.popleft()
    card = arr.popleft()
    arr.append(card)

print(arr[0])