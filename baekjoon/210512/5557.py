import sys
from itertools import permutations

assign = [-1, 1]


def check(num_idx):
    global sum_num
    # num을 적용할때 넘어갈 수 있는지

    for ass in assign:
        sum_num += ass * dat[num_idx]
        check(num_idx + 1)

        # 가능한지.

    if


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    dat = list(map(int, sys.stdin.readline().replace('\n', '').split()))

    answer = dat[-1]

    sum_num = dat[0]
