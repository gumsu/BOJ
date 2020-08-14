import sys
n = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))
num1 = max(num)
num2 = min(num)
print(num2,num1,sep=' ')