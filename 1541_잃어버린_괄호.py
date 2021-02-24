solv = input().split('-')

total = 0
tmp = solv.pop(0)
for i in tmp.split('+'):
    total += int(i)
        
for i in solv:
    tmp = i.split('+')
    for j in tmp:
        total -= int(j)

print(total)