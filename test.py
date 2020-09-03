# N 을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.
length = int(input())

mcount = 0


#
# def check(position, last=0, first=False):
#     global mcount
#     for i in range(10):
#         # 처음 이면서 0이 아니거나  앞수와 1차이가 나면.
#         if (first and i != 0) or abs(i - last) == 1:
#             if position == 0:
#                 mcount = mcount + 1
#             else:
#                 check(position - 1, i)
#
#
# check(length - 1, first=True)
# print(mcount)


def check(position, last):
    global mcount
    if position != 0:
        if last > 0: check(position - 1, last - 1)
        if last < 9: check(position - 1, last + 1)
    else:
        mcount += 1


for i in range(0, 10):
    check(length - 1, i)
    print(mcount)
    mcount = 0
