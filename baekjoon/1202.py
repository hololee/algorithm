# 210506

import sys
import heapq

if __name__ == "__main__":
    line = sys.stdin.readline

    # 보석을 가치가 큰 크기 부터 배열.(무게는 상관 x).
    heap_jwel = list()

    # 무게가 가장 작은 가방보다 많이 나가는 보석들을 모아둔 힙. (heap_jwel과 같이 가치가 큰거부터 )
    temp_jwel = list()

    # 가방을 작은 크기 부터 배열.
    heap_bag = list()

    # 가질 수 있는 가장 큰 값.
    max_val = 0

    heapq.heapify(heap_jwel)
    heapq.heapify(heap_bag)
    heapq.heapify(temp_jwel)

    n, k = map(int, line().replace('\n', '').split())

    for i in range(n):
        m, v = map(int, line().replace('\n', '').split())

        # 무게의 가치가 작은 순 부터 정렬.
        heapq.heappush(heap_jwel, (m, v))

    for i in range(k):
        c = int(line().replace('\n', ''))

        # 가방은 크기가 작은 것 부터 뽑을 것.
        heapq.heappush(heap_bag, c)

    while 1:
        if len(heap_bag) != 0 and heap_jwel != 0:
            bag_size = heapq.heappop(heap_bag)
            for i in range(len(heap_jwel)):
                if bag_size >= heap_jwel[0][0]:
                    m, v = heapq.heappop(heap_jwel)
                    heapq.heappush(temp_jwel, (-v, m))
                else:
                    break
                if len(heap_jwel) == 0:
                    break

            if len(temp_jwel) > 0:
                # temp_jwel 에서 pop 해서 가치 더하기.
                max_val += -1 * heapq.heappop(temp_jwel)[0]
        else:
            break
    print(max_val)
