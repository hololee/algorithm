# length = int(input())
#
# mcount = 0
#
#
# def check(position, last):
#     global mcount
#     if position != 0:
#         if last > 0: check(position - 1, last - 1)
#         if last < 9: check(position - 1, last + 1)
#     else:
#         mcount += 1
#
#
# for length in range(1, 9):
#     rect = []
#     for i in range(0, 10):
#         check(length - 1, i)
#         rect.append(mcount)
#
#         mcount = 0
#
#     print(rect)
#
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# # [1, 2, 2, 2, 2, 2, 2, 2, 2, 1]
# # [2, 3, 4, 4, 4, 4, 4, 4, 3, 2]
# # [3, 6, 7, 8, 8, 8, 8, 7, 6, 3]
# # [6, 10, 14, 15, 16, 16, 15, 14, 10, 6]
# # [10, 20, 25, 30, 31, 31, 30, 25, 20, 10]
# # [20, 35, 50, 56, 61, 61, 56, 50, 35, 20]
# # [35, 70, 91, 111, 117, 117, 111, 91, 70, 35]

import numpy as np

a_input = input()

left = len(a_input) % 3
if left != 0:
    a_input = '0' * (3 - left) + a_input

array = np.array(list(map(int, list(a_input))))
array = array.reshape([-1, 3])

a = list(zip(array[:, 0] * 4, array[:, 1] * 2, array[:, 2] * 1))
print(''.join(map(str, list(map(sum, a)))))