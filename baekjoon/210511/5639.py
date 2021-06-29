import sys
import bisect

sys.setrecursionlimit(20000)


def arrange2post(start_idx, end_idx):
    # post order로 정렬된 결과를 반환.
    if start_idx >= end_idx:
        # 스타트가 뒤에 있으면 빈 행렬 반환. -> 오류발생.
        return

    root = pre_order[start_idx:end_idx][0]
    index = bisect.bisect_left(pre_order[start_idx + 1: end_idx], root)

    # left
    arrange2post(start_idx + 1, start_idx + 1 + index)
    # right
    arrange2post(start_idx + 1 + index, end_idx)
    print(root)


if __name__ == '__main__':
    pre_order = list()
    while 1:
        try:
            read = sys.stdin.readline()
            pre_order.append(int(read.replace('\n', '')))
        except:
            break

    arrange2post(0, len(pre_order))
