K = int(input())

l = list(map(int,input().split(" ")))
s = set(l)

sumOFlist = sum(l)
sumOFset = sum(s)

bonusCapitanNos = (sumOFset*K)-sumOFlist

print(bonusCapitanNos//(K-1))