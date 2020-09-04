if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    arrSum = 0
    for i in student_marks[query_name]:
        arrSum+=i
    print('{0:.{1}f}'.format(arrSum/3,2))
