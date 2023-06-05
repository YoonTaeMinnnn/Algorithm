def solution(k, m, score):
    answer = 0
    s = len(score)
    n = s // m
    score.sort(reverse = True)
    result = []
    com = 0
    for _ in range(n):
        l = score[com:com+m]
        answer += min(l)*m
        com = com + m
    
    return answer