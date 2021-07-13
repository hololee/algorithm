def solution(participant, completion):
    answer = list(set(participant) - set(completion))
    if len(answer):
        return answer[0]
    else:
        temp = [x for x in participant if x not in set(completion)]
        return temp