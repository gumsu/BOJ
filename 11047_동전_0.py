n, k = map(int,input().split())

coinList = list()
for _ in range(n):
    coinList.append(int(input()))

coinList.sort(reverse=True)

cnt = 0
for i in coinList:
    if k // i >= 1:
        cnt += k // i
        k = k % i
print(cnt)