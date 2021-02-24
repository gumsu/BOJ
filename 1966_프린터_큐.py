t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    doc = list(map(int,input().split()))
    idx = list(range(len(doc)))
    idx[m] = 'target'
    
    cnt = 0

    while True:
        max_num = max(doc)
        tmp = doc.pop(0)
        tmp_idx = idx.pop(0)

        if max_num != tmp:
            doc.append(tmp)
            idx.append(tmp_idx)
        else:
            cnt += 1
            if tmp_idx == 'target':
                break
    print(cnt)