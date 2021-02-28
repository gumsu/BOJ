n = int(input())
arr = [-1 for _ in range(11)]
cnt = 0

for _ in range(n):
    a, b = map(int, input().split())
    if arr[a] == -1:
        arr[a] = b
    elif arr[a] != b:
        cnt += 1
        arr[a] = b
    print(arr, cnt)

print(cnt)