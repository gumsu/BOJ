import sys

x, y, w, s = map(int, sys.stdin.readline().split())

# 대각선으로 가는게 더 손해일 경우: only 평행선으로만 움직인다
if w*2 <= s:
    answer = (x+y) * w
# 대각선으로 최대한 움직인 후에 나머지 길을 평행선으로 가는 경우
else:
    answer = min(x,y)*s + abs(x-y)*w
# 대각선으로만 가는 경우

    # 대각선으로만 가는 경우: x+y가 짝수인 경우
    if (x + y) % 2 == 0 :
        answer = min(answer, max(x,y)*s)
    # 대각선으로만 가는 경우: x+y가 홀수인 경우
    else:
        answer = min(answer, (max(x,y)-1)*s + w)

print(answer)