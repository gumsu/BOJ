from collections import deque

def BFS():
    Q = deque()
    Q.append(n)

    while Q:
        x = Q.popleft()

        if x == m:
            return visited[x]
        for i in (x-1, x+1, x*2):
            if 0 <= i < 100001 and visited[i] == 0:
                visited[i] = visited[x] + 1
                Q.append(i)

n, m = map(int, input().split())
visited = [0]*100001
print(BFS())