def solution(N, stages):
    answer = []
    mapping = []
    for i in range(1,N+1):  #1~5
        cnt = 0
        s = 0
        result = 0
        for j in stages:       #1~6
            if j >= i :
                s+=1
            if j == i:
                cnt+=1
        if s == 0:
            result = 0
            continue
        result = cnt / s
        mapping.append((i,result))  #(1,실패율), (2,실패율)
    mapping.sort(key = lambda x : x[1], reverse=True)
    print(mapping)
    for i in mapping:
        answer.append(i[0])
    return answer


