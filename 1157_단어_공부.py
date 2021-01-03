word = input()

word = word.upper()
wordDict = dict()

for i in word:
    if i in wordDict:
        wordDict[i] += 1
    else:
        wordDict[i] = 1

maxValues = max(wordDict.values())
res = list()

for word, num in wordDict.items():
    if num == maxValues:
        res.append(word)
    if len(res) > 1:
        print('?')
        break
else:
    print(res[0])