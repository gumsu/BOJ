from collections import deque
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def BFS(x, y, num, color):
    
    Q = deque()
    Q.append((x, y))
    check[x][y] = num
    while Q:
        a, b = Q.popleft()
        for k in range(4):
            xx = a + dx[k]
            yy = b + dy[k]
            if 0 <= xx < n and 0 <= yy < n and check[xx][yy] == 0 and arr[xx][yy] == color:
                check[xx][yy] = num
                Q.append((xx,yy))
    # print('-------')
    # for z in check:
    #     print(z)
    # print('-------')

n = int(input())
arr = [list(input()) for _ in range(n)]
check = [[0]*n for _ in range(n)]
cnt1 = 0
cnt2 = 0

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R' and check[i][j] == 0:
            BFS(i, j, 1, 'R')
            cnt1 +=1
        elif arr[i][j] == 'G' and check[i][j] == 0:
            BFS(i, j, 2, 'G')
            cnt1 +=1
        elif arr[i][j] == 'B' and check[i][j] == 0:
            BFS(i, j, 3, 'B')
            cnt1 +=1

check = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G' and check[i][j] == 0:
            arr[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R' and check[i][j] == 0:
            BFS(i, j, 1, 'R')
            cnt2 +=1
        elif arr[i][j] == 'B' and check[i][j] == 0:
            BFS(i, j, 3, 'B')
            cnt2 +=1

# for i in range(n):
#     for j in range(n):
#         if arr[i][j] == 'R':
#             check[i][j] = 1
#         elif arr[i][j] == 'G':
#             check[i][j] = 2
#         else:
#             check[i][j] = 3

# for z in arr:
#     print(z)
print(cnt1, cnt2)