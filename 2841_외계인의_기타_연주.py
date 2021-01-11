n, p = map(int, input().split())

stack = [[] for _ in range(7)]
cnt = 0

for _ in range(n):
    idx, val = map(int, input().split())
    if not stack[idx]:              # 빈 배열이라면 그냥 추가
        stack[idx].append(val)
        cnt += 1
    else:                           # 빈 배열이 아니라면
        current = stack[idx][-1]    # top
        if current == val:
            continue
        elif current > val:         # top 보다 프렛이 작다면 배열에서 제거한 후 프렛 추가
            while stack[idx] and stack[idx][-1] > val:
                stack[idx].pop()
                cnt += 1
            if stack[idx] and stack[idx][-1] == val:
                continue
            stack[idx].append(val)
            cnt += 1
        elif current < val:
            stack[idx].append(val)
            cnt += 1
print(cnt)