def find_number(p_array, c_array):
    return sorted(p_array[c_array[0] - 1:c_array[1]])[c_array[2] - 1]


def solution(array, commands):
    answer = []

    for c in commands:
        answer.append(find_number(array, c))

    return answer