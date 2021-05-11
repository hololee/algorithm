import sys


def check(s1, s2):
    counter = dict()

    for w in s1:
        counter[w] = counter.setdefault(w, 0) + 1

    for w in s2:
        counter[w] = counter.setdefault(w, 0) - 1

    for item in counter.values():
        if item:
            return False
    return True


if __name__ == '__main__':
    str1: str = sys.stdin.readline()
    str2: str = sys.stdin.readline()

    print(check(str1, str2))
