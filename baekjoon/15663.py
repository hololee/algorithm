# 210512

import sys
from itertools import permutations

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().replace('\n', '').split())
    for i in sorted(set(permutations(map(int, sys.stdin.readline().replace('\n', '').split()), m))):
        print(*i)
