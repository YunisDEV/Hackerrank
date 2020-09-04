from itertools import product

A = map(int,input().split(' '))
B = map(int,input().split(' '))

AxB = list(product(A,B))
out = ""
# for i in AxB:
#     out+=str(i)+" "
# for

print(*AxB)
