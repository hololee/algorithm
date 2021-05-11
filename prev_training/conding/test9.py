import sys
from collections import defaultdict


def check_duplicate(s: str):
    spell_dic = defaultdict(int)

    for spell in s:
        spell_dic[spell] += 1

    for key, value in spell_dic.items():
        if value > 1:
            s = s.replace(key, "")

    return s


if __name__ == '__main__':
    word = sys.stdin.readline()

    removed = check_duplicate(word)
    print(removed)
