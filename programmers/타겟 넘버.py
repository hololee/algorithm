counter = 0


def move_next(index, marker, summer):
    global m_numbers, m_target, counter

    marker[index] = 1
    for i in [-1, 1]:
        new_marker = marker[:]
        new_summer = summer
        new_summer += m_numbers[index] * i

        if 0 <= index + 1 < len(m_numbers):
            if new_marker[index + 1] == 0:
                move_next(index + 1, new_marker, new_summer)
        else:
            if new_summer == m_target:
                counter += 1


def solution(numbers, target):
    global m_numbers, m_target

    m_numbers = numbers
    m_target = target

    marker = [0 for i in range(len(numbers))]
    move_next(0, marker, 0)

    return counter