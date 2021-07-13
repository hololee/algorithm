# 210503

import sys

if __name__ == '__main__':

    sum_list = list()

    lines = int(sys.stdin.readline().replace('\n', ''))

    for i in range(lines):
        l, m, r = map(int, sys.stdin.readline().replace('\n', '').split())
        if i == 0:
            min_mat = [l, m, r]
            max_mat = [l, m, r]
        else:
            # l은 0, 1 m은 2, 3, 4, r은 5, 6

            # 작은 수만 선택.
            new_min_mat = [min(l + min_mat[0], l + min_mat[1])] + [min(m + min_mat[0], m + min_mat[1], m + min_mat[2])] + [min(r + min_mat[1], r + min_mat[2])]

            # 큰수 만 선택.
            new_max_mat = [max(l + max_mat[0], l + max_mat[1])] + [max(m + max_mat[0], m + max_mat[1], m + max_mat[2])] + [max(r + max_mat[1], r + max_mat[2])]

            min_mat, max_mat = new_min_mat, new_max_mat

    print(' '.join([str(max(max_mat)), str(min(min_mat))]))
