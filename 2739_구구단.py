import sys

num= int(sys.stdin.readline())

def gugu(num):

    for i in range(1,10):
        print(num ,'*',i,'=',num*i,sep=' ')



gugu(num)