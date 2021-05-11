import sys
from collections import Counter


def check_max(array):
    a = [y for x in array for y in x]
    return max(a)


if __name__ == "__main__":
    # 큰 수 부터 좌표 구하기 (좌표의 의미는 지울 행이나 열)
    # 가장 큰 수의 좌표 와 K 번 아래로 작은 수 까지 비교.
    '''
    (col, row)
    if 
    8 = (0, 2), (3, 1)                 : 2
    7 = (2, 0)                         : 1
    6 = (3, 0), (1, 2)                 : 2
    5 = (1, 3)                         : 1
    4 = (1, 1), (2, 2), (4, 2)         : 3 
    3 = (0, 0), (0, 4), (1, 0), (0, 3) : 4
    .
    .

    '''

    n, m = map(int, sys.stdin.readline().split())
    k = int(sys.stdin.readline())
    row_col = dict()
    real_table = []
    max_val = 0

    for rdx in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        real_table.append(row)

        for cdx, c in enumerate(row):
            row_col.setdefault(c, [])
            row_col[c].append((cdx, rdx))
            max_val = max(max_val, c)

    for select in range(k):
        for coord in row_col[max_val]:
            print('')

    print('')
