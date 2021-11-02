from itertools import combinations

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
min_num = 1e9

# 팀 나누기
n_arr = list(range(n))
for z in combinations(n_arr, n//2):
    start_team = list(z)
    link_team = list(set(n_arr) - set(start_team))
   # print(start_team, link_team)

   # 2명씩 비교하기 위해 분리
    start_combi = list(combinations(start_team, 2))
    link_combi = list(combinations(link_team, 2))

   #print(start_combi, link_combi)

    start_num = 0
    link_num = 0
    for x, y in start_combi:
       # print(x, y)
        start_num += (s[x][y] + s[y][x])
    for x, y in link_combi:
        link_num += (s[x][y] + s[y][x])
        
    if abs(start_num-link_num) < min_num:
        min_num = min(min_num, abs(start_num-link_num))

print(min_num)