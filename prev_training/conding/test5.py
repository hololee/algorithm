import sys


def compress(val):
    count = 1
    tag = val[0]

    compressed = list()

    for idx, i in enumerate(val):
        if idx != 0:
            if i == tag:
                count += 1
            else:
                compressed.append(tag)
                compressed.append(str(count))
                count = 1
                tag = i

    return ''.join(compressed)


if __name__ == '__main__':
    dat = sys.stdin.readline()

    # dat = aabbbbcccddd

    print(compress(dat))
