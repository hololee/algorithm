def solution(board, moves):
    board = [list(item)for item in zip(*board)]

    answer =0

    def pickup(line):
        for idx, item in enumerate(line):
            if item > 0:
                if idx ==0:
                    line[idx] = 0
                    return line, item
                else:
                    item = line[idx]
                    line[idx] = 0
                    return line, item

    bucket = []

    # index 형으로 변경.
    moves = [i -1 for i in moves]

    for pos in moves:
        if board[pos][-1] > 0: # 비었는지 체크.
            line, item = pickup(board[pos])
            board[pos] = line
            bucket.append(item)

            # 마지막 2개가 같은지 체크.
            if len(bucket) >= 2 and bucket[-2] == bucket[-1]:
                del bucket[-2:]
                answer+=2

    return answer