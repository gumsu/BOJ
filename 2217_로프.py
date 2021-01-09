n = int(input())
rope = [int(input()) for _ in range(n)]

rope.sort(reverse=True)

heavy = max(rope)
for i in range(n):
    if heavy <= rope[i]*(i+1):
        heavy = rope[i]*(i+1)

print(heavy)