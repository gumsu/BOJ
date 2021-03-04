n = int(input())
arr = []
for _ in range(n):
    tmp = input()
    arr.append((tmp, len(tmp)))

arr = list(set(arr))
arr.sort(key=lambda x: (x[1], x[0]))

for z, idx in arr:
    print(z)