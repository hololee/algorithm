import sys

if __name__ == '__main__':
    N = sys.stdin.readline()
    balls = sys.stdin.readline().replace('\n', '')
    probs = 0
    # rb
    if balls.startswith('R'):
        if balls.endswith('R'):
            # start RR type.
            # to rb move r
            # print(balls.count('R') - len(balls.split('B')[0]))
            # to rb move b
            # print(balls.count('B'))
            # to br move r
            # print(balls.count('R') - len(balls.split('B')[-1]))
            # to br move b
            # print(balls.count('B'))
            probs = min(balls.count('R') - len(balls.split('B')[0]), balls.count('B'), balls.count('R') - len(balls.split('B')[-1]))
        else:
            # start RB type.
            # to rb move r
            # balls.count('R') - len(balls.split('B')[0])
            # to rb move b
            # balls.count('B') - len(balls.split('R')[-1])
            # to br move r
            # balls.count('R')
            # to br move b
            # balls.count('B')
            probs = min(balls.count('R') - len(balls.split('B')[0]), balls.count('B') - len(balls.split('R')[-1]))

    else:
        if balls.endswith('R'):
            # start BR type.
            # to rb move r
            # balls.count('R')
            # to rb move b
            # balls.count('B')
            # to br move r
            # balls.count('R') - len(balls.split('B')[-1])
            # to br move b
            # balls.count('B') - len(balls.split('R')[0])
            probs = min(balls.count('R') - len(balls.split('B')[-1]), balls.count('B') - len(balls.split('R')[0]))

        else:
            # start BB type.
            # to rb move r
            # balls.count('R')
            # to rb move b
            # balls.count('B') - len(balls.split('R')[-1])
            # to br move r
            # balls.count('R')
            # to br move b
            # balls.count('B') - len(balls.split('R')[0])
            probs = min(balls.count('B') - len(balls.split('R')[-1]), balls.count('R'), balls.count('B') - len(balls.split('R')[0]))

    print(probs)
