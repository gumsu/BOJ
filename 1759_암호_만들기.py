def DFS(password, index):
    if len(password) == l:
        vowelsCnt = 0
        consonantCnt = 0
        for a in password:
            if a in vowels:
                vowelsCnt += 1
            else:
                consonantCnt += 1
        if vowelsCnt >= 1 and consonantCnt >= 2:
            print(password)
            return
    if index >= c:
        return
    DFS(password+str(alpha[index]), index+1)
    DFS(password, index+1)

l, c = map(int, input().split())
alpha = list(input().split())
vowels = ['a','i','u','o','e']

alpha.sort()
DFS("", 0)