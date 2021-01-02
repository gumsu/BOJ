num = int(input())
count = 0

num -=1
count +=1
while num != 1:
    if num % 3 == 0:
        num = num / 3
        count += 1
    elif num % 2 == 0:
        num = num / 2
        count += 1

print(count)