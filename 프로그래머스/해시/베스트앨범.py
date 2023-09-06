def solution(genres, plays):
    answer = []
    d1 = dict()
    d2 = dict()
    
    for i in range(len(genres)):
        d1[genres[i]] = d1.get(genres[i], 0) + plays[i]
    
    l = list(d1.items())
    l = sorted(l, key = lambda x : x[1], reverse = True)
    
    for i in range(len(genres)):
        d2[genres[i]] = d2.get(genres[i], []) + [[i, plays[i]]]
    
    for i in l:
        a = d2[i[0]]
        a.sort(key = lambda x : (x[1], -x[0]))
        cnt = 0
        while a and cnt < 2:
            answer.append(a.pop()[0])
            cnt += 1
        
    
    return answer