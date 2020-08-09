import sys

a= int(sys.stdin.readline())

def sol(a):

    count = 0
    coin = [500,100,50,10,5,1]
    change = 1000-a

    for i in coin:
        if change >= i:
            count += change//i
            change %= i
    
    print(count)

sol(a)