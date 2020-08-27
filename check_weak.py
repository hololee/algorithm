from itertools import combinations

n = 12
weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]


# 가능한 조합에서  각 항목들의 합을 계산! => 나누어진 루트의 총 길이들.
def list_split(list, indices):
    temp = []
    for idx, index_num in enumerate(indices):
        try:
            temp.append(sum(list[index_num: indices[idx + 1]]))
        except:
            # 마지막인 경우, 시작점까지의 거리를 합산.
            temp.append(sum(list[index_num:]) + sum(list[:indices[0]]))

    return temp


# weak 사이 거리 계산.
def cal_step_weaks(weaks, max_len):
    step = []
    for idx_wall, wall in enumerate(weaks):
        if idx_wall == len(weaks) - 1:
            step.append(max_len - wall + weaks[0])
        else:
            step.append(weaks[idx_wall + 1] - wall)

    return step


# weak 사이 거리 계산.
steps = cal_step_weaks(weaks=weak, max_len=n)

print(f"총 거리 : {n!r}")
print(f"친구 목록 list : {dist!r}")
print(f"약한 지점 목록 list : {weak!r}")
print(f"weak 사이의 거리 list : {steps!r}\r\n")

for i in range(len(dist)):
    print(f"{i + 1!r} 번째 조합 : {i + 1!r}개의 dist 가 큰수부터 모두 만족을 시켜야함.")

    list_combination = list(combinations(list(range(len(steps))), i + 2))
    print(f"모든 slice 지점의 조합 : {list_combination!r}")

    searching_field = []  # 모든 가능한 조합을 보관.

    print("\r\n==========잘린 거리 리스트==========")
    for j in list_combination:
        splited = list_split(list=steps, indices=j)

        # 큰 거리부터 정렬.
        splited.sort()
        splited.reverse()

        # TODO: 하나라도 만족하면 answer 그대로
        # 전부 만족 못하는 경우 answer + 1

        searching_field.append(splited)
    print(searching_field)
    print("====================================\r\n")

    """ searching_field 에서 2가지 조함부터 체크해서 answer 1씩 늘리기.
        마지막 반복에서 만약 큰 순서대로 len(dist) 의 조건을 만족시키지 못하면 -1 리턴 
        !잘린 거리의 합산이 n 이 되는지 체크.!
    """
