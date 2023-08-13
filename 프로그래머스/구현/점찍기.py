def solution(k, d):
    global answer
    answer = 0
    
    for x in range(0, d+1, k):
        y = int( (d**2 - x**2)**(1/2))
        answer += (y // k + 1) 
        
    print(answer)
    return answer