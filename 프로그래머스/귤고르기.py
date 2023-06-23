def solution(k, tangerine):
    answer = 0
    d = dict()
    for i in tangerine:
        d[i] = d.get(i, 0) + 1
    
    a = sorted(d.items(), reverse = True, key = lambda x : x[1])
   
    l = []
    cnt = 0
    for i in a:
        if cnt >= k:
            return answer
        cnt += i[1]
        answer += 1
    
    return answer