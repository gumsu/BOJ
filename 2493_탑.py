n = int(input())
top = list(map(int, input().split()))
arr = []
stack = []

for i in range(n):
    while stack:
        if stack[-1][1] > top[i]:
            arr.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()

    if not stack:
        arr.append(0)
    stack.append((i, top[i]))
    # print(stack, arr)
print(' '.join(map(str, arr)))