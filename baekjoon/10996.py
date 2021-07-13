# 200922


num = int(input())

if num == 1:
    print('*')
else:
    second = (num // 2)
    first = second + (num % 2)

    for i in range(num):
        first_s = ''
        for i in range(first * 2):
            if i % 2 == 0:
                first_s += '*'
            else:
                first_s += ' '
        print(first_s.strip())
        second_s = ''
        for i in range(second * 2):
            if i % 2 == 1:
                second_s += '*'
            else:
                second_s += ' '
        print(second_s)
