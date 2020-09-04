import textwrap

def wrap(string, max_width):
    last_part = len(string)%max_width
    arr = []
    temp = ""
    counter = 0
    for i in string:
        temp+=str(i)
        if counter%max_width==max_width-1 and counter>0:
            arr.append(temp)
            temp=""
        counter+=1
    for i in arr:
        print(i)
    return string[-last_part:]

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)