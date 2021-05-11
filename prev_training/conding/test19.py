import sys

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().replace('\n', '').split())
    num_list = list(map(int, sys.stdin.readline().replace('\n', '').split()))

    count = 0
    ldx, rdx = 0, 1

    # 1. 현재 구간의 합산 구하기.
    sum_now = num_list[0]

    is_remaining = True
    while is_remaining:
        '''
        2. 현재 구간의 합산이 2보다 크거나 같으면 좌측 한칸 이동.
        3. 현재 구간의 합산이 2보다 작으면 우측 한칸 이동.
        '''
        if sum_now >= m:
            if sum_now == m:
                count += 1

            sum_now -= num_list[ldx]
            ldx += 1

        elif sum_now < m:
            if rdx < len(num_list):
                sum_now += num_list[rdx]
                rdx += 1

            if sum_now < m and rdx == len(num_list):
                is_remaining = False
                break
    print(count)
