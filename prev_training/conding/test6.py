def perm(s):
    bank = []

    if len(s) < 2:
        return s

    for idx, i in enumerate(s):

        bank.append(i)
        for j in perm(s[:idx] + s[idx + 1:]):
            # perm 이 하위 숫자 조합의 리스트를 반환함.
            '''
            '2'
            '1'
            
            '''
            bank.append(i + j)

    return bank


print(perm('123'))
