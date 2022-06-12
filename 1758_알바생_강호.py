n = int(input())
people = [int(input()) for _ in range(n)]
people.sort(reverse=True)
res = 0
for i in range(n):
    if people[i]-i < 0 :
        continue
    res += people[i]-i
print(res)