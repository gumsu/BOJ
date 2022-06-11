n = int(input())
cnt = 0
# n이 5의 배수인가? 5원짜리로만
# n이 5의 배수가 아닌 경우 -2

while n != 0:
    if n % 5 == 0:
        cnt += n//5
        break
    else:
        n -= 2
        cnt += 1
    if n < 0:
        cnt = -1
        break
print(cnt)