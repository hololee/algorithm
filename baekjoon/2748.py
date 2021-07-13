# 210503

import sys


def find_number(n):
    if n < 2:
        return n
    else:
        prev_dat = 0
        sum_dat = 1
        for i in range(n-1):
            new_sum_dat = prev_dat+sum_dat
            prev_dat = sum_dat
            sum_dat = new_sum_dat
        return sum_dat


if __name__ == "__main__":

    num = int(sys.stdin.readline())
    print(find_number(num))
