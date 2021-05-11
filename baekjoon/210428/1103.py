import sys


def four_way(coord, distance):
    return (coord[0] - distance, coord[1]), (coord[0] + distance, coord[1]), (coord[0], coord[1] - distance), (coord[0], coord[1] + distance)


def check_move_count(moved_coord):
    # 이동점에서 최대 이동 가능 거리를 출력.
    global marking_map, counting_map

    if is_outside_hole(moved_coord):
        return 0
    # 방문 체크.
    elif marking_map[moved_coord[0]][moved_coord[1]] == 1:
        print(-1)
        exit()
    elif counting_map[moved_coord[0]][moved_coord[1]] != 0:
        return counting_map[moved_coord[0]][moved_coord[1]]
    else:
        # # 정방향
        # 다음위치에서 돌아올 수 있으므로 이미 방문으로 변경,
        marking_map[moved_coord[0]][moved_coord[1]] = 1
        # 최대 가능 거리 최신화.
        # 4방향으로 이동하여 각 새로운 지점에서 마지막 이동 가능 지점 까지
        # 최대 거리를 리턴 받아 현재 위치의 값과 비교하여 최신화.
        for cc in four_way(moved_coord, total_map[moved_coord[0]][moved_coord[1]]):
            # +1 은 cc로 가는 횟수 1 추가.
            counting_map[moved_coord[0]][moved_coord[1]] = max(counting_map[moved_coord[0]][moved_coord[1]], check_move_count(cc) + 1)

        # # 역방향 전 위치를 고려.
        # moved 로 넘어오기 전에 있던 위치에서 moved의 위치는 이미 방문한 점이 아님.
        marking_map[moved_coord[0]][moved_coord[1]] = 0

    return counting_map[moved_coord[0]][moved_coord[1]]


def is_outside_hole(coord):
    if 0 <= coord[0] < n and 0 <= coord[1] < m:
        if total_map[coord[0]][coord[1]] != 0:  # hole.
            return False
    return True


# BFS
if __name__ == '__main__':
    total_map = list()
    n, m = map(int, sys.stdin.readline().split())

    for i in range(n):
        total_map.append([*map(int, sys.stdin.readline().replace('H', '0').replace('\n', ''))])

    marking_map = [[0 for i in range(m)] for j in range(n)]
    counting_map = [[0 for i in range(m)] for j in range(n)]

    max_count = check_move_count((0, 0))
    print(max_count)