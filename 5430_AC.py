from collections import deque

t = int(input())
for _ in range(t):
    p = input()
    n = int(input())
    arr = eval(input())
    arr = deque(arr)

    p = p.replace('RR','')

    flag = False

    for i in p:
        if i == 'R':
            if flag == True:
                flag = False
            else:
                flag = True
        else:
            if not arr:
                print('error')
                break
            if flag == True:
                arr.pop()
            else:
                arr.popleft()
    else:
        if flag == True:
            arr.reverse()
        print('['+','.join(map(str,arr))+']')