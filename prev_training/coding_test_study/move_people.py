import sys
from collections import deque


class MapChecker(object):

    def __init__(self, N, L, R):
        self.N = N
        self.L = L
        self.R = R
        self.direction = ((-1, 0), (1, 0), (0, -1), (0, 1))

        self.check_list = [[0 for i in range(N)] for j in range(N)]  # 체크리스트 초기화.
        self.check_count = 0

        self.search_que = deque()  # 검색 큐 초기화.
        self.union_area = deque()  # 유니온들의 큐.
        self.unions_mean_val = deque()  # 유니온들 평균 값 목록

        self.seed = (0, 0)  # 탐색 시드.

        self.specific_sum = 0  # 이동 가능한 나라 모든 인구 수
        self.specific_count = 0  # 이동 가능한 나라 수

    def init_people_map(self, map):
        self.people_map = map

    def _search(self, init):
        # 초기 위치는 check 가 안된 한점을 선택.
        if not self.search_que:
            self.search_que.append(init)
            self.check_list[init[0]][init[1]] = 1
            self.check_count += 1

        # BFS Search.
        while self.search_que:
            target = self.search_que.popleft()
            self._visit(target)

            self.union_area.append(target)
            self.specific_sum += self.people_map[target[0]][target[1]]  # 이동 가능한 나라 모든 인구 수
            self.specific_count += 1  # 이동 가능한 나라 수

    def _visit(self, target):
        # 가능 범위 체크. 4방향 L, R 체크
        for i in self.direction:
            tx = target[0] + i[0]
            ty = target[1] + i[1]
            if tx < 0 or ty < 0 or tx >= self.N or ty >= self.N:
                continue
            # 이어져 있지만 인구이동이 불가능한 나라를 다음 seed로 선택.  : seed
            if abs(self.people_map[target[0]][target[1]] - self.people_map[tx][ty]) < self.L or abs(self.people_map[target[0]][target[1]] - self.people_map[tx][ty]) > self.R:
                self.seed = (tx, ty)
                continue

            #  que 에 넣기. : search_que
            if self.check_list[tx][ty] == 0:
                self.search_que.append((tx, ty))
                #  방문 표시  : check_list
                self.check_list[tx][ty] = 1
                self.check_count += 1

    def check_move(self):
        can_move = False

        while self.check_count < (self.N * self.N):
            self._search(self.seed)
            # self.union_area 의 위치에 값들의 평균 값으로 치환.
            # self.union_area 는 한번 탐색으로 찾아낸 이동가능한 유니온 영역.

            mean_val = self.specific_sum / self.specific_count
            self.unions_mean_val.append(mean_val)
            for i in self.union_area:
                self.people_map[i[0]][i[1]] = mean_val

            self.specific_sum = 0  # 이동 가능한 나라 모든 인구 수
            self.specific_count = 0  # 이동 가능한 나라 수
            self.union_area.clear()  # 실제 위치들.

        # 체크리스트 초기화.
        self.check_list = [[0 for i in range(N)] for j in range(N)]
        self.check_count = 0
        self.seed = (0, 0)

        # TODO: unions_mean_val을 사용하여 union의 값들사이에 이동이 가능한지 파악할것.

        return can_move


if __name__ == '__main__':
    # map 정보 정리.
    N, L, R = list(map(int, sys.stdin.readline().split()))

    map_checker = MapChecker(N, L, R)

    # 인구 정보 정리.
    people_map = []
    for i in range(N):
        people_map.append(list(map(int, sys.stdin.readline().split())))

    # init map.
    map_checker.init_people_map(people_map)

    move_count = 0
    while map_checker.check_move():
        # 이동이 가능할 경우.
        move_count += 1

    print(move_count)
