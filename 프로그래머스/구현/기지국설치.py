def solution(n, stations, w):
    answer = 0
    
    com = w*2+1

    s = 0
    for station in stations:
        a = station - w - 1
        dis = a - s
        if a > s:
            if dis % com == 0:
                answer += (dis // com)
            else:
                answer += (dis // com + 1)
        s = station + w
        
    
    if s < n:
        dis = n - s 
        if dis % com == 0:
            answer += (dis // com)
        else:
            answer += (dis // com) + 1
    
    

    return answer