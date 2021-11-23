n = int(input())
arr = [[1e9]*n for _ in range(n)]
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1 :
        break
    a -= 1
    b -= 1
    arr[a][b] = arr[b][a] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j :
                arr[i][j] = 0
            elif arr[i][j] > arr[i][k] + arr[k][j]:
                 arr[i][j] = arr[i][k] + arr[k][j]

person = [0] * n

for i in range(n):
    person[i] = max(arr[i])
#print(person)
print(min(person), person.count(min(person)))
for i in range(len(person)):
    if person[i] == min(person):
        print(i+1, end=' ')