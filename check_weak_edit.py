from itertools import combinations, permutations

# n = 12
# weak = [1, 3, 4, 9, 10]
# dist = [3, 5, 7]
n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]


def solution(n, weak, dist):
    # 시계 생각! 12+1 = 13
    def shift_start(weak_origin, idx_start, max_length):
        assert 0 <= idx_start < len(weak_origin), "index 값이 범위를 벗어남!"
        shifted = weak_origin[idx_start:] + [(item + max_length) for item in weak_origin[:idx_start]]
        return shifted

    all_dists_permut = list(permutations(dist))

    remained_positions_list = [[shift_start(weak, weak_start, n) for weak_start in range(0, len(weak))] for j in
                               all_dists_permut]

    answers = []

    for idx_dist_list, permut_dist in enumerate(permutations(dist)):
        #TODO:print(f"현재 진행중인 친구들 : {permut_dist!r}")

        is_answer_filled = False

        for idx_permut, item_permut in enumerate(permut_dist):
            if not is_answer_filled:
                # 시작점이 다른 모든 경우의 수
                # if i == permut_dist[0]:  # 두번째 부터는 기존 남아있는 위치들을 그대로 이용한다.

                # print(f"{idx_permut!r}번째 친구 도전중..")

                # for 문으로 돌아가는 변수를 중간에 변경해도 진행중인 for문의 item은 영향이 없음을 확인.. for문이 끝날때 변수 값이 변함.
                for idx_rp, remained_positions in enumerate(remained_positions_list[idx_dist_list]):
                    if not is_answer_filled:
                        #TODO:print(f"{idx_dist_list!r}집합의 {idx_permut!r}번째 친구가 {idx_rp!r}번째 기준점 도전중..")
                        '''
                        [->[1,5,6,10], [5,6,10,13], [6,10,13,17], [10,13,17,18]]
                        [[1,5,6,10], ->[5,6,10,13], [6,10,13,17], [10,13,17,18]]
                        [[1,5,6,10], [5,6,10,13], ->[6,10,13,17], [10,13,17,18]]
                        [[1,5,6,10], [5,6,10,13], [6,10,13,17], ->[10,13,17,18]]
                        
                        반복이 끝나면.
                        [[6,10], [10,13], [13,17], [17,18]]
                        
                        '''

                        # 해당 차례의 친구가 이동한 최종 거리.
                        friend_target_position = remained_positions[0] + item_permut
                        # 남아 있는 목표의 첫번째 값이 처음 이동한 친구의 값보다 작아지기 전까지
                        if not is_answer_filled:
                            while remained_positions[0] <= friend_target_position:
                                # 남아있는 위치를 지운다.
                                del remained_positions[0]

                                #TODO:print(remained_positions)
                                # 남아 있는 수가 없을때 (합이 0일때) 현재 사용된 인원수를 반환.
                                if sum(remained_positions) == 0:
                                    answers.append(idx_permut + 1)
                                    is_answer_filled = True
                                    break

                        #TODO:print(remained_positions_list)

    # 모든 친구를 써도 weak 이 남아 있는겨우.
    if sum(answers) == 0:
        return -1
    else:
        return min(answers)


print(solution(n, weak, dist))
