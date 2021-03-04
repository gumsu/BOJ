scores = list()
for i in range(8):
    scores.append(int(input()))

res = list()
idxList = list()
idx = 0
for i in range(5):
    res.append(max(scores))
    idx = scores.index(max(scores))
    idxList.append(idx+1)
    scores[idx] = 0

idxList.sort()
print(sum(res))
print(*idxList)