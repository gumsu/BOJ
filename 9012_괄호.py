t = int(input())

for _ in range(t):
    ps = input()
    stack = list()

    for x in ps:
        if x == '(':
            stack.append(x)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(x)
    if not stack:
        print("YES")
    else:
        print("NO")