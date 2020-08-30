import sys

a= int(sys.stdin.readline())

def sol(a):
    for i in range(1,a+1):
        print(' '*(a-i)+'*'*i)

sol(a)