money = int(input())
machin_duck = list(map(int, input().split()))
jh_money = money
sm_money = money
jh_stock = 0
sm_stock = 0

# 준현
for i in machin_duck:
    if jh_money >= i:
        jh_stock += jh_money // i
        jh_money %= i

# 성민
for i in range(len(machin_duck)-3):
    # buy
    if machin_duck[i] > machin_duck[i+1] > machin_duck[i+2]:
        sm_stock += sm_money // machin_duck[i+3]
        sm_money = sm_money % machin_duck[i+3]
    # sell
    elif machin_duck[i] < machin_duck[i+1] < machin_duck[i+2]:
        sm_money += sm_stock * machin_duck[i+3]
        sm_stock = 0

jh_res = jh_money + machin_duck[-1] * jh_stock
sm_res = sm_money + machin_duck[-1] * sm_stock

if jh_res > sm_res:
    print("BNP")
elif jh_res < sm_res:
    print("TIMING")
else:
    print("SAMESAME")
# print(jh_res, sm_res)