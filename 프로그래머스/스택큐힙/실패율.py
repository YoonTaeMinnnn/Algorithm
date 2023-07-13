def solution(N, stages):
    answer = []
    mapping = []
    total = len(stages)
    for i in range(1,N+1):  #1~5
        if total != 0:
            fail = stages.count(i)
            fail_rate = fail / total
            total -= fail
            mapping.append((i,fail_rate))
        else :
            mapping.append((i,0))
    mapping.sort(key = lambda x : x[1], reverse = True)
    for i in mapping:
        answer.append(i[0])
    return answer