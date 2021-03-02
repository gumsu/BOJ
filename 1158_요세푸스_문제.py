n, k = map(int, input().split())
arr = list(range(1,n+1))
new = []
tmp = 0
while arr:
    # 현재 위치
    tmp += k-1
    if tmp >= len(arr):
        tmp %= len(arr)
    new.append(arr.pop(tmp))
print('<'+', '.join(map(str, new))+'>')