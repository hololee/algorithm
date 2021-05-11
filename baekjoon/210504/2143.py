import sys
import bisect


def cal_sum_list(array, size):
    array_sum_list = list()

    for s_size in range(1, size + 1):
        temp_sum = sum(array[0:s_size])
        array_sum_list.append(temp_sum)
        for s_crd in range(s_size, size):
            temp_sum += array[s_crd]
            temp_sum -= array[s_crd - s_size]
            array_sum_list.append(temp_sum)

    return sorted(array_sum_list), set(array_sum_list)


if __name__ == "__main__":
    t = int(sys.stdin.readline())
    len_a = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().replace('\r', '').split()))
    len_b = int(sys.stdin.readline())
    b = list(map(int, sys.stdin.readline().replace('\r', '').split()))

    a_sum_list, set_a = cal_sum_list(a, len_a)
    b_sum_list, set_b = cal_sum_list(b, len_b)

    count = 0
    for i in a_sum_list:
        target = t - i
        count += bisect.bisect_right(b_sum_list, target) - bisect.bisect_left(b_sum_list, target)

    print(count)