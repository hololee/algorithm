import sys
from collections import defaultdict, deque

if __name__ == '__main__':
    n = int(sys.stdin.readline())

    candidates = deque([i for i in range(10)][::-1])

    order_annotation = defaultdict(int)

    all_number = []

    for i in range(n):
        dat = sys.stdin.readline().replace('\n', '')

        # 수 추가.
        all_number.append(dat)
        for pdx, p in enumerate(dat[::-1]):
            order_annotation[p] += 10 ** pdx

    n_numbers = len(all_number)

    for key in dict(sorted(order_annotation.items(), key=lambda x: x[1], reverse=True)).keys():
        candidate = candidates.popleft()
        for ndx in range(n_numbers):
            all_number[ndx] = all_number[ndx].replace(key, str(candidate))

    print(sum(map(int, all_number)))