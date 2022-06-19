n = int(input())
switch = list(map(int, input().split()))
students = int(input())
for i in range(students):
    # 남 1, 여 2, 켜 1, 꺼 0
    gender, num = map(int, input().split())
    
    if gender == 1:
        temp = n // num # 8 나누기 3 은 2
        for j in range(1, temp+1):
            # switch[j*num-1] = 1 if switch[j*num-1] == 0 else switch[j*num-1] = 0
            if switch[j*num-1] == 0:
                switch[j*num-1] = 1
            else:
                switch[j*num-1] = 0
    else:
        # 무조건 선택한 숫자는 바꾸기
        # switch[num-1] = 1 if switch[num-1] == 0 else switch[num-1] = 0
        if switch[num-1] == 0 :
            switch[num-1] = 1
        else:
            switch[num-1] = 0
        
        left = num-2
        right = num
        while left >= 0 and right < n and switch[left] == switch[right]:
            if switch[left] == 0:
                switch[left], switch[right] = 1, 1
            elif switch[left] == 1:
                switch[left], switch[right] = 0, 0
            left -= 1
            right += 1
cnt = 0
res = ""
for i in range(n):
    res += str(switch[i]) + " "
    cnt += 1
    if cnt == 20:
        print(res)
        res = ""
        cnt = 0
if len(res) != 0:
    print(res)