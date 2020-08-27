from itertools import combinations

n = 12
weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]


def list_split(list, indexs):  # 가능한 조합에서  각 항목들의 합을 계산! => 나누어진 루트의 총 길이들.
    temp = []
    for idx, index_num in enumerate(indexs):
        try:
            temp.append(sum(list[index_num: indexs[idx + 1]]))
        except:
            temp.append(sum(list[index_num:]))

    return temp


def cal_step_weaks(weaks):
    step = []
    for idx_wall, wall in enumerate(weaks):
        if idx_wall == len(weaks) - 1:
            step.append(n - wall + weaks[0])
        else:
            step.append(weaks[idx_wall + 1] - wall)

    return step


steps = cal_step_weaks(weaks=weak)
print(f"weak 사이의 거리 list : {steps!r}")

for i in range(len(dist)):
    print(f"{i + 1!r} 번째 조합 : {i + 1!r}개의 dist 가 큰수부터 모두 만족을 시켜야함.")

    list_combination = list(combinations(list(range(len(steps))), i + 2))
    print(f"모든 slice 지점의 조합 : {list_combination!r}")

    searching_field = []  # 모든 가능한 조합을 보관.

    print("\r\n==========잘린 거리 리스트==========")
    for j in list_combination:
        splited = list_split(list=steps, indexs=j)

        # 큰 거리부터 정렬.
        splited.sort()
        splited.reverse()

        searching_field.append(splited)
    print(searching_field)
    print("====================================\r\n")
