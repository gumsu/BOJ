def DFS(level):
    # for z in com:
    #     print(z)
    # print()

    virus.append(level)
    check[level] = 1
    for i in range(1, n+1):
        if com[level][i] == 1 and check[i] == 0:
            com[level][i] = 0
            DFS(i)
n = int(input())
m = int(input())
com = [[0]*(n+1) for _ in range(n+1)]
check = [0]*(n+1)
virus = []

for i in range(m):
    x, y = map(int ,input().split())
    com[x][y] = com[y][x] = 1

# for z in com:
#     print(z)
# print()
DFS(1)
print(len(virus)-1)