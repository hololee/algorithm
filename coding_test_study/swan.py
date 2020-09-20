import sys
from queue import Queue
from copy import deepcopy


def find_swan(array, row, col):
    positions = []
    for i in range(row):
        for j in range(col):
            if array[i][j] == 'L':
                positions.append((i, j))
                array[i][j] = '.'

    return array, positions


def reduce_area(array, row, col):
    map = deepcopy(array)
    check_positions = set()  # 자리가 중복되는 경우 지우기.

    for i in range(row):
        for j in range(col):
            # 얼음인 경우만 동작.
            if map[i][j] == 'X':
                # 4방향 체크.
                # print(i, j)
                if i > 0 and map[i - 1][j] == '.':  # 상
                    check_positions.add((i, j))
                if i < (row - 1) and map[i + 1][j] == '.':  # 하
                    check_positions.add((i, j))
                if j > 0 and map[i][j - 1] == '.':  # 좌
                    check_positions.add((i, j))
                if j < (col - 1) and map[i][j + 1] == '.':  # 우
                    check_positions.add((i, j))

    for pos in check_positions:
        map[pos[0]][pos[1]] = '.'

    # TODO: 없어졌던 녀석들의 주변을 지우는건?

    return map


def is_reach(positions, array, row, col):
    check_positions = set()

    check_que = Queue()
    check_que.put(positions[0])

    # 모든 가능한 길 탐색
    while not check_que.empty():
        tar_pos = check_que.get()
        check_positions.add((tar_pos[0], tar_pos[1]))
        for adj_positions in get_adj(tar_pos, array, row, col):
            if (adj_positions[0], adj_positions[1]) not in check_positions:
                check_que.put(adj_positions)

    # 갔던 길에 다른 swan 이 포함 되는지 체크
    if (positions[1][0], positions[1][1]) in check_positions:
        return True
    else:
        return False


def get_adj(position, array, row, col):
    # 상하좌우 이동 가능한 공간.
    can_go = []
    x, y = position[0], position[1]
    if x > 0 and array[x - 1][y] == '.':  # 상
        can_go.append([x - 1, y])
    if x < (row - 1) and array[x + 1][y] == '.':  # 하
        can_go.append([x + 1, y])
    if y > 0 and array[x][y - 1] == '.':  # 좌
        can_go.append([x, y - 1])
    if y < (col - 1) and array[x][y + 1] == '.':  # 우
        can_go.append([x, y + 1])
    return can_go


R, C = list(map(int, sys.stdin.readline().split()))

lake = []
for i in range(R):
    lake.append(list(sys.stdin.readline().replace("\n", "")))

lake, swan_position = find_swan(lake, R, C)
meet = False
days = 0

while not meet:
    # check meet
    meet = is_reach(swan_position, lake, R, C)
    if meet:
        print(days)
    else:
        lake = reduce_area(lake, R, C)
    days += 1
