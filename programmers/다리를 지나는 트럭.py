from collections import deque


def get_candidate(base_sum, remain_list, max_val):
    candidate = 0
    if len(remain_list) > 0:
        if base_sum + remain_list[0] <= max_val:
            candidate = remain_list[0]

            del remain_list[0]

    return candidate


def solution(bridge_length, weight, truck_weights):
    passed = 0
    count = 0
    weight_sum = 0

    total_sum = sum(truck_weights)

    bridge = deque()
    first_car = truck_weights[0]
    bridge.append(first_car)
    weight_sum += first_car
    count += 1

    del truck_weights[0]

    while bridge:
        # 공간이 남는지 확인.
        if len(bridge) == bridge_length:
            # 다리 최대 길이와 같거나 크면 (같은 경우 목표) 하나 빼고 후보군 넣어줌.
            get_item = bridge.popleft()
            weight_sum -= get_item
            passed += get_item
            # 수가 다 통과했는지 체크.
            if passed == total_sum:
                count += 1
                break

        candidate = get_candidate(weight_sum, truck_weights, weight)
        bridge.append(candidate)
        weight_sum += candidate

        count += 1

    return count