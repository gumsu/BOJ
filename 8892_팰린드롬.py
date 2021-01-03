t = int(input())

def isPalindrome(word):
    reversedWord = ''.join(reversed(word))
    if reversedWord == word:
        return True
    else:
        return False

for i in range(t):
    num = int(input())
    arr = [input() for _ in range(num)]

    word = ""
    flag = False

    for x in range(len(arr)):
        for y in range(x+1, len(arr)):
            word = arr[x] + arr[y]
            flag = isPalindrome(word)
            if flag:
                print(word)
                break
            word = arr[y] + arr[x]
            flag = isPalindrome(word)
            if flag:
                print(word)
                break
        if flag:
            break
    else:
        print(0)