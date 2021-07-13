# 210505

import sys
import heapq


class TopListHeap(object):
    def __init__(self):
        # 가장 작은 값을 우선시 하는 힙. (상위 랭크)
        self.base_list = list()
        # 힙 변환.
        heapq.heapify(self.base_list)

    def __len__(self):
        return len(self.base_list)

    def add_item(self, item: int):
        heapq.heappush(self.base_list, item)

    def pop_item(self):
        return heapq.heappop(self.base_list)

    def get_lowest(self):
        return self.base_list[0]


class LowListHeap(object):
    def __init__(self):
        # 가장 큰 값을 우선시 하는 힙. (하위 랭크)
        self.base_list = list()
        # 힙 변환.
        heapq.heapify(self.base_list)

    def __len__(self):
        return len(self.base_list)

    def add_item(self, item: int):
        heapq.heappush(self.base_list, -1 * item)

    def pop_item(self):
        return -1 * heapq.heappop(self.base_list)

    def get_highest(self):
        return -1 * self.base_list[0]


def compare_allocate(top_list: TopListHeap, low_list: LowListHeap, target: int):
    if len(low_list) == 0:
        # 아직 값을 입력받기 전 하위에 처음으로 추가.\
        low_list.add_item(target)
    elif len(low_list) == 1 and len(top_list) == 0:
        l = low_list.get_highest()
        if target < l:
            # 하위의크기가 클때 하위로 추가하고 하위의 가장 큰값을상위에추가.
            low_list.add_item(target)
            top_list.add_item(low_list.pop_item())
        else:
            # 큰쪽에 추가.
            top_list.add_item(target)

    else:
        l = low_list.get_highest()
        h = top_list.get_lowest()

        if l <= target <= h:
            # 숫자가 상위의 가장 작은 값과 하위 가장큰 값 사이인경우:
            if len(low_list) <= len(top_list):
                # 두 힙의 크기가 같으면 아래쪽으로 추가.
                low_list.add_item(target)
            else:
                # 두 힙 중 크기가 작은쪽으로 추가.
                top_list.add_item(target)

        elif target > h:
            # 숫자가 상위의 가장 작은 값보다 큰경우.
            if len(low_list) == len(top_list):
                # 두 힙의크기가같을때 상위에추가하고 상위의 작은  값을  하위로추가
                top_list.add_item(target)
                low_list.add_item(top_list.pop_item())
            else:
                # 하위의 크기가 클때 상위로 추가.
                top_list.add_item(target)

        elif target < l:
            #  숫자가 하위의 가장 큰 값보다 작은 경우,
            if len(low_list) == len(top_list):
                # 두 힙의 크기가 같을때 하위로 추가.
                low_list.add_item(target)
            else:
                # 하위의크기가 클때 하위로 추가하고 하위의 가장 큰값을상위에추가.
                low_list.add_item(target)
                top_list.add_item(low_list.pop_item())

    # 두 힙의 크기는 하위 힙이 크거나 둘이 같기 때문에
    # 중간값은 항상 하위의 가장 큰 값.
    return low_list.get_highest()


if __name__ == '__main__':
    read = sys.stdin.readline

    n = int(read())

    '''
    상위 하위 힙으로 나눠서 상위는 최소힙, 하위는 최대힙.
    넣을 숫자가 주어질때 상위의 가장 작은 값과 하위의 가장 큰값과 비교.
    '''
    list_top = TopListHeap()
    list_low = LowListHeap()

    for i in range(n):
        num = int(read())

        print(compare_allocate(list_top, list_low, num))