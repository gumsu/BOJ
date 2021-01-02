import sys

num = sys.stdin.readline().rstrip()
nlist = list()
idx = 0
for i in num:
    nlist.append(int(num[idx]))
    idx += 1
nlist.sort(reverse=True)
for i in range(len(nlist)): print(nlist[i],end='')