n = 0
while True:
    user = list(map(int,input().split()))
    n = user.pop(0)
    
    if n == 0:
        break
    
    numList = list()

    for i in range(len(user)):
        for j in range(i+1, len(user)):
            if user[i] == user[i+1]:
                user.pop(i+1)
    
    for i in user:
        print(i , end=' ')
    print('$')