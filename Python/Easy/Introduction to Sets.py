def average(array):
    Sum = 0
    SET = set(array)
    for i in SET:
        Sum+=i
    return Sum/len(SET)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)