if __name__ == '__main__':
    numArr = []
    fullArr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        numArr.append(score)
        fullArr.append([name,score])
    numArr.sort()
    first = numArr[0]
    validAnswer=0
    for i in numArr:
        if i !=first:
            validAnswer = i
            break
    resultArr = []
    for x,y in fullArr:
        if y == validAnswer:
            resultArr.append(x)
    resultArr.sort()
    for i in resultArr:
        print(i)
