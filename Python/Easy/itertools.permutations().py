from itertools import permutations

string,k = input().split(' ')
perms = []
for i in permutations(list(string),int(k)):
    perms.append("".join(i))

perms.sort()

for i in perms:
    print(i)
