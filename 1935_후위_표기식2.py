n = int(input())
expression = input()
num = [[]]
stack = list()

for i in range(1, n+1):
    num.append([])
    num[i].append(chr(64+i))
    tmp = int(input())
    num[i].append(tmp)

for j in expression:
    if j.isalpha():         # 알파벳은 다 넣는다. (넣기전 숫자로 변형)
        transfer = [num[x][1] for x in range(1, len(num)) if num[x][0] == j] # 숫자로 변형
        stack.append(transfer[0])
    else:                   # 연산자라면
        if len(stack) != 1:
            tmp1 = stack.pop()  # 두 번째 수
            tmp2 = stack.pop()  # 첫 번째 수

            if j == '*':
                stack.append(tmp2*tmp1)
            elif j == '/':
                stack.append(tmp2/tmp1)
            elif j == '+':
                stack.append(tmp2+tmp1)
            elif j == '-':
                stack.append(tmp2-tmp1)
print(f'{stack[0]:.2f}')   # 소수점 둘째 자리까지 출력