def mutate_string(string, position, character):
    result = ''
    index=0
    for i in string:
        if index==position:
            result+=character
        else:
            result+=i
        index+=1
    return result

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)