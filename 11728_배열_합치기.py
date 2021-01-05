n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

p1 = p2 = 0
new = list()

while p1 < n and p2 < m:
    if a[p1] < b[p2]:
        new.append(a[p1])
        p1 += 1
    else:
        new.append(b[p2])
        p2 += 1
    
if p1 < n:
    new = new + a[p1:]
else:
    new = new + b[p2:]

print(*new)