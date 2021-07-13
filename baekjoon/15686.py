# 210427

import sys
from itertools import combinations


def find_same_ele(dis_list, min_list):
    count = 0
    removed_list = list()

    for dist in zip(dis_list, min_list):
        if dist[0] == dist[1]:
            count += 1
            removed_list.append(dist[0])

    return count, removed_list


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())

    home_list = list()
    chic_list = list()

    for r in range(n):
        for c, b_type in enumerate(map(int, sys.stdin.readline().split())):
            if b_type == 0:
                continue
            elif b_type == 1:
                home_list.append((r, c))
            else:
                chic_list.append((r, c))

    distance_list = list()
    min_key_by_home = list()

    for h in home_list:

        home_temp = list()
        for c in chic_list:
            home_temp.append(abs(h[0] - c[0]) + abs(h[1] - c[1]))

        # 가장 작은값 넣기.
        min_key_by_home.append(min(home_temp))

        # 모든 거리 리스트.
        distance_list.append(home_temp)

    total_dis_list = []
    for selected_chick_indices in combinations(range(len(chic_list)), m):

        combi_min = 0
        for h in range(len(home_list)):
            dis_list = []
            for selected_chick_index in selected_chick_indices:
                dis_list.append(distance_list[h][selected_chick_index])

            combi_min += min(dis_list)

        total_dis_list.append(combi_min)

    print(min(total_dis_list))
