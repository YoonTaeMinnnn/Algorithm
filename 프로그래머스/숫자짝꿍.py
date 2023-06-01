def solution(X, Y):
    answer = ''
    X = str(X)
    Y = str(Y)
    d1 = dict()
    d2 = dict()
    for i in X:
        d1[i] = d1.get(i, 0) + 1
    for i in Y:
        d2[i] = d2.get(i, 0) + 1
    
    for key, value in d1.items():
        if d2.get(key, 0) == 0:
            continue
        if d1[key] == d2.get(key, 0) or d1[key] < d2.get(key, 0):
            answer += key*value
        elif d1[key] > d2.get(key, 0):
            answer += key*d2[key]
    
            
    if len(answer) == 0:
        return "-1"
    
    answer = list(answer)
    answer.sort(reverse = True)
    result =""
    cnt = 0
    for i in answer:
        result += i
        if i == "0":
            cnt += 1
    if cnt == len(answer):
        return "0"
    return result