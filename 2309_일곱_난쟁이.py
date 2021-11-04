from itertools import permutations

people = []
for _ in range(9):
    people.append(int(input()))

for i in permutations(people, 7):
    if sum(i) == 100:
        tmp = sorted(list(i))
        for z in tmp:
            print(z)
        break