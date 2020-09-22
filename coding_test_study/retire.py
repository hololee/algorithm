# import sys
#
# days = int(sys.stdin.readline())
# table = []
# can_go = [0 for d in range(days)]
# for i in range(days):
#     item = list(map(int, sys.stdin.readline().split()))
#     table.append(item)
#
# for i in range(days):
#     index = (days - 1) - i
#     finish_day = (index - 1) + table[index][0]  # 본인 날짜도포함.
#     if finish_day >= days:
#         table[index][1] = 0
#
#     else:
#         target_list = []
#         for d in range(finish_day + 1, days):
#             target_list.append(d)
#             # target_list = (table[index][1] + can_go[d])
#
#         can_go[index] = target_list


import sys


def temp_call(base_prices, m_list):
    temp_array = []
    for price in m_list:
        if isinstance(price, list):
            temp_array.append(temp_call(base_prices, price))
        else:
            temp_array.append(base_prices + price)
    return temp_array


def flatten(m_list):
    all = []
    for price in m_list:
        if isinstance(price, list):
            all.extend(flatten(price))
        else:
            all.append(price)
    return all


days = int(sys.stdin.readline())
table = []
stacked_money = [0 for d in range(days)]
for i in range(days):
    item = list(map(int, sys.stdin.readline().split()))
    table.append(item)

for i in range(days):
    index = (days - 1) - i
    finish_day = (index - 1) + table[index][0]  # 본인 날짜도포함.
    if finish_day >= days:
        table[index][1] = 0

    else:
        target_list = []
        if finish_day+1 == days:
            target_list.append(table[index][1] )
        else:
            # d는 갈 수 있는 위치.
            for d in range(finish_day + 1, days):
                if isinstance(stacked_money[d], list):
                    target_list.append(temp_call(table[index][1], stacked_money[d]))
                    # temp_array = []
                    # for go_price in can_go[d]:
                    #     if isinstance(go_price, list):
                    #         temp_array2 = []
                    #         for go_price2 in go_price:
                    #             temp_array2.append(table[index][1] + go_price2)
                    #
                    #         temp_array.append(temp_array2)
                    #     else:
                    #         temp_array.append(table[index][1] + go_price)
                    # target_list.append(temp_array)
                else:
                    target_list.append(table[index][1] + stacked_money[d])

        stacked_money[index] = target_list

flattened = flatten(stacked_money)
print(max(flattened))