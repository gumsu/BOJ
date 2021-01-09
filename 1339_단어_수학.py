n = int(input())
words = [input() for _ in range(n)]

alpha = dict()
for word in words:
    length = len(word)

    for i in word:
        if i in alpha:
            alpha[i] += pow(10, length-1)
        else:
            alpha[i] = pow(10, length-1)
        length -= 1

alpha = sorted(alpha.items(), key=lambda x: x[1], reverse=True)

num = 9
res = 0
for key, values in alpha:
    res += values*num
    num -= 1
print(res)