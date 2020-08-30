import sys

num= int(sys.stdin.readline())

def star(num):
    for i in range(1,num+1):
        print('*'*i)

star(num)