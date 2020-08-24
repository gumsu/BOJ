import sys

l = []
for _ in range(9):
    num = int(sys.stdin.readline())
    l.append(num)
print(max(l),l.index(max(l))+1,sep='\n')