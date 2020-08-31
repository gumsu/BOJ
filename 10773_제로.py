import sys

num = int(sys.stdin.readline())
money_list = []
for i in range(num):
    money = int(sys.stdin.readline().rstrip())
    if money == 0 :
        money_list.pop()
    else:
        money_list.append(money)

print(sum(money_list))