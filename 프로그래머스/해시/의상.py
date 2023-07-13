# 모든 경우의 수 : 각 원소의 곱 - 1 (모두 포함하지 않는 경우)
def solution(clothes):
    answer = 1
    d = dict()
    for c, t in clothes:
        d[t] = d.get(t, 0) + 1
    
    for i in d.values():
        answer *= (i+1)
    
    return answer-1
