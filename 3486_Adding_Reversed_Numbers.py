import sys
n = int(sys.stdin.readline())

for i in range(n):
    a, b = map(str, sys.stdin.readline().split())
    a = a[::-1]
    b = b[::-1]
    sum = str(int(a)+int(b))
    sum = sum[::-1]
    print(int(sum))
