import sys
a, b = map(str, sys.stdin.readline().split())

a = a[::-1]
b = b[::-1]

if int(a) < int(b):
    print(b)
else:
    print(a)