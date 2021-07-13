# 210427

from collections import Counter
import sys

if __name__ == '__main__':
    check_list = Counter()
    validate_list = []

    n = int(sys.stdin.readline())

    for dat in map(int, sys.stdin.readline().split()):
        check_list[dat] += 1

    m = int(sys.stdin.readline())

    for dat in map(int, sys.stdin.readline().split()):
        if dat in check_list.keys():
            validate_list.append(1)
        else:
            validate_list.append(0)

    for v in validate_list:
        print(v)