import sys
import math


def check(number: int):
    if number == 1:
        return False
    else:
        for i in range(1, int(math.sqrt(number)) + 1):
            if i != 1 and number % i == 0:
                return False
        return True


# list(map(check, [1,2,3,4,5,6,7,8,9,10]))

if __name__ == "__main__":

    while 1:
        t = int(sys.stdin.readline())
        a = None
        b = None

        # End check.
        if t == 0:
            break
        else:
            for num in range(1, t + 1):
                # num check.
                if check(num) and check(t - num):
                    a = num
                    b = t - num
                    break

        if a is None:
            print("Goldbach's conjecture is wrong.")
        else:
            print(f"{t} = {a} + {b}")
