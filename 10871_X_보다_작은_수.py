import sys

n, x = map(int,sys.stdin.readline().split())
num = [int(i) for i in sys.stdin.readline().split()]

def sol(x):
    for i in num:
        if x > i:
            print(i,end=' ')

sol(x)