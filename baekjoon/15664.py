# 210513

import sys
from itertools import combinations

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().replace('\n', '').split())
    all_nums = list(map(int, sys.stdin.readline().replace('\n', '').split()))

    outs = set()

    for i in combinations(all_nums, m):
        outs.add(tuple(sorted(i)))

    for n in sorted(list(outs)):
        print(*n)
