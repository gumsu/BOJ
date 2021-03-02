n, m = map(int, input().split())
program = dict()
for _ in range(n):
    site, pw = input().split()
    program[site] = pw

for _ in range(m):
    a = input()
    print(program[a])