# 파라메트릭 서치
# https://hbj0209.tistory.com/144
# https://kau-algorithm.tistory.com/136
n, m, l = map(int, input().split())
rest_area = list(map(int, input().split()))

# 도로의 시작과 끝 추가
rest_area.append(0)
rest_area.append(l)
rest_area.sort()

def Count(length):
    dist = 0
    for i in range(1, n+2):
        dist += (rest_area[i] - rest_area[i-1]-1)//length   # 나누어 떨어질 때 겹치므로
    return dist

lt, rt = 1, rest_area[-1]

while lt != rt:
    mid = (lt+rt) // 2

    if Count(mid) > m:
        lt = mid + 1
    else:
        rt = mid 
print(lt)
# print(*rest_area)