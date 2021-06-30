import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    flag = [[0 for i in range(M)] for j in range(N)]

    dir_count = 0
    dir_state = ((0, 1), (1, 0), (-1, 0), (0, -1))
    cur_state = dir_state[0]


