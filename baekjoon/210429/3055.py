import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def check_inside(coord):
    if 0 <= coord[0] < r and 0 <= coord[1] < c:
        return True
    else:
        return False


def check_water_go(coord):
    # 물은 구역 밖이나 X, D를 갈 수 없다.
    if check_inside(coord) and total_map[coord[0]][coord[1]] != 'X' and total_map[coord[0]][coord[1]] != 'D':
        if w_visited[coord[0]][coord[1]] != 1:
            return True

    return False


def check_s_go(coord):
    # 고슴도치는 구역 밖이나 *,  X를 갈 수 없다.
    if check_inside(coord) and total_map[coord[0]][coord[1]] != 'X' and w_visited[coord[0]][coord[1]] != 1:
        if s_visited[coord[0]][coord[1]] != 1:
            return True

    return False


if __name__ == '__main__':
    r, c = map(int, sys.stdin.readline().split())

    # 이동 시간.
    count = 0

    # 각 초기 위치

    # 마지막으로 물이 채워진 위치.
    w_fill_last = deque()

    # 고슴도치 다음 탐색 위치.
    s_go = deque()

    total_map = [[0 for j in range(c)] for i in range(r)]
    s_visited = [[0 for j in range(c)] for i in range(r)]
    w_visited = [[0 for j in range(c)] for i in range(r)]

    # 맵 완성.
    for rdx in range(r):
        for cdx, val in enumerate(sys.stdin.readline().replace('\n', '')):
            total_map[rdx][cdx] = val
            if val == 'S':
                s_go.append((rdx, cdx))
                # 고슴도치 방문 체크.
                s_visited[rdx][cdx] = 1
            elif val == '*':
                w_fill_last.append((rdx, cdx))
                # 물 채워짐.
                w_visited[rdx][cdx] = 1

    # BFS 시작.
    while s_go:

        # 물부터 채우기.
        next_w_fill_list = deque()
        for w in w_fill_last:
            # 4방향 체크해서 물이 이동 가능한 지점을 다음 레벨로 추가.
            for i in range(4):
                if check_water_go((w[0] + dx[i], w[1] + dy[i])):
                    # 다음 좌표 갱신.
                    next_w_fill_list.append((w[0] + dx[i], w[1] + dy[i]))
                    # 물 채워짐.
                    w_visited[w[0] + dx[i]][w[1] + dy[i]] = 1

        # 다음 리스트 갱신.
        w_fill_last = next_w_fill_list

        next_s_go = deque()
        # 고슴도치 이동.
        for s in s_go:
            # 4방향 체크하고 고슴도치가 이동가능한 지점을 다음 레벨로 추가.
            for i in range(4):
                if check_s_go((s[0] + dx[i], s[1] + dy[i])):
                    if total_map[s[0] + dx[i]][s[1] + dy[i]] == 'D':
                        # 만났다.
                        print(count + 1)
                        exit()
                    else:
                        next_s_go.append((s[0] + dx[i], s[1] + dy[i]))
                        # 고슴도치 방문 체크.
                        s_visited[s[0] + dx[i]][s[1]+ dy[i]] = 1

        # 다음 고슴도치가 갈곳 갱신.
        s_go = next_s_go

        # 분 추가.
        count += 1

        # for dd in range(r):
        #     print(w_visited[dd])
        # print('--------------')
        # for dd in range(r):
        #     print(s_visited[dd])
        # print(count)

    print("KAKTUS")
