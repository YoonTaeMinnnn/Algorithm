def solution(s):
    answer = []
    d = dict()
    for key, value in enumerate(s):
        if value in d:
            answer.append(key - d[value])
        else:
            answer.append(-1)
        d[value] = key
            
        
    return answer