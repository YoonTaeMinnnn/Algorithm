def solution(name, yearning, photo):
    answer = []
    d = dict()
    for i in range(len(name)):
        d[name[i]] = yearning[i]
    for i in range(len(photo)):
        sum = 0
        for j in range(len(photo[i])):
            sum += d.get(photo[i][j], 0)
        answer.append(sum)
    
    return answer