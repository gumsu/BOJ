n = int(input())

cnt = 0
# 1의자리 / 10의자리 / 100의자리
for i in range(1, n+1):
    if i < 10:
        cnt += 1
    elif i < 100:
        cnt += 1
    elif i < 1000:
        tmp1 = i//100
        tmp2 = (i-tmp1*100)//10
        tmp3 = (i-tmp1*100-tmp2*10)
        #print(tmp1, tmp2, tmp3)
        if tmp2 - tmp1 == tmp3 - tmp2:
            cnt += 1
print(cnt)