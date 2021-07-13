import sys
from collections import deque

if __name__ == '__main__':
    N, M, R = map(int, sys.stdin.readline().split())
    matrix = []
    for ndx in range(N):
        matrix.append(list(map(int, sys.stdin.readline().split())))

    # all lines.
    shifted = [[0 for m in range(M)] for n in range(N)]

    # rotate line from outside.
    for l in range(min(N, M) // 2):
        # one flatten line..
        line_index = deque()
        line_val = deque()

        # line.
        n, m = N - (2 * l), M - (2 * l)
        dir = 0
        c_x = l
        c_y = l
        for p in range((2 * m) + (2 * (n - 2))):
            line_index.append((c_x, c_y))
            line_val.append(matrix[c_x][c_y])

            # check direction change points.
            if c_y == M - l - 1 and dir == 0:
                dir += 1
            elif c_x == N - l - 1 and dir == 1:
                dir += 1
            elif c_y == l and dir == 2:
                dir += 1

            # move by direction.
            if dir == 0:
                c_y += 1
            elif dir == 1:
                c_x += 1
            elif dir == 2:
                c_y -= 1
            elif dir == 3:
                c_x -= 1

        # shift lines.
        for x in range(R):
            line_val.append(line_val.popleft())

        # save to shifted.
        for pdx, pose in enumerate(line_index):
            shifted[pose[0]][pose[1]] = line_val[pdx]

    for i in shifted:
        print(' '.join(map(str, i)))
