a, b = map(int, input().split())

cnt = 0
arr = [0]
while len(arr) < 1000:
    tmp = [cnt] * cnt
    arr = arr + tmp
    cnt += 1

arr = arr[a:b+1]
print(sum(arr))