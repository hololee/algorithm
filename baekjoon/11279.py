# 210505

import sys
import heapq

if __name__ == '__main__':
    read = sys.stdin.readline
    bucket = []
    heapq.heapify(bucket)

    n = int(read())
    for i in range(n):
        num = int(read())
        if num:
            # 음수로 assign 해서 저장. heap은 기본적으로 최소값을 반환.
            heapq.heappush(bucket, -num)

        else:
            # print
            if len(bucket) == 0:
                print(0)
            else:
                print(-1 * heapq.heappop(bucket))