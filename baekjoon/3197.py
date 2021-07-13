# 200921

import sys
from collections import deque

class LakeMap(object):
    def __init__(self, lake, row, col):
        self.lake = lake
        self.row = row
        self.col = col
        self.check_positions = [[0 for c in range(col)] for r in range(row)]

        self.swan_position = []
        self.melting_positions = set()

        # 이웃들.
        self.ice_in_path = set()

        self._find_swan()

    def _find_swan(self):
        for i in range(self.row):
            for j in range(self.col):
                if self.lake[i][j] == 'L':
                    self.swan_position.append((i, j))
                    self.lake[i][j] = '.'

    def reduce_area(self):
        new_melting_positions = set()

        # 타켓이 없는경우.
        if not self.melting_positions:
            for i in range(self.row):
                for j in range(self.col):
                    # 얼음인 경우만 동작.
                    if self.lake[i][j] == '.':
                        # 4방향 체크.
                        if i > 0 and self.lake[i - 1][j] == 'X':  # 상
                            new_melting_positions.add((i - 1, j))
                        if i < (self.row - 1) and self.lake[i + 1][j] == 'X':  # 하
                            new_melting_positions.add((i + 1, j))
                        if j > 0 and self.lake[i][j - 1] == 'X':  # 좌
                            new_melting_positions.add((i, j - 1))
                        if j < (self.col - 1) and self.lake[i][j + 1] == 'X':  # 우
                            new_melting_positions.add((i, j + 1))

        # 타켓 (전에 사라진 얼음들) 이 있는경우.
        else:
            for target in self.melting_positions:
                i = target[0]
                j = target[1]
                # 4방향 체크.
                if i > 0 and self.lake[i - 1][j] == 'X':  # 상
                    new_melting_positions.add((i - 1, j))
                if i < (self.row - 1) and self.lake[i + 1][j] == 'X':  # 하
                    new_melting_positions.add((i + 1, j))
                if j > 0 and self.lake[i][j - 1] == 'X':  # 좌
                    new_melting_positions.add((i, j - 1))
                if j < (self.col - 1) and self.lake[i][j + 1] == 'X':  # 우
                    new_melting_positions.add((i, j + 1))

        for pos in new_melting_positions:
            self.lake[pos[0]][pos[1]] = '.'

        self.melting_positions = new_melting_positions

    def _visit_adj(self, moving_position, target_que):
        # 상하좌우 이동 가능한 공간.
        x, y = moving_position[0], moving_position[1]
        if x > 0:
            if self.lake[x - 1][y] == '.':  # 상
                if self.check_positions[x - 1][y] == 0:
                    self.check_positions[x - 1][y] = 1
                    target_que.append((x - 1, y))
            else:
                self.ice_in_path.add((x - 1, y))
        if x < (self.row - 1):
            if self.lake[x + 1][y] == '.':  # 하
                if self.check_positions[x + 1][y] == 0:
                    self.check_positions[x + 1][y] = 1
                    target_que.append((x + 1, y))
            else:
                self.ice_in_path.add((x + 1, y))
        if y > 0:
            if self.lake[x][y - 1] == '.':  # 좌
                if self.check_positions[x][y - 1] == 0:
                    self.check_positions[x][y - 1] = 1
                    target_que.append((x, y - 1))
            else:
                self.ice_in_path.add((x, y - 1))
        if y < (self.col - 1):
            if self.lake[x][y + 1] == '.':  # 우
                if self.check_positions[x][y + 1] == 0:
                    self.check_positions[x][y + 1] = 1
                    target_que.append((x, y + 1))
            else:
                self.ice_in_path.add((x, y + 1))

    def is_reach(self):
        target_que = deque()
        if not self.ice_in_path:
            target_que.append(self.swan_position[0])
            self.check_positions[self.swan_position[0][0]][self.swan_position[0][1]] = 1
        else:
            # 기존 탐색시 만난 얼음들 부터 탐색.
            for pos in self.ice_in_path:
                target_que.append(pos)
                self.check_positions[pos[0]][pos[1]] = 1

        self.ice_in_path.clear()

        # 모든 가능한 길 탐색
        while target_que:
            tar_pos = target_que.popleft()

            self._visit_adj(tar_pos, target_que)
            # 탐색 중 얼음으로 못갔던 부분을 따로 저장 나중에 해당 지점부터 다시 시작.

        # 갔던 길에 다른 swan 이 포함 되는지 체크
        if self.check_positions[self.swan_position[1][0]][self.swan_position[1][1]] == 1:
            return True
        return False


# Main start
R, C = list(map(int, sys.stdin.readline().split()))

lake = []
for i in range(R):
    lake.append(list(sys.stdin.readline().replace('\n', '')))

meet = False
days = 0

lakeMap = LakeMap(lake, R, C)

while not lakeMap.is_reach():
    days += 1
    lakeMap.reduce_area()
print(days)

