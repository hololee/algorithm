import sys
from operator import itemgetter

if __name__ == '__main__':
    n_case = int(sys.stdin.readline().replace('\n', ''))

    for i_case in range(n_case):
        n_people = int(sys.stdin.readline().replace('\n', ''))

        # all grade.
        grades = []

        for i_people in range(n_people):
            grades.append(tuple(map(int, sys.stdin.readline().replace('\n', '').split(' '))))

        # sort.
        grades.sort(key=itemgetter(0))

        min_grade = n_people
        can_get = 0
        for grade in grades:
            if grade[1] <= min_grade:
                can_get += 1
                min_grade = grade[1]
        print(can_get)
