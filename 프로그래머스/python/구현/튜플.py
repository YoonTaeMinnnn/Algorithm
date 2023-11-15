def solution(s):
    answer = []
    
    s = s[2:-2].split('},{')
    
    l = []
    for i in s:
        a = i.split(',')
        l.append(a)
    l.sort(key = lambda x : len(x))
    
    
    d = dict()
    for i in range(len(l)):
        for j in range(len(l[i])):
            if d.get(l[i][j], 0) == 0:
                d[l[i][j]] = 1
                answer.append(int(l[i][j]))
    
    return answer