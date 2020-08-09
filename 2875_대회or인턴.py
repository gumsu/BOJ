import sys
n, m, k = map(int, sys.stdin.readline().split())

def sol(n,m,k):
    count = 0
    while n >= 2 and m >=1 and n+m >= k+3:
        n -= 2
        m -= 1
        count += 1
    print(count)


sol(n,m,k)