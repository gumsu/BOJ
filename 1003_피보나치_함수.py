t = int(input())
for _ in range(t):
    n = int(input())
    dp_zero = [1, 0]
    dp_one = [0, 1]

    for i in range(2, n+1):
        dp_zero.append(dp_zero[i-2]+dp_zero[i-1])
        dp_one.append(dp_one[i-2]+dp_one[i-1])
    print(dp_zero[n], dp_one[n], sep=' ')