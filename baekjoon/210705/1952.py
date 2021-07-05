import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    flag = [[0 for i in range(M)] for j in range(N)]
    map_size = (N, M)

    dir_count = 0
    dir_state = ((0, 1), (1, 0), (0, -1), (-1, 0))
    cur_state = 0
    cur_pose = [0, 0]

    # 이동.
    while 1:
        if flag[cur_pose[0]][cur_pose[1]] != 1:
            flag[cur_pose[0]][cur_pose[1]] = 1

            if sum(dir_state[cur_state]) > 0:
                if cur_pose[dir_state[cur_state].index(max(dir_state[cur_state]))] + 1 > map_size[dir_state[cur_state].index(max(dir_state[cur_state]))] - 1:
                    dir_count += 1
                    cur_state = (cur_state + 1) % 4
                elif flag[cur_pose[0] + dir_state[cur_state][0]][cur_pose[1] + dir_state[cur_state][1]] == 1:
                    # 범위 안쪽일때. 다음 위치.
                    dir_count += 1
                    cur_state = (cur_state + 1) % 4
            else:
                if cur_pose[dir_state[cur_state].index(min(dir_state[cur_state]))] - 1 < 0:
                    dir_count += 1
                    cur_state = (cur_state + 1) % 4
                elif flag[cur_pose[0] + dir_state[cur_state][0]][cur_pose[1] + dir_state[cur_state][1]] == 1:
                    # 범위 안쪽일때. 다음 위치.
                    dir_count += 1
                    cur_state = (cur_state + 1) % 4

            cur_pose[0], cur_pose[1] = cur_pose[0] + dir_state[cur_state][0], cur_pose[1] + dir_state[cur_state][1]

        else:
            break

        # print(flag)
        # print(cur_pose, cur_state)

    print(dir_count -1)
