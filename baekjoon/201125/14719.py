import sys


def check_conditions(remained):

    # remove zeros.
    while(remained[0] == 0):
        remained = remained[1:]
    while(remained[-1] == 0):
        remained = remained[:-1]

    return remained.count(0)


if __name__ == '__main__':
    box_size = list(map(int, sys.stdin.readline().split()))
    remain_levels = list(map(int, sys.stdin.readline().split()))

    sum_of_rain_region = 0

    while(sum(remain_levels) != 0):

        # remain_levels 에서 하나씩 빼서 리스트를 만듬.
        one_line = []

        for pos, remain in enumerate(remain_levels):
            if remain > 0:
                one_line.append(1)
                remain_levels[pos] -= 1
            else:
                one_line.append(0)

        sum_of_rain_region += check_conditions(one_line)

    print(sum_of_rain_region)
