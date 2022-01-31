from collections import deque

n = int(input())
cnt = 0
for _ in range(n):
    word = input()
    q = deque()
    for i in word:
        if q and q[-1] == i:
            q.pop()
        else:
            q.append(i)
        # print(q)
    if not q:
        cnt += 1
print(cnt)