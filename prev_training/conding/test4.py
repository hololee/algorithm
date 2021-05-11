import sys


def next(array, stack):
    if len(array) > 2:
        for i in range(len(array) - 1):
            sub = array[:]
            dat = sum(array[i:i + 2])
            if dat <= 3:
                del sub[i]
                sub[i] = dat
                if sub not in stack:
                    stack.append(sub)
                if isinstance(sub, list):
                    next(sub, stack)
    elif len(array) == 2:
        nex_val = sum(array)
        if [nex_val] not in stack:
            if nex_val <= 3:
                stack.append([nex_val])
    else:
        pass


if __name__ == '__main__':
    iter = int(sys.stdin.readline())

    for i in range(iter):
        dat = int(sys.stdin.readline())

        stack = []
        target = [1 for j in range(dat)]
        stack.append(target)
        next(target, stack)

        print(len(stack))
