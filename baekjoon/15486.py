# 200926

import sys

days = int(sys.stdin.readline())
consume = []
money = []
after_can_get = []

for day in range(days):
    c, m = list(map(int, sys.stdin.readline().split()))
    consume.append(c)
    money.append(m)
    after_can_get.append(0)

for i in range(days):
    index = days - i - 1
    if index + consume[index] > days:  # 은퇴보다 더 상담이 길어지는 경우.
        if index != days - 1:# 마지막 날짜가 아닌경우
            take_current = 0
            not_take_current = after_can_get[index + 1]
            after_can_get[index] = max(take_current, not_take_current)
        else:
            # 얻을 돈이 없음.
            after_can_get[index] = 0
    elif index + consume[index] == days:  # !! 여러번 나올 경우를 생각!
        if index != days - 1:# 마지막 날짜가 아닌경우
            take_current = money[index]
            not_take_current = after_can_get[index + 1]
            after_can_get[index] = max(take_current, not_take_current)
        else:
            after_can_get[index] = money[index]
    else:
        # 현재 날짜의 상담을했을때 얻을 수 있는돈 + 그 이후에 선택할 돈의 합.
        take_current = money[index] + after_can_get[index + consume[index]]
        # 현재 날짜의 상담을 하지 않을경우. 바로 다음날부터 선택가능한 돈들의 합(가장 큰 돈)
        not_take_current = after_can_get[index + 1]
        # 현재 날짜를 선택하면 그 이후에 선택가능한 날짜들의 돈의 합과 현재상담의 돈이 벌 수 있는돈의 합.
        # 현재 날짜를 포기하면 바로 그 다음날 이후로 선택가능한 날짜들의돈의 합이 벌 수 있는돈.
        # 따라서 현재날짜를포기 할지 선택할지 그 값을 보고 결정한다.
        after_can_get[index] = max(take_current, not_take_current)

print(after_can_get[0])
