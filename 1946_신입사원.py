t = int(input())

for i in range(t):
    n = int(input())
    applicants = [tuple(map(int, input().split())) for _ in range(n)]

    applicants.sort(key=lambda x: x[0])

    cnt = 0
    tmp = 2417000000
    for grade, rank in applicants:
        if rank < tmp:
            cnt += 1
            tmp = rank
    print(cnt)