n = int(input())
myCard = list(map(int, input().split()))
m = int(input())
cardList = list(map(int, input().split()))

myCard.sort()

res = [0]*m

for i in range(m):
    lt = 0
    rt = n-1

    while lt <= rt :
        mid = (lt + rt) // 2
        
        if myCard[mid] == cardList[i]:
            res[i] = 1
            break
        elif myCard[mid] < cardList[i]:
            lt = mid + 1
        else:
            rt = mid - 1
print(*res)