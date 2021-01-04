a = int(input())
b = int(input())
c = int(input())

res = a*b*c
numList = [0]*10
res = str(res)

for i in res:
    numList[int(i)] += 1

for i in numList:
    print(i)