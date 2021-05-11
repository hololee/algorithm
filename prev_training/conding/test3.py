import sys


def check(count, index, target):
    if index == 0:
        return ((count % 15) == target) or ((count % 15) == 0 and target == 15)
    elif index == 1:
        return ((count % 28) == target) or ((count % 28) == 0 and target == 28)
    else:
        return ((count % 19) == target) or ((count % 19) == 0 and target == 19)


if __name__ == "__main__":
    dat = sys.stdin.readline()

    E, S, M = map(int, dat.split(" "))

    count = 0
    while 1:
        count += 1
        if check(count, 0, E) and check(count, 1, S) and check(count, 2, M):
            print(count)
            break
