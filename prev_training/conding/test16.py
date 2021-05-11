import sys
from collections import deque

if __name__ == '__main__':

    def get_candidate(base_sum, remain_list, max_val):
        candidate = 0
        for r in remain_list:
            if base_sum + r <= max_val:
                candidate = max(candidate, r)

        # 리스트에서 다리건널 차량 제거.
        if candidate in remain_list:
            remain_list.remove(candidate)

        return candidate


    def solution(bridge_length, weight, truck_weights):
        passed = 0
        count = 0
        weight_sum = 0

        truck_weights = sorted(truck_weights, reverse=True)

        total_sum = sum(truck_weights)

        bridge = deque()
        first_pass_car = max(truck_weights)
        truck_weights.remove(first_pass_car)
        bridge.append(first_pass_car)
        weight_sum += first_pass_car
        count += 1

        while bridge:
            # 공간이 남는지 확인.
            if len(bridge) >= bridge_length:
                # 다리 최대 길이와 같거나 크면 (같은 경우 목표) 하나 빼고 후보군 넣어줌.
                get_item = bridge.popleft()
                weight_sum -= get_item
                passed += get_item
                # 수가 다 통과했는지 체크.
                if passed == total_sum:
                    count += 1
                    print(count)
                    break

            candidate = get_candidate(weight_sum, truck_weights, weight)
            bridge.append(candidate)
            weight_sum += candidate

            count += 1

            print(candidate)

        return count


    solution(2, 10, [7, 4, 5, 6])
