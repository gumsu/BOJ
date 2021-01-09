n = int(input())
person = list(map(int, input().split()))

person.sort()

total = 0
for i in range(n):
    total += person[i]*(n-i)

print(total)