input()
A = set(map(int,input().split(' ')))
for _ in range(int(input())):
    getattr(A,input().split(' ')[0])(set(map(int,input().split(' '))))
print(sum(A))