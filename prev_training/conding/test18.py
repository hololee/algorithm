import sys


def pick(selected_list, vowel_count, consonant_count):
    global l, c, total_candidates, final_selected_list

    if len(selected_list) == 0:
        # 기존에 선택된 문자가 없기 때문에 후보군 변동 없음
        new_candidates = total_candidates[:]
    else:
        # 후보군중 기존 선택된 후보군 보다 뒤쪽에 올 수 있는 숫자를 픽업.
        new_candidates = total_candidates[total_candidates.index(selected_list[-1]) + 1:]
        # 기존의 선택된 문자보다 순위가 아래인 문자들중만 선택가능.

    # 끝났는지 확인.
    if len(selected_list) == l:
        # 자음, 모음 개수가 잘 들어갔나 확인.
        if vowel_count >= 1 and consonant_count >= 2:
            # 암호 만들기 성공.
            final_selected_list.append(selected_list)

    # 안끝났으면 선택 프로세스.
    elif len(new_candidates) >= l - (vowel_count + consonant_count):
        # 작성해야 하는 비밀번호와 후보군 개수를 비교하여 진행 가능한지 체크.

        # 다음 선택 프로세스.
        for sdx, sel in enumerate(new_candidates):

            # 선택한 후보군 저장.
            new_selected_list = selected_list[:]
            new_selected_list.append(sel)

            # 분기 카운트 생성,
            n_vowel_count = vowel_count
            n_consonant_count = consonant_count

            # 모음 자음 카운트.
            if sel in vowel:
                n_vowel_count = n_vowel_count + 1
            else:
                n_consonant_count = n_consonant_count + 1

            pick(new_selected_list, n_vowel_count, n_consonant_count)


if __name__ == '__main__':
    l, c = map(int, sys.stdin.readline().replace('\n', '').split())

    total = {*'abcdefghijklmnopqrstuvwxyz'}
    vowel = {*'aeiou'}
    consonant = total.difference(vowel)

    final_selected_list = list()

    total_candidates = list()
    for dat in sys.stdin.readline().replace('\n', '').split():
        # 선택 후보 리스트.
        total_candidates.append(dat)
    total_candidates = sorted(total_candidates)

    # 탐색.
    pick([], 0, 0)

    for i in final_selected_list:
        print(''.join(i))