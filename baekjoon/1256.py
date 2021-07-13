# 210513

import sys
from itertools import permutations

if __name__ == '__main__':
    n, m, k = map(int, sys.stdin.readline().replace('\n', '').split())

    list_all = ['a'] * n + ['z'] * m
    word_all = list(map(''.join, sorted(set(permutations(list_all)))))

    if len(word_all) < k:
        print(-1)
    else:
        print(word_all[k - 1])
