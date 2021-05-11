import sys


# 코드는 대략 아래와 같은데 저기 에서 중복 처리가 안되어서 일단 틀렸습니다 ㅠ
'''
방법은 우선  a b c 물건이 있고 각 val 이 A B C 일때 a 먼저 넣고 자리 있으면 b 넣고  그다음 들어올 c 랑 (a, b) 랑 비교해서 큰거 넣고 
대략적으로 이런 방식으로 진행을 하였는데 
중복일경우( 아이탬 무게랑 val 이 같은경우) 처리가 안되서 일단 틀렸습니ㅏㄷ ㅠ

예로 아래 가 있을때 Val 은 A +B 상태인거지
이런식으로?

저 break point 인근에서 자꾸 혼돈이 와서 틀렸어

(a, b)

'''

def searching(K, items):
    total = []

    for i, item in enumerate(items):
        temp = []
        for j in range(0, K + 1):
            if i == 0:
                if item[0] > j:
                    temp.append(0)  # can not add value.
                else:
                    temp.append(item[1])  # add value.
            else:
                if item[0] > j:
                    temp.append(total[i - 1][j])  # can not add value.

                else:
                    # can add val.
                    if j - item[0] > 0:  # free space remain.
                        if j - item[0] > item[0]:
                            # prevent use same goods.  # 같은 아이템이 여러개 있을 경우는 판단 불가.
                            temp_val = max(max(item[1], total[i - 1][j]), item[1] + total[i - 1][j - item[0]])
                        else:
                            temp_val = max(temp[j - 1], total[i - 1][j])
                    else:
                        temp_val = max(item[1], total[i - 1][j])


                        '''
                        temp0 = 0 0 0 0 0 0 0 ... 0
                        temp1 = 여기서부터 위값이랑 현재 선택한 물건의 값 , 이전 history 값 하고 비교를 해서 최고 값만 stack 시키는 구조 입니다.
                        
                        tempN 이 있을때 예를들어 8의 공간이 있고 1인 물건을 선택했는데 남은 공간이 7인데 계속 1을 더 선택하는 경우가 만들어져서
                        그부분을 제할려고 37-44 추가했는데 
                        같은 아이템이 생기니 이전에 한번 사용했다고 보고 사용을 안해서  stack이 안됩니다.ㅠㅠ
                        이부분은 해결되면 다시 말씀 드릴게요 여기 짜다가 막 들어와서 고민좀 해봐야 할드...
                        
                        일단 틀려서 접근 법이 맞나 모르겠ㄴ에 요요
                        
                       '''


                    temp.append(temp_val)
        total.append(temp)

    print(total[-1][-1])


if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())

    items = []

    for item in range(N):
        input_dat = tuple(map(int, sys.stdin.readline().split()))
        if input_dat not in items:
            items.append(input_dat)
    items.sort(reverse=True)

    searching(K, items)
