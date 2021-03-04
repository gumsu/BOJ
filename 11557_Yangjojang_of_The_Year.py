t = int(input())

for _ in range(t):

    dic = dict()
    n = int(input())

    for _ in range(n):
        key, val = input().split()
        dic[key] = int(val)
    
    for k, v in dic.items():
        if v == max(dic.values()):
            print(k)