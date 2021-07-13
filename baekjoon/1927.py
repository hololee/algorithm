# 210506

import sys
import heapq

if __name__ == '__main__':

    n = int(sys.stdin.readline())

    que = list()

    for i in range(n):
        dat = int(sys.stdin.readline())

        if dat == 0:
            # 현재 최솟값 출력.
            if len(que) == 0:
                print(0)
            else:
                print(heapq.heappop(que))

        else:
            # data 추가.
            heapq.heappush(que, dat)