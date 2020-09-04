for _ in range(int(input())):
    x,a,y,b = input(), set(input().split()), input(), set(input().split())
    print(a.issubset(b))