import sys

if __name__ == '__main__':
    read = sys.stdin.readline

    p, c = map(int, read().replace('\n', '').split())
    cur_per = int((c * 100) / p)

    if cur_per >= 99:
        print(-1)
    else:
        min_val = ((p * (cur_per + 1)) - (c * 100)) // (99 - cur_per)
        remain = ((p * (cur_per + 1)) - (c * 100)) % (99 - cur_per)
        if remain == 0:
            print(min_val)
        else:
            print(min_val + 1)