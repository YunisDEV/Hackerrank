from collections import Counter
input()
shoesList = input().split(' ')
catalog = dict(Counter(shoesList))
todaySum = 0
for _ in range(int(input())):
    stdin = input().split(' ')
    if stdin[0] in catalog:
        if catalog[stdin[0]]>0:
            todaySum+=int(stdin[1])
            catalog[stdin[0]]-=1

print(todaySum)
