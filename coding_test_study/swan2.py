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


def reduce_area(array, row, col, targets):
    map = deepcopy(array)
    melting_positions = set()  # 자리가 중복되는 경우 지우기.

    # 타켓이 없는경우.
    if not targets:
        for i in range(row):
            for j in range(col):
                # 얼음인 경우만 동작.
                if map[i][j] == '.':
                    # 4방향 체크.
                    # print(i, j)
                    if i > 0 and map[i - 1][j] == 'X':  # 상
                        melting_positions.add((i - 1, j))
                    if i < (row - 1) and map[i + 1][j] == 'X':  # 하
                        melting_positions.add((i + 1, j))
                    if j > 0 and map[i][j - 1] == '#':  # 좌
                        melting_positions.add((i, j - 1))
                    if j < (col - 1) and map[i][j + 1] == 'X':  # 우
                        melting_positions.add((i, j + 1))

    # 타켓 (전에 사라진 얼음들) 이 있는경우.
    else:
        for target in targets:
            i = target[0]
            j = target[1]
            if map[i][j] == '.':
                # 4방향 체크.
                # print(i, j)
                if i > 0 and map[i - 1][j] == 'X':  # 상
                    melting_positions.add((i - 1, j))
                if i < (row - 1) and map[i + 1][j] == 'X':  # 하
                    melting_positions.add((i + 1, j))
                if j > 0 and map[i][j - 1] == 'X':  # 좌
                    melting_positions.add((i, j - 1))
                if j < (col - 1) and map[i][j + 1] == 'X':  # 우
                    melting_positions.add((i, j + 1))

    for pos in melting_positions:
        map[pos[0]][pos[1]] = '.'

    return map, melting_positions


def is_reach(positions, array, row, col):
    check_positions = set()
    ice_in_path = set()

    check_que = Queue()
    check_que.put(positions[0])

    # 모든 가능한 길 탐색
    while not check_que.empty():
        tar_pos = check_que.get()
        check_positions.add((tar_pos[0], tar_pos[1]))

        # 탐색 중 얼음으로 못갔던 부분을 따로 저장, TODO: 나중에 해당 지점부터 다시 시작.
        can_go, ice_pos = get_adj(tar_pos, array, row, col)
        ice_in_path.add(*ice_pos)

        for adj_positions in can_go:
            if (adj_positions[0], adj_positions[1]) not in check_positions:
                check_que.put(adj_positions)

    # 갔던 길에 다른 swan 이 포함 되는지 체크
    if (positions[1][0], positions[1][1]) in check_positions:
        return True, check_positions, ice_in_path
    else:
        return False, check_positions, ice_in_path


def get_adj(position, array, row, col):
    # 상하좌우 이동 가능한 공간.
    can_go = []
    ice_pos = []
    x, y = position[0], position[1]
    if x > 0:
        if array[x - 1][y] == '.':  # 상
            can_go.append([x - 1, y])
        else:
            ice_pos.append([x - 1, y])
    if x < (row - 1):
        if array[x + 1][y] == '.':  # 하
            can_go.append([x + 1, y])
        else:
            ice_pos.append([x + 1, y])
    if y > 0:
        if array[x][y - 1] == '.':  # 좌
            can_go.append([x, y - 1])
        else:
            ice_pos.append([x, y - 1])
    if y < (col - 1):
        if array[x][y + 1] == '.':  # 우
            can_go.append([x, y + 1])
        else:
            ice_pos.append([x, y + 1])
    return can_go, ice_pos


R, C = list(map(int, sys.stdin.readline().split()))

lake = []
for i in range(R):
    lake.append(list(sys.stdin.readline().replace("\n", "")))

lake, swan_position = find_swan(lake, R, C)
meet = False
days = 0

target = None
check_positions = set()
ice_in_path = set()

while not meet:
    # check meet
    meet, check_positions, ice_in_path = is_reach(swan_position, lake, R, C)
    if meet:
        print(days)
    else:
        #  1. 기존 각 branch 의 마지막 가지에서 부터 탐색을 출발한는건 어떤지? (얼음을 지운 이후에 이전 stage 의 각 branch의 마지막 지점들 부터 탐색 시작.)
        #  2. 아니면 can_go 가 아닌 위치들만 모아서 해당 부분부터 탐색을 진행하는것은?(기존 check_positions는 유지.)
        #  3. melting_positions 근처 얼음을 지우고 기존 check_position은 유지하고 melting_positions 로 부터 탐색을 시작하는것은?
        # TODO: 4. 기존 check_position은 유지하고 BFS 중 만나는 얼음들의 위치 부터 탐색을 시작 하는것은?
        lake, target = reduce_area(lake, R, C, target)
        print("")
    days += 1
