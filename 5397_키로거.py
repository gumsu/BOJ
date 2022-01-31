t = int(input())
for _ in range(t):
    user = input()
    pw1 = []
    pw2 = []
    for i in user:
        if i == '-':
            if pw1:
                pw1.pop()
        elif i == '<':
            if pw1:
                pw2.append(pw1.pop())
        elif i == '>':
            if pw2:
                pw1.append(pw2.pop())
        else:
            pw1.append(i)
    if pw2:
        pw2.reverse()
    print(''.join(pw1+pw2))