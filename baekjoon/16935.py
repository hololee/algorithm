# 210629

import sys
import copy


def calculate(cal_type, matrix, n, m):
    temp_matrix = copy.deepcopy(matrix)

    if cal_type == 1:
        # 상하 반전.
        for row in range(n):
            matrix[row] = temp_matrix[n - row - 1]

    elif cal_type == 2:
        # 좌우 반전.
        for row in range(n):
            for col in range(m):
                matrix[row][col] = temp_matrix[row][m - col - 1]

    elif cal_type == 3:
        # cw 90.
        new_matrix = [[0 for j in range(n)] for i in range(m)]
        for row in range(n):
            for col in range(m):
                new_matrix[col][row] = temp_matrix[n - row - 1][col]

        n, m = m, n
        matrix = new_matrix

    elif cal_type == 4:
        # ccw 90.
        new_matrix = [[0 for j in range(n)] for i in range(m)]
        for row in range(n):
            for col in range(m):
                new_matrix[col][row] = temp_matrix[row][m - col - 1]

        n, m = m, n
        matrix = new_matrix

    elif cal_type == 5:
        # 분할 cw 90.
        for row in range(n):
            for col in range(m):
                if row < n // 2 and col < m // 2:
                    # region1
                    matrix[row][col] = temp_matrix[row + n // 2][col]
                elif row < n // 2 and col >= m // 2:
                    # region2
                    matrix[row][col] = temp_matrix[row][col - m // 2]
                elif row >= n // 2 and col >= m // 2:
                    # region3
                    matrix[row][col] = temp_matrix[row - n // 2][col]
                else:
                    # region4
                    matrix[row][col] = temp_matrix[row][col + m // 2]

    elif cal_type == 6:
        # 분할 ccw 90.
        for row in range(n):
            for col in range(m):
                if row < n // 2 and col < m // 2:
                    # region1
                    matrix[row][col] = temp_matrix[row][col + m // 2]
                elif row < n // 2 and col >= m // 2:
                    # region2
                    matrix[row][col] = temp_matrix[row + n // 2][col]
                elif row >= n // 2 and col >= m // 2:
                    # region3
                    matrix[row][col] = temp_matrix[row][col - m // 2]
                else:
                    # region4
                    matrix[row][col] = temp_matrix[row - n // 2][col]

    return matrix, n, m


if __name__ == '__main__':
    N, M, R = map(int, sys.stdin.readline().split())

    m_matrix = list()

    for idx in range(N):
        m_matrix.append(sys.stdin.readline().split())

    for cal_type in map(int, sys.stdin.readline().split()):
        m_matrix, N, M = calculate(cal_type, m_matrix, N, M)

    for n in range(N):
        print(' '.join(m_matrix[n]))
