n, m = map(int, input().split())
n_list = [input() for _ in range(n)]
m_list = [input() for _ in range(m)]
new = list(set(n_list) & set(m_list))
print(len(new))
new.sort()
for z in new:
    print(z)