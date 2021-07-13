from itertools import permutations
from collections import Counter
import math

def check_number(number):
    flag = True
    if number <=1:
        return False
    else:
        for i in range(2, int(math.sqrt(number))+1):
            if number % i == 0:
                flag = False
    return flag

def solution(numbers):
    checker  = Counter()
    answer = 0
    for n in range(1, len(numbers)+1):
        for perm in permutations([*numbers], n):
            val = int(''.join(perm))
            if not checker[val] and check_number(val):
                answer +=1
                checker[val] += 1
    print(checker)
    return answer