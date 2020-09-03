import sys

def push(x):
    stack.append(x)
def pop():
    if not stack:
        return -1
    else:
        return stack.pop()
def size():
    return len(stack)
def empty():
    return 0 if stack else 1
def top():
    return stack[-1] if stack else -1

num = int(sys.stdin.readline().rstrip())
stack = []

for _ in range(num):
    x = sys.stdin.readline().rstrip().split()
    order = x[0]
    if order == "push":
        push(x[1])
    elif order == "pop":
        print(pop())
    elif order == "size":
        print(size())
    elif order == "empty":
        print(empty())
    else:
        print(top())