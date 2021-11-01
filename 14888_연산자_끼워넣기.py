from itertools import permutations

n = int(input())
num = list(map(int, input().split()))
# + - * /
operator_num = list(map(int, input().split()))
operator = ['+','-','*','/']
operator_list = []

# 연산자의 개수 만큼 리스트에 담기
for i in range(4):
    for j in range(operator_num[i]):
        operator_list.append(operator[i])

small = 1e9
big = -1e9

def cal(op):
    total = num[0]
    for i in range(len(op)):
        if op[i] == '+':
            total += num[i+1]
        elif op[i] == '-':
            total -= num[i+1]
        elif op[i] == '*':
            total *= num[i+1]
        elif op[i] == '/':
            total = int(total / num[i+1])
    return total
for case in permutations(operator_list, n-1) :
    # print(case[0], case[1], case[2], case[3], case[4])
    small = min(small, cal(case))
    big = max(big, cal(case))

print(big)
print(small)