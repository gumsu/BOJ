def DFS(idx, res, ch):
    if idx == m:                            # m=2이면, 두 번 다 뽑았으면 출력 후 리턴
        print(res)
        return
    for i in range(1, n+1):                 # 1부터 n까지 
        if not ch[i]:                       # 중복 방지(체크리스트에 False일 경우에만 실행)
            ch[i] = True                    # i번째 수를 뽑고 체크리스트에 True 저장
            DFS(idx+1, res+str(i)+' ', ch)  # idx+1 번째(다음수)에 i번째 뽑은 수와 함께 결과값, 체크리스트를 넘겨준다.
            ch[i] = False                   # 체크리스트의 i자리 True를 다시 False로 돌려주어야 함 


if __name__=="__main__":
    n, m = map(int, input().split())
    res = ""
    ch = [False for _ in range(n+1)]
    DFS(0, res, ch)