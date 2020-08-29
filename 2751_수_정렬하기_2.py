import sys

num = int(sys.stdin.readline())
nlist = []
for i in range(num):
    nlist.append(int(sys.stdin.readline().rstrip()))

nlist.sort()
for i in nlist: print(i)