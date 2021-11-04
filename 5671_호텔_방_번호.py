while True:
	try:
		n, m = map(int, input().split())
		cnt = 0
		for i in range(n, m+1):
			num = [0]*10
			tmp = str(i)
			for j in tmp:
				if num[int(j)] == 0:
					num[int(j)] += 1
				else:
					break
			else:
				cnt += 1
		print(cnt)
			
	except:
		break