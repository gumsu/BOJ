num = [False]*100000

for i in range(1, 10001):
    if i < 10:
        tmp = i + i
        num[tmp] = True
    elif i < 100 :
        tmp1 = i // 10
        tmp2 = i % 10
        tmp = i + tmp1 + tmp2
        num[tmp] = True
    elif i < 1000 :
        tmp1 = i // 100
        tmp2 = (i-tmp1*100) // 10
        tmp3 = i-tmp1*100-tmp2*10
        tmp = i + tmp1 + tmp2 + tmp3
        num[tmp] = True
    elif i < 10000:
        tmp1 = i // 1000
        tmp2 = (i-tmp1*1000) // 100
        tmp3 = (i-tmp1*1000-tmp2*100) // 10
        tmp4 = i-tmp1*1000-tmp2*100-tmp3*10
        tmp = i + tmp1 + tmp2 + tmp3 + tmp4
        num[tmp] = True

for i in range(1, 10000):
    if not num[i]:
        print(i)