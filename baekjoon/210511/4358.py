import sys
from collections import Counter

if __name__ == '__main__':
    spec_list = Counter()
    count = 0
    while 1:
        dat = sys.stdin.readline().replace('\n', '')
        if dat:
            spec_list[dat] += 1
            count += 1
        else:
            break

    for i in sorted(spec_list.keys()):
        print(i, '%.4f' % round(spec_list[i] * 100 / count, 4))
