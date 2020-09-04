K = int(input())

l = list(map(int,input().split(" ")))
s = set(l)

sumOFlist = sum(l)
sumOFset = sum(s)

print(((sumOFset*K)-(sumOFlist))//(K-1))