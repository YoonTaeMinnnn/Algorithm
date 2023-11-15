def solution(want, number, discount):
    answer = 0
    d = dict()
    
    for i in range(len(discount)-10+1):
        for z in range(len(want)):
            d[want[z]] = number[z]
        l = discount[i:i+10]
        for j in l:
            if j in d.keys():
                d[j] -= 1
        if all(x == 0 for x in d.values()):
            answer += 1
        
            
    return answer