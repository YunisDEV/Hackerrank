# Enter your code here. Read input from STDIN. Print output to STDOUT
coord = list(map(int,input().split(' ')))

counter = 1
counterPlus = 2
for i in range(1,coord[0]+1):
    if i==coord[0]//2+1:
        hypenCount = (coord[1]-7)//2
        print("-"*hypenCount+'WELCOME'+"-"*hypenCount)
        counterPlus = -2
    else:
        hypenCount = (coord[1]-counter*3)//2
        print("-"*hypenCount+".|."*counter+"-"*hypenCount)
        if i==coord[0]//2: continue
        counter+=counterPlus
