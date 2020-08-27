from itertools import combinations, permutations
import copy

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

    dist.reverse()
    answer_list = []

    for permut_dist in permutations(dist):
        print(f"현재 진행중인 친구들 : {permut_dist!r}")

        remained_positions_list = []
        for i in permut_dist:
            # 시작점이 다른 모든 경우의 수
            if i == permut_dist[0]:  # 두번째 부터는 기존 남아있는 위치들을 그대로 이용한다.
                remained_positions_list = [shift_start(weak, weak_start, n) for weak_start in range(0, len(weak))]

            # for 문으로 돌아가는 변수를 중간에 변경해도 진행중인 for문의 item은 영향이 없음을 확인.. for문이 끝날때 변수 값이 변함.
            for idx_rp, remained_positions in enumerate(remained_positions_list):
                '''
                [->[1,5,6,10], [5,6,10,13], [6,10,13,17], [10,13,17,18]]
                [[1,5,6,10], ->[5,6,10,13], [6,10,13,17], [10,13,17,18]]
                [[1,5,6,10], [5,6,10,13], ->[6,10,13,17], [10,13,17,18]]
                [[1,5,6,10], [5,6,10,13], [6,10,13,17], ->[10,13,17,18]]
                
                반복이 끝나면.
                [[6,10], [10,13], [13,17], [17,18]]
                
                '''
                # 그냥 하면 리스트 원본이 영향을 받음.
                copied_remained_positions = remained_positions.copy()

                # 해당 차례의 친구가 이동한 최종 거리.
                friend_target_position = copied_remained_positions[0] + i
                # 남아 있는 목표의 첫번째 값이 처음 이동한 친구의 값보다 작아지기 전까지
                while copied_remained_positions[0] <= friend_target_position:
                    # 남아있는 위치를 지운다.
                    del copied_remained_positions[0]

                    # 남아 있는 수가 없을때 (합이 0일때) 현재 사용된 인원수를 반환.
                    if sum(copied_remained_positions) == 0:
                        return i

                remained_positions_list[idx_rp] = copied_remained_positions  # 원본 남은 거리를 최신으로 변경.

    # 모든 친구를 써도 weak 이 남아 있는겨우.
    return -1


print(solution(n, weak, dist))
