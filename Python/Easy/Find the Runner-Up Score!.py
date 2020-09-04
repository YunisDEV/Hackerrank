if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    first_item=arr[0]
    for i in arr:
        if i!=first_item:
            print(i)
            break
