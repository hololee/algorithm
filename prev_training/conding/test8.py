import sys
from itertools import combinations_with_replacement
from collections import defaultdict


def check(S, n_faces=6):
    dic_sum = defaultdict(int)
    dic_list = defaultdict(list)

    for prob in combinations_with_replacement(range(1, n_faces + 1), 2):
        dic_sum[prob[0] + prob[1]] += 1
        dic_list[prob[0] + prob[1]].append(prob)

    return dic_sum[S], dic_list[S]


if __name__ == '__main__':

    dat = sys.stdin.readline()
    print(check(int(dat)))