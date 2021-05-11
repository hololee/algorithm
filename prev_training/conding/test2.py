import sys
from itertools import combinations as c

if __name__ == "__main__":
    d_list = []
    for i in range(9):
        dat = int(sys.stdin.readline())
        d_list.append(dat)

    for i in c(d_list, 7):
        if sum(i) == 100:
            i = sorted(list(i))
            for j in i:
                print(j)
            break
