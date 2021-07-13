# 200917

from copy import deepcopy


def check_same_array(array1, array2):
    stack = []
    for idx, i in enumerate(array1):
        if i == array2[idx]:
            stack.append(1)
        else:
            stack.append(0)
    if sum(stack) == len(array1):
        return True
    else:
        return False


def logical_or(array1, array2):
    stack = []

    for idx, i in enumerate(array1):
        if (i == '#') or (array2[idx] == '#'):
            stack.append('#')
        else:
            stack.append('.')
    return ''.join(stack)


def cal_multiply(array):
    multiply = 1
    for i in array:
        multiply *= i
    return multiply


all_num = ['' for i in range(10)]
# .replace('#', '1').replace('.', '0')
all_num_list = ['###...#.###.###.#.#.###.###.###.###.###',
                '#.#...#...#...#.#.#.#...#.....#.#.#.#.#',
                '#.#...#.###.###.###.###.###...#.###.###',
                '#.#...#.#.....#...#...#.#.#...#.#.#...#',
                '###...#.###.###...#.###.###...#.###.###']

for i in range(10):
    for j in range(len(all_num_list)):
        all_num[i] += (all_num_list[j][i * 4:  i * 4 + 3])

# all _num : target_feature.

size = 0
test_num_list = []

for i in range(6):
    if i == 0:
        size = int(input())
    else:
        test_num_list.append(input())

test_num = ['' for i in range(size)]

for i in range(size):
    for j in range(len(test_num_list)):
        test_num[i] += (test_num_list[j][i * 4:  i * 4 + 3])

# all_num = (10 ,feature_size) : 0~ 9까지 숫자들
# test_num = (N ,feature_size) : 입력값.

check_position = [[] for i in range(len(test_num))]

for idx, i in enumerate(test_num):
    for jdx, j in enumerate(all_num):
        if check_same_array(logical_or(i, j), j):
            check_position[idx].append(str(jdx))

can_be_number = []
sum_possible = 1
for i in check_position:
    can_be_number.append(len(i))
    sum_possible *= len(i)

if sum_possible == 0:
    print(-1)
else:
    sum_n = 0
    positions = len(check_position)
    # 각 자리수 별 모든 합. 뒤만 계산?
    for i in range(positions):
        copied = deepcopy(can_be_number)
        copied.pop(i)
        sum_n += sum(map(int, check_position[i])) * cal_multiply(copied) * 10 ** (positions - 1 - i)

    print(sum_n / sum_possible)
