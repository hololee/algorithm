# 201125

import sys

if __name__ == '__main__':
    first_line = sys.stdin.readline().split(' ')
    base_type = int(first_line[0])
    target_type = int(first_line[1])

    digits_base = int(sys.stdin.readline())

    position_val_base = [base_type**i for i in range(digits_base)]
    position_val_base.reverse()

    base_number = map(int, sys.stdin.readline().split(' '))

    for pos, one_digit in enumerate(base_number):
        position_val_base[pos] *= one_digit

    # sum.
    base_10_num = sum(position_val_base)

    # target num
    target_array = []

    remained = base_10_num
    while(remained >= target_type):
        # 나머지가 있다면.
        target_digit_val = remained % target_type
        remained = remained // target_type

        target_array.append(target_digit_val)

    if remained != 0:
        # 0이 아니면 더하기.
        target_array.append(remained)

    target_array.reverse()

    print(' '.join(map(str, target_array)))