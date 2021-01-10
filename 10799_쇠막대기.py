sp = input()

stack = list()
cnt = 0

for i in range(len(sp)):
    if sp[i] == '(':
        stack.append(i)
    else:   # ) 일 때
        stack.pop()
        if sp[i-1] == '(':  # 바로 앞에 ( 일때 -> 레이저
            cnt += len(stack)
        else:   # 바로 앞에 ) 일 때
            cnt += 1    # 막대기 마지막 부분 카운트
print(cnt)