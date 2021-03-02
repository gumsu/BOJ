n = int(input())
state = dict()

for _ in range(n):
    name, now = input().split()
    state[name] = now

tmp = []
for name, state in state.items():
    if state == 'enter':
        tmp.append(name)

tmp.sort(reverse=True)
for z in tmp:
    print(z)